#usr/bin/env python
#takes SATQuestions and creates instances of class Sat_Q_Processed(models.Model), storing them in the database
from mchlrn.models import Sat_Q_Processed as sqp
from mchlrn.models import SATQuestion as sq

sqlist = sq.objects.all()

def countNums(a): #counts the number of numbers in the string inside of a
    g = lambda x: x in '1234567890'
    counter = 0
    newchar = 1 #not just a continuation of old number
    for c in a:
        if (newchar):
            if (g(c)):
                counter += 1
                newchar = 0
        else:
            if (c == ' '):
                newchar = 1
    return counter

for s in sqlist:
    if (len(sqp.objects.filter(orig_q = s)) == 0): #check if it's already in the database
        print s
        numnums = countNums(s.question)
        length_question = len(s.question)
        p = sqp.objects.create(orig_q = s, num_numbers = numnums, col_num = -1, length=length_question)

