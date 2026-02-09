# Servicio de Guardería - Módulo Odoo

## Descripción

Este módulo implementa un servicio de guardería para empleados utilizando **herencia por delegación** (`_inherits`) en Odoo. El módulo hereda simultáneamente de dos modelos:

- **`hr.employee`**: Para gestionar el monitor del servicio de guardería
- **`calendar.event`**: Para representar los horarios en los que el servicio está abierto

## Características Principales

### Herencia por Delegación
El modelo `guarderia.service` utiliza `_inherits` para heredar de ambos modelos padre. Esto significa que:
- Al crear un servicio de guardería, se crean automáticamente un empleado y un evento de calendario
- Los campos de ambos modelos son **directamente accesibles** sin necesidad de usar notación Many2one
- Por ejemplo: `record.name` en lugar de `record.employee_id.name`

### Campos Personalizados
- **Descripción** (`description`): Campo de texto para describir el servicio
- **Rango de Edad** (`age_range`): Selección con opciones:
  - 0-2 años
  - 3-5 años
  - 6-8 años
  - 9-11 años

### Campos Heredados Accesibles

#### De `hr.employee`:
- `name`: Nombre del monitor
- `work_email`: Email de trabajo
- `work_phone`: Teléfono de trabajo
- `department_id`: Departamento
- `job_id`: Puesto de trabajo
- `mobile_phone`: Teléfono móvil
- `work_location_id`: Ubicación de trabajo
- `company_id`: Compañía

#### De `calendar.event`:
- `start`: Hora de inicio del servicio
- `stop`: Hora de fin del servicio
- `duration`: Duración en horas
- `location`: Ubicación del servicio
- `partner_ids`: Padres que dejan a sus hijos (participantes)

## Seguridad

### Grupos de Seguridad
1. **Usuario de Guardería** (`group_guarderia_user`):
   - Permisos: Lectura, Escritura, Creación
   - No puede eliminar registros

2. **Administrador de Guardería** (`group_guarderia_manager`):
   - Permisos: Lectura, Escritura, Creación, Eliminación
   - Acceso completo al módulo

## Vistas

### Vista de Formulario
Organizada en secciones:
- **Información del Monitor**: Campos del empleado
- **Horario del Servicio**: Campos del evento
- **Información del Servicio**: Campos personalizados
- **Participantes**: Padres registrados (Many2many)
- **Información Adicional del Monitor**: Datos complementarios

### Vista de Lista
Muestra columnas clave:
- Monitor
- Rango de edad
- Inicio y fin del servicio
- Ubicación
- Departamento

### Vista de Búsqueda
Incluye:
- Filtros por rango de edad (0-2, 3-5, 6-8, 9-11)
- Filtro "Hoy" para servicios del día actual
- Agrupación por: rango de edad, departamento, ubicación

## Instalación

1. Copiar el módulo a la carpeta `addons` de Odoo
2. Actualizar la lista de aplicaciones
3. Buscar "Servicio de Guardería"
4. Instalar el módulo

## Dependencias

- `hr`: Módulo de Recursos Humanos
- `calendar`: Módulo de Calendario

## Uso

1. Ir a **Guardería > Servicios de Guardería**
2. Crear un nuevo registro
3. Rellenar los datos del monitor (nombre, email, teléfono, etc.)
4. Definir el horario del servicio (inicio, fin, ubicación)
5. Seleccionar el rango de edad
6. Añadir una descripción
7. Añadir padres como participantes
8. Guardar

## Estructura del Módulo

```
guarderia_service/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── guarderia_service.py
├── security/
│   ├── guarderia_security.xml
│   └── ir.model.access.csv
└── views/
    └── guarderia_service_views.xml
```

## Autor

omq - 2ºDAM Sistemas de Gestión Empresarial

## Licencia

LGPL-3
