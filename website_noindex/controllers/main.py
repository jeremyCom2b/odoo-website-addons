# -*- coding: utf-8 -*-
from openerp.addons.web import http
from openerp.http import request


class Website(http.Controller):

    @http.route(['/website/index_noindex'], type='json', auth="public", website=True)
    def index_noindex(self, index):

        if index == 'index':
            request.website.write({
                'no_index': False
            })
        else:
            request.website.write({
                'no_index': True
            })

        return True
