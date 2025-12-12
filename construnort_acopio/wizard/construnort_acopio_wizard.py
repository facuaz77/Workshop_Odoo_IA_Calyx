# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ConstrunortAcopioWizard(models.TransientModel):
    _name = 'construnort.acopio.wizard'
    _description = 'Wizard de Acopio'

    check_process = fields.Boolean(
        string='Confirmar Proceso',
        help='Marque esta casilla para confirmar el proceso de acopio'
    )

    def action_confirm_acopio(self):
        """Método para confirmar el acopio y cambiar el estado de la orden"""
        self.ensure_one()
        
        if not self.check_process:
            raise UserError(_('Debe marcar la casilla de confirmación para proceder con el acopio.'))
        
        # Obtener la orden de venta desde el contexto
        active_id = self.env.context.get('active_id')
        if not active_id:
            raise UserError(_('No se encontró una orden de venta activa.'))
        
        sale_order = self.env['sale.order'].browse(active_id)
        
        # Cambiar el estado a 'acopio'
        sale_order.write({'state': 'acopio'})
        
        return {'type': 'ir.actions.act_window_close'}
