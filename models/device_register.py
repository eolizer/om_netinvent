from odoo import models, fields, api, _

class NIDeviceRegister(models.Model):
    _name = 'ni.device.register'
    _description = "Device register"

    # name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    vendor = fields.Char(string="Vendor")
    model = fields.Char(string="Model")
    category = fields.Many2one('ni.device.categories', string="Device Category")

    def name_get(self):
        result = []
        for rec in self:
            name = '%s %s' % (rec.vendor, rec.model)
            result.append((rec.id, name))
        return result