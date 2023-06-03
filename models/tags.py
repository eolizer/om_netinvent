from odoo import models, fields, api, _
from random import randint


class NITags(models.Model):
    _name = 'ni.settings.tags'
    _description = 'Tags'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color", default=_get_default_color)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists")
    ]
