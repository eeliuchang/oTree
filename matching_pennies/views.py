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


class Introduction(Page):

    template_name = 'matching_pennies/Introduction.html'
    def participate_condition(self):
        return self.subsession.round_number == 1



class Choice(Page):

    template_name = 'matching_pennies/Choice.html'

    form_model = models.Player
    form_fields = ['penny_side']
    def variables_for_template(self):
        me_in_previous_rounds = self.player.me_in_previous_rounds()
        return {'me_in_previous_rounds': me_in_previous_rounds,
              }

class Results(Page):

    template_name = 'matching_pennies/Results.html'

    def participate_condition(self):
        return self.subsession.round_number == Constants.number_of_rounds

    def variables_for_template(self):
        me_in_all_rounds = self.player.me_in_all_rounds()
        self.player.participant.vars['matching_pennies_results'] = [p.penny_side for p in self.player.me_in_all_rounds()]
        return {'me_in_all_rounds': me_in_all_rounds,
                'matching_pennies_results': self.player.participant.vars['matching_pennies_results']
              }




def pages():
    return [
        Introduction,
        Choice,
        Results,
    ]


