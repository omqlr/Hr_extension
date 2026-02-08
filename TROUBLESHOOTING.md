# Guía de Solución: Módulo no aparece en Odoo

## Problema
El módulo `hr_employee_extension` no aparece en la lista de aplicaciones de Odoo.

## Verificación realizada ✅
- Estructura de archivos correcta
- Sintaxis de Python correcta
- `__manifest__.py` bien formado
- Archivos `__init__.py` en su lugar

## Soluciones paso a paso

### 1. Reiniciar el servidor Odoo (IMPORTANTE)
```bash
# Detener el servidor Odoo si está corriendo
# Luego reiniciarlo con el parámetro --update-addons-path o -u all
```

### 2. Actualizar la lista de aplicaciones en Odoo

**Opción A: Desde la interfaz web**
1. Ir a **Aplicaciones** (Apps)
2. Hacer clic en el menú de tres puntos (⋮) o en "Actualizar lista de aplicaciones"
3. Si no ves esta opción, activa el **Modo Desarrollador**:
   - Ir a **Ajustes** (Settings)
   - Scroll hasta el final
   - Hacer clic en "Activar modo desarrollador"
   - Volver a **Aplicaciones**
   - Ahora deberías ver "Actualizar lista de aplicaciones"

**Opción B: Desde línea de comandos**
```bash
# Navegar al directorio de Odoo
cd /home/omq/odoo

# Actualizar módulo (reemplaza 'tu_base_de_datos' con el nombre real)
./odoo-bin -d tu_base_de_datos -u hr_employee_extension --stop-after-init

# O actualizar todos los módulos
./odoo-bin -d tu_base_de_datos -u all --stop-after-init
```

### 3. Verificar que la ruta de addons esté configurada

El servidor Odoo debe conocer la ruta `/home/omq/odoo/addons`. Verifica en:

**Archivo de configuración de Odoo** (normalmente `odoo.conf` o `.odoorc`):
```ini
[options]
addons_path = /home/omq/odoo/addons,/ruta/a/otros/addons
```

O al iniciar Odoo:
```bash
./odoo-bin --addons-path=/home/omq/odoo/addons
```

### 4. Buscar el módulo en Odoo

Una vez actualizada la lista:
1. Ir a **Aplicaciones**
2. Quitar el filtro "Apps" (buscar todos los módulos)
3. Buscar: **"HR Employee Extension"** o **"NSS"** o **"DNI"**

### 5. Verificar logs de Odoo

Si aún no aparece, revisa los logs del servidor Odoo para ver si hay errores al cargar el módulo.

## Checklist de verificación

- [ ] Servidor Odoo reiniciado
- [ ] Modo desarrollador activado
- [ ] Lista de aplicaciones actualizada
- [ ] Filtro "Apps" desactivado en la búsqueda
- [ ] Ruta de addons incluye `/home/omq/odoo/addons`
- [ ] Módulo `hr` (Human Resources) instalado previamente

## Nota importante

⚠️ **El módulo `hr` debe estar instalado primero** porque `hr_employee_extension` depende de él. Si no tienes instalado el módulo de Recursos Humanos, instálalo primero.
