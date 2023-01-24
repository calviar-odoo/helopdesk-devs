# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class SubClasificacionTicket(models.Model):
    _name = 'subclasificacion.ticket'
    _description = 'Clasificación de los tickets'

    name = fields.Char(string='Requerimiento')
    clasificacion_id = fields.Many2one(string="Categoria", comodel_name="clasificacion.ticket")
    solucion_ids = fields.One2many(string="Solucion", comodel_name="solucion", inverse_name="subclasificacion_id")

    
