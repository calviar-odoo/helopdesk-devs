# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class TicketCustomTimer(models.Model):
    _inherit = 'helpdesk.ticket'

    team_id = fields.Many2one(required=True)
    user_id = fields.Many2one('res.users', string='Asignado a', default=lambda self: self._get_user()) #required=True
    #helpdesk_team_id = fields.Many2one('res.users', string='Asignado', default=lambda self: self._get_user(), required=True)
    canal_type = fields.Many2one('res.canales', string='Canal', index=True)
    alias_ticket = fields.Many2one('res.alias', string='Alias', index=True)
    clasificacion_ticket = fields.Many2one('clasificacion.ticket', string='Clasificacion', index=True)
    subclasificacion_ticket = fields.Many2one('subclasificacion.ticket', string='subclasificacion', index=True)
    #solucion = fields.Many2one('solucion', string='Solucion', index=True)


    team_timer = fields.Float(string='Team Timer')
    user_timer = fields.Float(string='User Timer')
    start = fields.Float(string='Start')

    progress = fields.Float(string='Progress')
    prueba = fields.Integer(string='Progress', default=5)
    tiempo_progress = fields.Float(string='T. Nuevo a Progreso', store=True)
    tiempo_completado = fields.Float(string='T. en Completarse', store=True)
    tiempo_anulado = fields.Float(string='T. en ser Anulado', store=True)

    # Auxiliary Variables
    responsible = []

    @api.onchange('team_id', 'user_id')
    def team_and_user_counter(self):
        length = len(self.responsible)
        if length is not 0:
            if (self.team_id.id is self.responsible[length-1]['grupo']) and \
                    (self.user_id.id is self.responsible[length-1]['usuario']):
                print('There was no change in the register')

            elif (self.team_id.id is not self.responsible[length-1]['grupo']) and \
                    (self.user_id.id is self.responsible[length-1]['usuario']):
                print('There was a diff group in the register')
                time_diff = time.time() - self.team_timer
                self.responsible[length - 1]['team_duration'] = time_diff
                self.responsible.append({"grupo": self.team_id.id,
                                         "usuario": self.responsible[length-1]['usuario'],
                                         "number_team": length+1,
                                         "number_user": self.responsible[length-1]['number_user'],
                                         "team_duration": 0.00,
                                         "user_duration": 0.00})
                print(self.responsible)

            elif (self.team_id.id is self.responsible[length-1]['grupo']) and \
                    (self.user_id.id is not self.responsible[length-1]['usuario']):
                print('There was a diff user in the register')
                time_diff = time.time() - self.user_timer
                self.responsible[length - 1]['user_duration'] = time_diff
                self.responsible.append({"grupo": self.responsible[length-1]['grupo'],
                                         "usuario": self.user_id.id,
                                         "number_team": self.responsible[length-1]['number_team'],
                                         "number_user": length+1,
                                         "team_duration": 0.00,
                                         "user_duration": 0.00})
                print(self.responsible)

            elif (self.team_id.id is not self.responsible[length-1]['grupo']) and \
                    (self.user_id.id is not self.responsible[length-1]['usuario']):
                print('There is full change in the register')
                time_di = time.time() - self.team_timer
                time_diff = time.time() - self.user_timer
                self.responsible[length - 1]['team_duration'] = time_di
                self.responsible[length - 1]['user_duration'] = time_diff
                self.responsible.append({"grupo": self.team_id.id,
                                         "usuario": self.user_id.id,
                                         "number_team": length + 1,
                                         "number_user": length + 1,
                                         "team_duration": 0.00,
                                         "user_duration": 0.00})
                print(self.responsible)

    @api.onchange('team_id')
    def _get_user(self):
        for record in self:
            return {'domain': {'helpdesk_team_id': [('helpdesk_team_id', '=', record.team_id.id)]}}

    @api.onchange('alias_ticket')
    def _get_servicio(self):
        for record in self:
            return {'domain': {'clasificacion_ticket': [('alias', '=', record.alias_ticket.id)]}}        

    @api.onchange('clasificacion_ticket')
    def _get_alias(self):
        for record in self:
            return {'domain': {'subclasificacion_ticket': [('clasificacion_id', '=', record.clasificacion_ticket.id)]}}
    
    @api.onchange('subclasificacion_ticket')
    def _get_clasificacion(self):
        for record in self:
            return {'domain': {'solucion': [('subclasificacion_id', '=', record.subclasificacion_ticket.id)]}}

    @api.onchange("stage_id")
    def stoppingStage(self):
        for record in self:

            if record.stage_id.id == 2:
                record.progress = time.time()
                elapsed_time_progress = time.time() - record.start
                record.tiempo_progress = elapsed_time_progress
                print(record.tiempo_progress)

            if record.stage_id.id == 3:
                elapsed_time_completado = time.time() - record.progress
                record.tiempo_completado = elapsed_time_completado
                print(record.tiempo_completado)

            if record.stage_id.id == 4:
                elapsed_time_anulado = time.time() - record.progress
                record.tiempo_anulado = elapsed_time_anulado
                print(record.tiempo_anulado)

    @api.model
    def create(self, vals):
        vals['start'] = time.time()
        vals['progress'] = time.time()
        vals['team_timer'] = time.time()
        vals['user_timer'] = time.time()
        #self.responsible.append({"grupo": vals['team_id'],
        #                         "usuario": vals['user_id'],
        #                         "number_team": 1,
        #                         "number_user": 1,
        #                         "team_duration": 0.00,
        #                         "user_duration": 0.00})
        result = super(TicketCustomTimer, self).create(vals)
        return result