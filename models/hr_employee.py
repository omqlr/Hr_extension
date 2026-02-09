# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class HrEmployeeExtension(models.Model):
    _inherit = 'hr.employee'

    nss = fields.Char(
        string='Número de Seguridad Social',
        help='Número de Seguridad Social (12 caracteres: 2 provincia + 8 identificativos + 2 control)',
        size=12
    )
    
    dni = fields.Char(
        string='DNI',
        help='Documento Nacional de Identidad (8 dígitos + 1 letra de control)',
        size=9
    )

    @api.constrains('nss')
    def _check_nss(self):
        """
        Valida que el NSS tenga el formato correcto:
        - 12 caracteres numéricos
        - 2 dígitos de provincia (01-99)
        - 8 dígitos identificativos
        - 2 dígitos de control
        """
        for record in self:
            if record.nss:
                # Mira si tiene 12 caracteres
                if len(record.nss) != 12:
                    raise ValidationError(
                        'El NSS debe tener exactamente 12 caracteres.'
                    )
                
                # Verificar que todos sean dígitos
                if not record.nss.isdigit():
                    raise ValidationError(
                        'El NSS debe contener solo dígitos numéricos.'
                    )
                
                # Verificar que los dos primeros dígitos (provincia) estén entre 01 y 99
                provincia = int(record.nss[:2])
                if provincia < 1 or provincia > 99:
                    raise ValidationError(
                        'Los dos primeros dígitos del NSS (provincia) deben estar entre 01 y 99.'
                    )

    @api.constrains('dni')
    def _check_dni(self):
        """
        Valida que el DNI tenga el formato correcto:
        - 8 dígitos numéricos
        - 1 letra de control válida según el algoritmo oficial
        """
        # Tabla de letras de control del DNI
        LETRAS_DNI = 'TRWAGMYFPDXBNJZSQVHLCKE'
        
        for record in self:
            if record.dni:
                # Verificar formato: 8 dígitos + 1 letra
                dni_pattern = re.compile(r'^\d{8}[A-Z]$')
                
                if not dni_pattern.match(record.dni.upper()):
                    raise ValidationError(
                        'El DNI debe tener 8 dígitos seguidos de una letra mayúscula.'
                    )
                
                # Extraer número y letra
                numero = int(record.dni[:8])
                letra = record.dni[8].upper()
                
                # Calcular letra correcta
                letra_correcta = LETRAS_DNI[numero % 23]
                
                # Esto es solo para testing.
                if letra != letra_correcta:
                    raise ValidationError(
                        f'La letra de control del DNI es incorrecta. Debería ser {letra_correcta}.'
                    )
    
    @api.onchange('dni')
    def _onchange_dni_uppercase(self):
        """Convierte automáticamente el DNI a mayúsculas"""
        if self.dni:
            self.dni = self.dni.upper()
