# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
import otree.models
from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>

from django_countries.fields import CountryField



class Constants:
    name_in_url = 'consent_form'
    players_per_group = 1
    number_of_rounds = 1

    # define more constants here


class Subsession(otree.models.BaseSubsession):
    pass


class Group(otree.models.BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>


class Player(otree.models.BasePlayer):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    group = models.ForeignKey(Group, null = True)
    # </built-in>

    accept = models.NullBooleanField(widget=widgets.RadioSelect())
    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

