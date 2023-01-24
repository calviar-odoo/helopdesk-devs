# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class ResAlias(models.Model):
    _name = 'res.alias'
    _description = 'Clasificación de los tickets'

    name = fields.Char(string='Producto/Servicio')
    categoria_ids = fields.One2many(string="Categorias", comodel_name="clasificacion.ticket", inverse_name="alias")
