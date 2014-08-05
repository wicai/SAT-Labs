#!usr/bin/env python

#removes all the quesitons with channel = 'fake'

from mchlrn.models import SATQuestion as sq

toberemoved = sq.objects.filter(channel = 'fake').delete()
