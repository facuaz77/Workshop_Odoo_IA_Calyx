# Construnort Acopio

Módulo Odoo 15 para agregar un estado de "Acopio" a las órdenes de venta y un wizard de confirmación.

Características principales:
- Añade la opción `acopio` al campo `state` de `sale.order`.
- Añade un wizard (`construnort.acopio.wizard`) con un campo booleano `check_process`.
- Botón "Acopio" en el encabezado del formulario de la orden de venta que abre el wizard.
- Grupo de seguridad `Construct Acopio` para controlar la visibilidad del botón.

Dependencias:
- `base`
- `sale_management`

Archivos importantes:
- `models/sale_order.py` - Extiende `sale.order` añadiendo el estado `acopio`.
- `wizard/construnort_acopio_wizard.py` - Wizard para confirmar y cambiar el estado.
- `views/sale_order_views.xml` - Inserta el botón en el formulario de la orden y agrega el estado al statusbar.
- `wizard/construnort_acopio_wizard_views.xml` - Vista y acción del wizard.
- `security/security_groups.xml` - Define el grupo `Construct Acopio`.
- `security/ir.model.access.csv` - Permisos para el wizard.

Instalación:
1. Copiar el módulo a tu carpeta de `addons` (por ejemplo `/mnt/extra-addons`).
2. Reiniciar el servidor Odoo.
3. Actualizar la lista de Apps y buscar "Construnort Acopio".
4. Instalar el módulo.

Uso:
- Desde una orden de venta, si el usuario pertenece al grupo `Construct Acopio`, verá el botón "Acopio" en el header. Al presionar, se abre un wizard que solicita marcar la casilla de confirmación; al confirmar, la orden pasará a estado `acopio`.

Notas:
- Este módulo no añade cambios en el flujo de ventas más allá del estado y el wizard; adáptalo según necesidad.
