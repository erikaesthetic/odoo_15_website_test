from odoo import http

from odoo.http import request

class Aesthetic_employees(http.Controller):
    @http.route('/employee', website=True, auth='public')
    def aesthetic_employee(self, **kw):
        return "My name is Erik"
