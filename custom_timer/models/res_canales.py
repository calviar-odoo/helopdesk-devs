# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class ResCanales(models.Model):
    _name = 'res.canales'
    _description = 'Tipos de Canales por los que pasan los tickets'

    name = fields.Char(string='Canal')
    canal_type_ids = fields.One2many(string='Ticket del Canal', comodel_name='helpdesk.ticket',
                                           inverse_name='canal_type')