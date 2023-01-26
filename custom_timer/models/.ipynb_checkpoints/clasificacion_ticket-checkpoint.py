# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class ClasificacionTicket(models.Model):
    _name = 'clasificacion.ticket'
    _description = 'Clasificación de los tickets'

    name = fields.Char(string='Alias')
    alias = fields.Many2one(string="Alias", comodel_name="res.alias")
    ticket_ids = fields.One2many(string='Clasificación', comodel_name='helpdesk.ticket',
                                 inverse_name='clasificacion_ticket')
    subclasificacion_ids = fields.One2many(string="Subclasificacion", comodel_name="subclasificacion.ticket",
                                           inverse_name="clasificacion_id")