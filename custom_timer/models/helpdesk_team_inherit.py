# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class HelpdeskTeamInherit(models.Model):
    _inherit = 'helpdesk.team'
 # Verificar el many2many para relacion con usuarios
    team_id = fields.Many2one(required=True)
