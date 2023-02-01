# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class HelpdeskTicketReportAnalysisInherit(models.Model):
    _inherit = 'helpdesk.ticket.report.analysis'

    canal_type = fields.Many2one('res.canales', string='Canal', readonly=True)
    canal_typesito = fields.Char(string='Canal', readonly=True)
    alias_ticket = fields.Many2one('res.alias', string='Alias', index=True)
    clasificacion_ticket = fields.Many2one('clasificacion.ticket', string='Categoria', index=True)
    subclasificacion_ticket = fields.Many2one('subclasificacion.ticket', string='Sub-Categoria', index=True)
    tiempo_progress = fields.Float(string='T. Nuevo a Progreso')
    tiempo_completado = fields.Float(string='T. en Completarse')
    tiempo_anulado = fields.Float(string='T. en ser Anulado')

    def _select(self):
        select_str = """
            SELECT T.id AS id,
                   T.id AS ticket_id,
                   T.create_date AS create_date,
                   T.priority AS priority,
                   T.canal_type AS canal_type,
                   T.alias_ticket AS alias_ticket,
                   T.clasificacion_ticket AS clasificacion_ticket,
                   T.subclasificacion_ticket AS subclasificacion_ticket,
                   T.tiempo_progress AS tiempo_progress,
                   T.tiempo_completado AS tiempo_completado,
                   T.tiempo_anulado AS tiempo_anulado,
                   T.user_id AS user_id,
                   T.partner_id AS partner_id,
                   T.ticket_type_id AS ticket_type_id,
                   T.stage_id AS ticket_stage_id,
                   T.sla_deadline AS ticket_deadline,
                   NULLIF(T.close_hours, 0) AS ticket_close_hours,
                   EXTRACT(HOUR FROM (COALESCE(T.assign_date, NOW()) - T.create_date)) AS ticket_open_hours,
                   NULLIF(T.assign_hours, 0) AS ticket_assignation_hours,
                   T.close_date AS close_date,
                   T.assign_date AS assign_date,
                   NULLIF(T.rating_last_value, 0) AS rating_last_value,
                   T.active AS active,
                   T.team_id AS team_id,
                   T.company_id AS company_id,
                   T.kanban_state AS kanban_state
        """
        return select_str

    def _from(self):
        from_str = """
            helpdesk_ticket T
        """
        return from_str
