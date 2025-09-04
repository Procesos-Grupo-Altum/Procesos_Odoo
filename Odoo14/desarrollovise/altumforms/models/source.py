# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Fuente(models.Model):
    _name = 'source'

    name = fields.Char(string='Nombre', required=True)