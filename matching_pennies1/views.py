# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


def variables_for_all_templates(self):
    return {
        'total_q': 3,  # total number of questions to help participants understand study
        'total_rounds': Constants.number_of_rounds,
        'round_number': self.subsession.round_number,
    }


class Introduction1(Page):

    template_name = 'matching_pennies1/Introduction1.html'
    def participate_condition(self):
        return self.subsession.round_number == 1

class ResultsWaitPage1(WaitPage):


    def body_text(self):
        return "Waiting for your opponent."

    def participate_condition(self):
        return self.subsession.round_number == 1


class Choice1(Page):

    template_name = 'matching_pennies1/Choice1.html'

    form_model = models.Player
    form_fields = ['penny_side']
    def variables_for_template(self):
        me_in_previous_rounds = self.player.me_in_previous_rounds()
        other_results = self.player.other_player().participant.vars['matching_pennies_results']
        return {'me_in_previous_rounds': me_in_previous_rounds,
                'other_results_in_order': other_results[0:self.subsession.round_number-1],
              }

class Results1(Page):

    template_name = 'matching_pennies1/Results1.html'

    def participate_condition(self):
        return self.subsession.round_number == Constants.number_of_rounds

    def variables_for_template(self):
        me_in_all_rounds = self.player.me_in_all_rounds()
        return {'me_in_all_rounds': me_in_all_rounds,
              }




def pages():
    return [
        Introduction1,
        ResultsWaitPage1,
        Choice1,
        Results1,
    ]

