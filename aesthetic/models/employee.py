from odoo import fields, models, api, _

class Aesthetic(models.Model):
    _name = 'aesthetic.employee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Module to register employees"
    _rec_name = 'employee_name'

    employee_name = fields.Char(string='Name', required=True)
    employee_ref = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                               default=lambda self: _('New'))
    employee_surname = fields.Char(string='Surname', required=True)
    employee_personal_id = fields.Char(string='Personal ID')
    employee_gender = fields.Selection([
            ('male', "Male"),
            ('female', "Female"),
        ], required = True, default = 'male')
    employee_age  = fields.Integer('Age')
    about_employee = fields.Text(string="About employee")
#    image = fields.Binary(string='Image')
    image = fields.Image(string='Upload image')
    manager_name_id = fields.Many2one(comodel_name = "res.partner", string="Manager")
    need_to_do = fields.Text(String="Need ToDo")
    employee_other_info = fields.Text(String="Need ToDo")

    @api.model
    def create(self, vals):
        if vals.get("employee_ref", _("New")) == _("New"):
            vals['employee_ref'] = self.env['ir.sequence'].next_by_code('aesthetic.employee') or _("New")
        res = super(Aesthetic, self).create(vals)
        return res

    def name_get(self):
        result = []
        for rec in self:
            print(rec.employee_name)
            name = rec.employee_surname + " " + rec.employee_name
            print(name)
            print("________________")
            result.append((rec.employee_name, name))
        return result

