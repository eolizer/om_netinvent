from odoo import models, fields, api, _

class NIDeviceCategories(models.Model):
    _name = 'ni.device.categories'
    _description = "Network device categories"

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
