from odoo import models, fields


class SaleResponsible(models.Model):
    _inherit = 'sale.order'
    responsible = fields.Many2one('hr.employee', string='Responsible', required=True)
