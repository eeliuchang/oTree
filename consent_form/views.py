# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    form_model = models.Player
   ## form_fields = ['my_field']
    form_fields = ['accept']
    def participate_condition(self):
        return True

    template_name = 'consent_form/Introduction.html'

    def variables_for_template(self):
        return {
            'my_variable_here': 1,
        }


def pages():
    return [
        Introduction
    ]
