from mchlrn.models import UserData
from mchlrn.models import Sat_Q_Processed as SQP
from mchlrn.models import Sat_Pred as SP
from mchlrn.models import Sat_Pred_Row as SPR
from mchlrn.models import Sat_Pred_Item as SPI
from mchlrn.models import Answered_Sat_Q as ASQ
from mchlrn.models import SATQuestion as SQ
from django.contrib.auth.models import User
import numpy

from mchlrn.learning import train_general

#given a list values, returns the index of the item with the least value
def index_min(values):
    return min(xrange(len(values)),key=values.__getitem__)

#called when asked to recommend a question for a user with col_num of -1(new user)

def choose_q(some_user): #a is a User
    train_general.train(some_user)
    print "training done"
    some_user_data = UserData.objects.get(user=some_user)    
    #get the usr col #
    col_num = some_user_data.col_num
    #get the appropriate row of SAT_Pred, stick them in an array PRED
    #get the array of probabilities from processed q's, put them in AVG
    pred = []
    avg = []
    all_rows = SPR.objects.all()
    print SPI.objects.all()
    for a_row in all_rows:
        pred_score = SPI.objects.get(row = a_row, col = col_num)
        pred.append(pred_score.val)
        avg_score = SQP.objects.filter(col_num = pred_score.row.row)[0].avg_score
        avg.append(avg_score)
        #take the difference AVG-PRED
    diff = []
    for i in range(0, len(pred)):
        #check if there's an answered SAT question with this user and question
        #user=some_user_data
        #question is the ith processed question
        aa = ASQ.objects.filter(user=some_user_data,unanswered_q=SQP.objects.all()[i].orig_q)
        if len(aa) > 0:#user already answered that question
            diff.append(10)
        else:
            diff.append(pred[i] - avg[i])
    print diff
    #find the highest difference where the user hasn't answered the question yet
    min_index = index_min(diff)
    #return the question
        
    return SQP.objects.filter(col_num = all_rows[min_index].row)[0].orig_q
