# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GuarderiaService(models.Model):
    _name = 'guarderia.service'
    _description = 'Servicio de Guarderia'
    _rec_name = 'name'  # Usar el campo name heredado de employee
    _inherits = {
        'hr.employee': 'employee_id',
        'calendar.event': 'event_id'
    }

    # Campos Many2one para la herencia por delegacion
    employee_id = fields.Many2one(
        'hr.employee',
        string='Monitor',
        required=True,
        ondelete='cascade',
        auto_join=True,
        index=True,
        help='Empleado que actua como monitor del servicio de guarderia'
    )
    
    event_id = fields.Many2one(
        'calendar.event',
        string='Evento',
        required=True,
        ondelete='cascade',
        auto_join=True,
        index=True,
        help='Evento de calendario que representa el horario del servicio'
    )

    # Campos personalizados
    description = fields.Text(
        string='Descripcion',
        help='Descripcion detallada del servicio de guarderia'
    )
    
    age_range = fields.Selection(
        [
            ('0-2', '0-2 anos'),
            ('3-5', '3-5 anos'),
            ('6-8', '6-8 anos'),
            ('9-11', '9-11 anos'),
        ],
        string='Rango de Edad',
        help='Rango de edad de los ninos para este servicio'
    )

    @api.model
    def create(self, vals):
        """
        Override create para manejar manualmente la creacion de employee y event
        debido a que calendar.event tiene un campo 'name' computed
        """
        # Crear el empleado primero
        employee_vals = {}
        if 'name' in vals:
            employee_vals['name'] = vals['name']
        if 'work_email' in vals:
            employee_vals['work_email'] = vals.pop('work_email')
        if 'work_phone' in vals:
            employee_vals['work_phone'] = vals.pop('work_phone')
        if 'department_id' in vals:
            employee_vals['department_id'] = vals.pop('department_id')
        if 'job_id' in vals:
            employee_vals['job_id'] = vals.pop('job_id')
        if 'mobile_phone' in vals:
            employee_vals['mobile_phone'] = vals.pop('mobile_phone')
        if 'work_location_id' in vals:
            employee_vals['work_location_id'] = vals.pop('work_location_id')
        if 'company_id' in vals:
            employee_vals['company_id'] = vals.pop('company_id')
        
        employee = self.env['hr.employee'].create(employee_vals)
        vals['employee_id'] = employee.id
        
        # Crear el evento
        event_vals = {}
        if 'name' in vals:
            # Usar el nombre del empleado como nombre del evento
            event_vals['name'] = 'Servicio de Guarderia - ' + vals['name']
        if 'start' in vals:
            event_vals['start'] = vals.pop('start')
        if 'stop' in vals:
            event_vals['stop'] = vals.pop('stop')
        if 'location' in vals:
            event_vals['location'] = vals.pop('location')
        if 'duration' in vals:
            event_vals['duration'] = vals.pop('duration')
        if 'partner_ids' in vals:
            event_vals['partner_ids'] = vals.pop('partner_ids')
        
        event = self.env['calendar.event'].create(event_vals)
        vals['event_id'] = event.id
        
        # Ahora crear el registro de guarderia
        return super(GuarderiaService, self).create(vals)

    def write(self, vals):
        """
        Override write para sincronizar cambios con employee y event
        """
        # Actualizar employee si hay cambios en sus campos
        employee_vals = {}
        for field in ['name', 'work_email', 'work_phone', 'department_id', 'job_id', 
                      'mobile_phone', 'work_location_id', 'company_id']:
            if field in vals:
                employee_vals[field] = vals[field]
        
        if employee_vals:
            self.employee_id.write(employee_vals)
        
        # Actualizar event si hay cambios en sus campos
        event_vals = {}
        for field in ['start', 'stop', 'location', 'duration', 'partner_ids']:
            if field in vals:
                event_vals[field] = vals[field]
        
        if event_vals:
            self.event_id.write(event_vals)
        
        return super(GuarderiaService, self).write(vals)

    def unlink(self):
        """
        Override unlink para asegurar la eliminacion en cascada
        """
        employees = self.mapped('employee_id')
        events = self.mapped('event_id')
        
        result = super(GuarderiaService, self).unlink()
        
        # Eliminar employees y events huerfanos
        employees.unlink()
        events.unlink()
        
        return result
