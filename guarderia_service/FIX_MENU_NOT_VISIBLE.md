# Solucion: Menu Guarderia No Aparece

## Problema
El menu "Guarderia" no aparece en la barra superior de Odoo despues de instalar el modulo.

## Causa
Los menuitem no tenian el atributo `groups` especificado. Esto puede causar que el menu no sea visible para ciertos usuarios, especialmente si no son administradores.

## Solucion Aplicada

### Cambios en views/guarderia_service_views.xml:

**Menu Principal (linea 117-119):**
```xml
<!-- ANTES -->
<menuitem id="menu_guarderia_root"
          name="Guarderia"
          sequence="60"/>

<!-- DESPUES -->
<menuitem id="menu_guarderia_root"
          name="Guarderia"
          groups="guarderia_service.group_guarderia_user"
          sequence="60"/>
```

**Submenu (linea 122-126):**
```xml
<!-- ANTES -->
<menuitem id="menu_guarderia_services"
          name="Servicios de Guarderia"
          parent="menu_guarderia_root"
          action="action_guarderia_service"
          sequence="10"/>

<!-- DESPUES -->
<menuitem id="menu_guarderia_services"
          name="Servicios de Guarderia"
          parent="menu_guarderia_root"
          action="action_guarderia_service"
          groups="guarderia_service.group_guarderia_user"
          sequence="10"/>
```

## Pasos para Aplicar la Solucion

### Opcion 1: Actualizar el Modulo (Recomendado)

```bash
./odoo-bin -c odoo.conf -u guarderia_service -d tu_base_datos
```

### Opcion 2: Via Interfaz de Odoo

1. **Activar modo desarrollador:**
   - Settings (Configuracion) → Activate Developer Mode

2. **Actualizar el modulo:**
   - Apps → Buscar "Guarderia"
   - Click en el modulo
   - Click en "Upgrade" (Actualizar)

### Opcion 3: Reiniciar Odoo

Si usas systemctl:
```bash
sudo systemctl restart odoo
```

## Asignar Permisos al Usuario

Despues de actualizar, asegurate de que tu usuario tiene los permisos:

1. **Settings → Users & Companies → Users**
2. **Selecciona tu usuario**
3. **En la pestana "Access Rights"**, busca:
   - **Guarderia: Usuario de Guarderia** ✓
   - O **Guarderia: Administrador de Guarderia** ✓
4. **Save**

## Verificacion

Despues de actualizar y asignar permisos:

1. **Refresca la pagina** (F5)
2. **Busca el menu "Guarderia"** en la barra superior
3. Deberia aparecer junto a otros menus

## Si Aun No Aparece

### Verificar instalacion:
1. Apps → Buscar "Guarderia"
2. Verificar que dice "Installed" (verde)

### Verificar permisos:
1. Settings → Technical → Security → Groups
2. Buscar "Usuario de Guarderia"
3. Verificar que tu usuario esta en la lista de usuarios

### Ver logs de Odoo:
```bash
tail -f /var/log/odoo/odoo.log
```
Buscar errores relacionados con `guarderia_service`
