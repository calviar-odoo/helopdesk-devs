from odoo import api, fields, models
import time

class Solucion(models.Model):
    _name = 'solucion'
    _description = 'Solucion para los tickets'

    name = fields.Char(string='Solucion')
    subclasificacion_id = fields.Many2one(string="Requerimiento", comodel_name="subclasificacion.ticket")
