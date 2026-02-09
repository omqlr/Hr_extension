#!/bin/bash
# Script para actualizar el modulo guarderia_service en Odoo

echo "=== Actualizando modulo guarderia_service ==="
echo ""

# Opcion 1: Si Odoo esta corriendo como servicio
echo "Opcion 1: Actualizar via systemctl"
echo "sudo systemctl stop odoo"
echo "./odoo-bin -c /etc/odoo/odoo.conf -u guarderia_service -d NOMBRE_BASE_DATOS --stop-after-init"
echo "sudo systemctl start odoo"
echo ""

# Opcion 2: Si ejecutas Odoo manualmente
echo "Opcion 2: Actualizar directamente"
echo "./odoo-bin -c odoo.conf -u guarderia_service -d NOMBRE_BASE_DATOS"
echo ""

# Opcion 3: Modo desarrollo
echo "Opcion 3: Actualizar en modo desarrollo"
echo "./odoo-bin -c odoo.conf -u guarderia_service -d NOMBRE_BASE_DATOS --dev=all"
echo ""

echo "Despues de actualizar:"
echo "1. Ve a Settings → Users & Companies → Users"
echo "2. Selecciona tu usuario"
echo "3. En Access Rights, marca: 'Guarderia: Usuario de Guarderia'"
echo "4. Save y refresca la pagina (F5)"
echo ""
echo "El menu 'Guarderia' deberia aparecer en la barra superior"
