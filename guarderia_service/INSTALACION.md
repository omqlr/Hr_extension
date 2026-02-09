# Instrucciones de Instalacion - Modulo Guarderia

## Modulo sin Tildes - Listo para Instalar

Se han eliminado todas las tildes del modulo para evitar problemas de codificacion.

## Opcion 1: Instalar via Interfaz de Odoo

1. **Actualizar lista de aplicaciones:**
   - Ir a **Apps** (Aplicaciones)
   - Click en el menu de 3 puntos (esquina superior derecha)
   - Seleccionar **Update Apps List** (Actualizar Lista de Aplicaciones)
   - Confirmar la actualizacion

2. **Buscar e instalar:**
   - En el buscador, escribir: `Guarderia`
   - Deberia aparecer: **Servicio de Guarderia**
   - Click en **Install** (Instalar)

3. **Acceder al modulo:**
   - Ir al menu principal
   - Buscar **Guarderia**
   - Click en **Servicios de Guarderia**

## Opcion 2: Instalar via Linea de Comandos

```bash
# Desde el directorio de Odoo
./odoo-bin -c odoo.conf -u guarderia_service -d nombre_base_datos

# O si usas python directamente
python3 odoo-bin -c odoo.conf -u guarderia_service -d nombre_base_datos
```

## Opcion 3: Modo Desarrollo (Recomendado para pruebas)

```bash
# Reiniciar Odoo en modo desarrollo con actualizacion
./odoo-bin -c odoo.conf -u guarderia_service -d nombre_base_datos --dev=all
```

## Verificar Instalacion

1. **Comprobar que el modulo esta instalado:**
   - Ir a **Apps**
   - Buscar `Guarderia`
   - Deberia mostrar estado: **Installed** (verde)

2. **Comprobar el menu:**
   - En el menu principal deberia aparecer **Guarderia**
   - Al hacer click deberia mostrar **Servicios de Guarderia**

## Crear un Servicio de Prueba

1. Ir a **Guarderia > Servicios de Guarderia**
2. Click en **Create** (Crear)
3. Rellenar los campos:
   - **Nombre del Monitor**: Maria Garcia
   - **Work Email**: maria@example.com
   - **Hora de Inicio**: Manana a las 09:00
   - **Hora de Fin**: Manana a las 17:00
   - **Rango de Edad**: 3-5 anos
   - **Descripcion**: Servicio de guarderia para ninos de preescolar
4. Click en **Save** (Guardar)

## Verificar Herencia por Delegacion

Despues de crear un servicio:

1. **Verificar empleado creado:**
   - Ir a **Employees** (Empleados)
   - Deberia aparecer "Maria Garcia"

2. **Verificar evento creado:**
   - Ir a **Calendar** (Calendario)
   - Deberia aparecer el evento con el horario

3. **Verificar acceso directo a campos:**
   - En el formulario de guarderia, los campos `name`, `work_email`, `start`, `stop` son accesibles directamente
   - NO necesitas usar `employee_id.name` o `event_id.start`

## Solucionar Problemas

### Error: "Module not found"
```bash
# Verificar que el modulo esta en la ruta correcta
ls /home/omq/odoo/addons/guarderia_service/

# Reiniciar Odoo
sudo systemctl restart odoo
# O si lo ejecutas manualmente, detener y volver a iniciar
```

### Error: "Access Denied"
- Asegurate de tener permisos de administrador
- Asigna el grupo "Administrador de Guarderia" a tu usuario

### Error de Sintaxis
```bash
# Verificar sintaxis Python
cd /home/omq/odoo/addons/guarderia_service
python3 -m py_compile models/guarderia_service.py

# Si hay errores, revisar el archivo
```

## Desinstalar (si es necesario)

1. Ir a **Apps**
2. Buscar `Guarderia`
3. Click en el modulo
4. Click en **Uninstall** (Desinstalar)
5. Confirmar

## Archivos del Modulo

```
/home/omq/odoo/addons/guarderia_service/
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

## Caracteristicas Implementadas

✓ Herencia por delegacion de `hr.employee` y `calendar.event`
✓ Campos personalizados: `description` y `age_range`
✓ Grupos de seguridad: Usuario y Administrador
✓ Vistas completas: Formulario, Lista, Busqueda
✓ Filtros por rango de edad
✓ Sin tildes (sin problemas de codificacion)
