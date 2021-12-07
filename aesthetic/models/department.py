from odoo import fields, models, api, _

class AestheticDepartment(models.Model):
    _name = 'aesthetic.department'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'manager_name'

    department_name = fields.Char(string='Department Name', required=True)
    unic_department_name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                               default=lambda self: _('New'))
    about_department = fields.Text(string="About Department")
    manager_name = fields.Many2one(comodel_name = "aesthetic.employee", string="Manager", tracking=True)
    age  = fields.Integer(string='Manager Age', related='manager_name.employee_age', tracking=True)


    @api.model
    def create(self, vals):
        if vals.get("unic_department_name", _("New")) == _("New"):
            vals['unic_department_name'] = self.env['ir.sequence'].next_by_code('aesthetic.department') or _("New")
        res = super(AestheticDepartment, self).create(vals)
        return res



