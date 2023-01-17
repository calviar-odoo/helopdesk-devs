# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class ClasificacionTicket(models.Model):
    _name = 'clasificacion.ticket'
    _description = 'Clasificación de los tickets'

    name = fields.Char(string='Categoria')
    alias = fields.Many2one(string="Alias", comodel_name="res.alias")
    ticket_ids = fields.One2many(string='Clasificación', comodel_name='helpdesk.ticket',
                                 inverse_name='clasificacion_ticket')
    contar = fields.Float("MeasureCuentaClasifc", compute='_calculate_percentage', compute_sudo=True, store=True)
    subclasificacion_ids = fields.One2many(string="Sub-Categoria", comodel_name="subclasificacion.ticket",
                                           inverse_name="clasificacion_id")

    @api.model
    def _calculate_percentage(self):
        for record in self:
            contar = self.env['helpdesk.ticket'].search_count(['clasificacion_ticket', '=', 1])
            record.contar = contar
