#!usr/bin/env python
from mchlrn.models import Sat_Q_Processed as SQP
from mchlrn.models import Answered_Sat_Q as ASQ
from mchlrn.models import SATQuestion as SQ

def set_avg():
    all_sqp = SQP.objects.all()
    all_asq = ASQ.objects.all()

    #for each SQP, go through ASQ which has it, sum asq.correct, divide by total number, put that in sqp.avg_score
    for one_sqp in all_sqp:
        total = 0.
        correct = 0.
        answered = ASQ.objects.filter(unanswered_q = one_sqp.orig_q)
        for a in answered:
            total += 1
            if (a.correct == 1):
                correct +=1
        if (total == 0):
            one_sqp.avg_score = .5
        else:
            one_sqp.avg_score = (correct/total)
        one_sqp.save()

set_avg()