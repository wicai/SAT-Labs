from mchlrn.models import Sat_Q_Processed as sqp
from mchlrn.models import SATQuestion as sq

real_qs = sq.objects.filter(channel = "fake")
real_qs
for a in sqp.objects.all():
    real = 0
#filter(orig_q in real_qs): # is a processed unfake question
    for i in range(0, len(real_qs)): # for each real question
        if a.orig_q == real_qs[i]: #check if a correspond to it
            real = 1 # if it does it's real
    if (real == 0):
        a.delete() #delete the processed question (not the real one!)


