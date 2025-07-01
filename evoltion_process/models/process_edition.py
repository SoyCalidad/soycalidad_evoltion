from odoo import api, fields, models, _


class ProcessEditionResponsible(models.Model):
    _inherit = "process.edition.responsible"

    job_id = fields.Many2one(
        comodel_name="hr.job",
        string="Puesto",
    )
