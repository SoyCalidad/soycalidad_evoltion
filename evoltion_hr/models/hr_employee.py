from odoo import fields, models


class HREmployee(models.Model):
    _inherit = "hr.employee"

    supervisor_ids = fields.Many2many(
        comodel_name="hr.employee",
        relation="hr_employee_supervisor_rel",   
        column1="employee_id",                  
        column2="supervisor_id",                
        string="Supervisor(es)",
    )
