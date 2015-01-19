# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
import otree.models
from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>


doc = """
A simple 1-player game demonstrating some of oTree’s basic capabilities,
as well as its interaction with some plugins.
"""

source_code = "https://github.com/oTree-org/oTree/tree/master/demo_game2"


bibliography = ()


links = {}


keywords = ()



class Constants:
    players_per_group = 1
    name_in_url = 'demo_game2'
    number_of_rounds = 1

class Subsession(otree.models.BaseSubsession):

    pass


class Group(otree.models.BaseGroup):

    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


class Player(otree.models.BasePlayer):

    # <built-in>
    group = models.ForeignKey(Group, null=True)
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    demo_field1 = models.CharField(
        doc="""field With radiobutton input.""",
        widget=widgets.RadioSelect(),
    )

    def set_payoff(self):
        self.payoff = c(0)


    training_question_1 = models.CharField(widget=widgets.RadioSelect())
    training_question_2 = models.CharField(widget=widgets.RadioSelect())
    training_question_3 = models.CharField(widget=widgets.RadioSelect())

    def training_question_1_choices(self):
        return ['Head', 'Tail']

    def training_question_2_choices(self):
        return ['Head', 'Tail']

    def training_question_3_choices(self):
        return ['Head', 'Tail']



