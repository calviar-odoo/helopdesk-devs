# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class ResAlias(models.Model):
    _name = 'res.alias'
    _description = 'Clasificación de los tickets'

    name = fields.Char(string='Ente/Operadora')
    categoria_ids = fields.One2many(string="Servicio", comodel_name="clasificacion.ticket", inverse_name="alias")
