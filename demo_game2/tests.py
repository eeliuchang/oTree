# -*- coding: utf-8 -*-
from __future__ import division

import random

from otree.common import Currency as c, currency_range

from ._builtin import Bot
from .models import Constants
from . import views


class PlayerBot(Bot):

    def play(self):

        self.submit(views.Introduction)

        self.submit(views.Question1, {
            'training_question_1': 'Head',
        })


        self.submit(views.Question2, {
            'training_question_2': 'Tail',
        })


        self.submit(views.Question3, {
            'training_question_3': 'Head',
        })

        self.submit(views.Results)

        self.submit(views.Finish)

    def validate_play(self):
        pass
