#!/usr/bin/env python
from mchlrn.models import User as usr
from mchlrn.models import Answered_Sat_Q as asq
from mchlrn.models import SATQuestion as sq

for j in range(0,len(usr.objects.all())): #for each user
    for i in range(0,len(asq.objects.filter(user=usr.objects.all()[j]))): #for each answered question
    	answered = asq.objects.filter(user=usr.objects.all()[j])[i]
	channel = answered.unanswered_q.channel
	print channel
