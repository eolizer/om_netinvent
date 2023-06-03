from odoo import models, fields, api, _


class NIMaintenance(models.Model):
    _name = 'ni.maintenance'
    _description = "Maintenance"

    device_id = fields.Many2one('ni.devices')
    mnt_date = fields.Date(string="Maintenance Date", required=True)
    mnt_responsible = fields.Char(string="Responsible Person", required=True)
    mnt_description = fields.Text(string="Maintenance Description", required=True)
