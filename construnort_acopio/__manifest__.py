# -*- coding: utf-8 -*-
{
    'name': 'Construnort Acopio',
    'version': '15.0.1.0.0',
    'category': 'Sales',
    'summary': 'Módulo de acopio para órdenes de venta',
    'description': """
        Módulo que agrega funcionalidad de acopio a las órdenes de venta.
        - Nuevo estado 'acopio' en sale.order
        - Wizard para procesar el acopio
        - Grupo de seguridad para control de acceso
    """,
    'author': 'Facundo Alaniz',
    'website': 'https://www.construnort.com',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'wizard/construnort_acopio_wizard_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
