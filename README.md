# HR Employee Extension - NSS y DNI

Módulo de Odoo que extiende `hr.employee` para incluir campos de Número de Seguridad Social (NSS) y DNI con validación automática.

## Características

### Campos añadidos:
- **NSS (Número de Seguridad Social)**: Campo de 12 caracteres
- **DNI**: Campo de 8 dígitos + 1 letra de control

### Validaciones implementadas:

#### NSS:
- Exactamente 12 caracteres numéricos
- Formato: 2 dígitos de provincia (01-99) + 8 dígitos identificativos + 2 dígitos de control
- Validación automática al guardar

#### DNI:
- 8 dígitos numéricos + 1 letra de control
- Validación de la letra de control según el algoritmo oficial del DNI español
- Conversión automática a mayúsculas
- Mensaje de error indicando la letra correcta si es incorrecta

## Instalación

1. Copiar el módulo a la carpeta de addons de Odoo
2. Actualizar la lista de aplicaciones
3. Instalar el módulo "HR Employee Extension - NSS y DNI"

## Uso

Los campos NSS y DNI aparecen en el formulario de empleado, después del campo de identificación.

## Ejemplos válidos:

- **NSS**: `281234567890` (28 = provincia de Madrid)
- **DNI**: `12345678Z` (la letra Z es la correcta para el número 12345678)

## Autor

omq - 2ºDAM Sistemas de Gestión Empresarial
