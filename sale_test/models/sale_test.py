from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import string
import random


class SaleResponsible(models.Model):
    _inherit = 'sale.order'
    test = fields.Char(
        string='Test',
        readonly=True,
        states={'draft': [('readonly', False)]}
    )
    date_order = fields.Datetime(default=None)

    @api.onchange('date_order', 'order_line')
    def onchange_date_order_amount_total(self):
        if self.date_order:
            self.test = '%(amount_total).2f - %(date_order)s' % {
                'amount_total': self.amount_total,
                'date_order': self.date_order.strftime('%d/%m/%Y %H:%M:%S')
            }

    @api.constrains('test')
    def check_test(self):
        for record in self:
            if record.test:
                if len(record.test) > 50:
                    raise ValidationError(_('The length of the text must be less than 50 characters!'))
    
    @api.model
    def default_get(self, fields):
        res = super(SaleResponsible, self).default_get(fields)
        res['test'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        return res
