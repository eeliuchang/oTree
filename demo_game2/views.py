# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


def variables_for_all_templates(self):
    return {
        'total_q': 3,  # total number of questions to help participants understand study
    }


class Introduction(Page):

    template_name = 'demo_game2/Introduction.html'


class Question1(Page):
    template_name = 'demo_game2/Question.html'

    def participate_condition(self):
        return True

    form_model = models.Player
    form_fields = ['training_question_1']

    def variables_for_template(self):
        return {'num_q': 1}

class Question2(Page):
    template_name = 'demo_game2/Question.html'

    def participate_condition(self):
        return True

    form_model = models.Player
    form_fields = ['training_question_2']

    def variables_for_template(self):
        return {'num_q': 2,
                'answer1': self.player.training_question_1,
                }

class Question3(Page):
    template_name = 'demo_game2/Question.html'

    def participate_condition(self):
        return True

    form_model = models.Player
    form_fields = ['training_question_3']

    def variables_for_template(self):
        return {'num_q': 3,
                'answer1': self.player.training_question_1,
                'answer2': self.player.training_question_2,
                }

class Results(Page):

    def variables_for_template(self):
        return {'answer1': self.player.training_question_1,
                'answer2': self.player.training_question_2,
                'answer3': self.player.training_question_3,
                }

    template_name = 'demo_game2/Results.html'


class Finish(Page):

    template_name = 'demo_game2/Finish.html'


def pages():
    return [
        Introduction,
        Question1,
        Question2,
        Question3,
        Results,
        Finish,
    ]