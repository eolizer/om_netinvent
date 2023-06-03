from odoo import models, fields, api, _


class NIDevices(models.Model):
    _name = 'ni.devices'
    _description = "Network Devices"
    _rec_name = 'hostname'

    hostname = fields.Char(string="Hostname", required=True)
    serial_number = fields.Char(string="Serial Number")
    description = fields.Char(string="Description")
    tag_ids = fields.Many2many('ni.settings.tags', string="Tags")
    devitem_id = fields.Many2one('ni.device.register', string="Device Item")
    network_id = fields.Many2one('ni.networks')
    location = fields.Char(string="Location")
    resp_user = fields.Char(string="Responsible User")

    # Management Access
    mgmt_ip = fields.Char(string="Management IP Address")
    mgmt_vlan = fields.Char(string="Management VLAN")
    mgmt_mac = fields.Char(string="Management Interface MAC")
    mgmt_web = fields.Boolean(string="Management Web Interface")
    mgmt_ssh = fields.Boolean(string="Management SSH Interface")
    mgmt_telnet = fields.Boolean(string="Management Telnet Interface")

    add_info = fields.Text(string="Additional Info")

    # Maintenance
    mnt_ids = fields.One2many('ni.maintenance', 'device_id')
    # Interfaces
    intf_ids = fields.One2many('ni.interfaces', 'device_id')
