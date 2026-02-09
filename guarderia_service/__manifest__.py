# -*- coding: utf-8 -*-
{
    'name': 'Servicio de Guarderia',
    'version': '1.0',
    'summary': 'Gestion de servicios de guarderia con herencia por delegacion',
    'description': """
        Modulo de Servicio de Guarderia
        ================================
        
        Este modulo implementa un servicio de guarderia que hereda de:
        - hr.employee: Para gestionar el monitor del servicio
        - calendar.event: Para gestionar los horarios del servicio
        
        Caracteristicas:
        - Herencia por delegacion (_inherits)
        - Campos personalizados: descripcion y rango de edad
        - Grupos de seguridad: usuario y administrador
        - Vistas completas: formulario, lista y busqueda
    """,
    'category': 'Human Resources',
    'author': 'omq',
    'depends': ['hr', 'calendar', 'hr_employee_extension'],
    'data': [
        'security/guarderia_security.xml',
        'security/ir.model.access.csv',
        'views/guarderia_service_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
