from odoo import models, fields, api, _

class NIInterfaces(models.Model):
    _name = 'ni.interfaces'
    _description = "Device Interfaces"

    device_id = fields.Many2one('ni.devices')
    intf_name = fields.Char(string="Interface Name", required=True)
    intf_ip = fields.Char(string="IP Address")
    intf_mac = fields.Char(string="Interface MAC Address")
    link_type_id = fields.Many2one('ni.interfaces.link.type', string="Link Type")
    intf_peer = fields.Many2one('ni.devices')
    intf_description = fields.Char(string="Description")


class NILinkType(models.Model):
    _name = 'ni.interfaces.link.type'
    _description = "Link Type"

    name = fields.Char(string="Link Type")


