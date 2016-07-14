# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Website(models.Model):
    _inherit = "website"

    no_index = fields.Boolean(
        string="Disallow the site to appear in search engines like Google and"
        " Bing.")


class WebsiteConfigSettings(models.TransientModel):

    """Settings Website"""

    _inherit = 'website.config.settings'

    no_index = fields.Boolean(
        related='website_id.no_index',
        string="Disallow the site to appear in search engines like Google "
        " and Bing.")
