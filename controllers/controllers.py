import random

from odoo import http


class TestModule(http.Controller):
    @http.route('/test_module/belarusbank/', auth='user')
    def index(self, **kw):
        data = ""
        employee_ids = http.request.env['hr.employee'].sudo().search([])
        for e in employee_ids:
                data += str(e.iban) + "      " + str(random.randrange(100, 5000)) + "  " + str(e.name) + "\n"
        res = http.Response()
        res.headers['Content-Disposition'] = 'attachment; filename=belarusbank.txt'
        res.set_data(data)
        return res