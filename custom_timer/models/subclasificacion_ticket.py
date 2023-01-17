# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class SubClasificacionTicket(models.Model):
    _name = 'subclasificacion.ticket'
    _description = 'Clasificación de los tickets'

    name = fields.Char(string='Sub-categoria')
    clasificacion_id = fields.Many2one(string="Categoria", comodel_name="clasificacion.ticket")
    contar = fields.Float("MeasureCuentaClasifc", compute='_calculate_percentage', compute_sudo=True, store=True)

    @api.model
    def _calculate_percentage(self):
        for record in self:
            contar = self.env['helpdesk.ticket'].search_count(['clasificacion_ticket', '=', 1])
            record.contar = contar
