from odoo import models, fields, api, _


class NINetworks(models.Model):
    _name = 'ni.networks'
    _description = 'Networks'

    _sql_constraints = [
        ('name_uniq', 'unique(name)', "Network with the same name already exists")
    ]

    name = fields.Char(string="Network Name", required=True)
    description = fields.Char(string="Network Description")
    tag_ids = fields.Many2many('ni.settings.tags', string="Tags")
    range_ids = fields.One2many('ni.network.range', 'net_id')
    range_ids_str = fields.Char(compute='_get_range_ids_str', string="Network Ranges")  # Comma-separated string representation of IP ranges

    def _get_range_ids_str(self):
        for rec in self:
            rec.range_ids_str = ', '.join(rec.range_ids.mapped('ip_range'))


class NINetworkIPRanges(models.Model):
    _name = 'ni.network.range'
    _device = "Network IP Ranges"
    _rec_name = 'ip_range'

    _sql_constraints = [
        ('ip_range_uniq', 'unique (ip_range)', "IP range already exists")
    ]

    net_id = fields.Many2one('ni.networks')
    ip_range = fields.Char(string="Network IP Range", required=True)
    notes = fields.Char(string="Network IP Range Notes")
