from odoo import models, fields, _

class nando_purchase(models.Model):
    _name = 'nando.purchase'

    name = fields.Char(string='Name')
    tanggal = fields.Date(string='Tanggal')
    status = fields.Selection([('draft','Draft'), ('approve','Approve'), ('done','Done')])
