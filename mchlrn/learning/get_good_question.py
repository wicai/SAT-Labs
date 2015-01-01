from mchlrn.models import UserData as USR
from mchlrn.models import Sat_Q_Processed as SQP
from mchlrn.models import Sat_Pred as SP
from mchlrn.models import Sat_Pred_Row as SPR
from mchlrn.models import Sat_Pred_Item as SPI
import numpy

def index_min(values):
    return min(xrange(len(values)),key=values.__getitem__)

def choose_q(a): #a is a usrdata
#get the usr col #
    col_num = a.col_num
#get the appropriate row of SAT_Pred, stick them in an array PRED
#get the array of probabilities from processed q's, put them in AVG
    pred = []
    avg = []
    all_rows = SPR.objects.all()
    for a_row in all_rows:
        pred_score = SPI.objects.filter(row = a_row, col = col_num)[0]
        pred.append(pred_score.val)
        avg_score = SQP.objects.filter(col_num = pred_score.row.row)[0].avg_score
        avg.append(avg_score)
#take the difference AVG-PRED
    diff = []
    for i in range(0, len(pred)):
        diff.append(pred[i] - avg[i])
    print diff
#find the highest difference where the user hasn't answered the question yet
    min_index = index_min(diff)
#return the question
        
    return SQP.objects.filter(col_num = all_rows[min_index].row)[0].orig_q
