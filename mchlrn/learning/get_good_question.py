from mchlrn.models import User as USR
from mchlrn.models import Sat_Q_Processed as SQP
from mchlrn.models import Sat_Pred as SP
from mchlrn.models import Sat_Pred_Row as SPR
from mchlrn.models import Sat_Pred_Item as SPI

def choose_q(a): #a is a usr
#get the usr
#get the appropriate row of SAT_Pred, stick them in an array PRED
#get the array of probabilities from processed q's, put them in AVG
#take the difference AVG-PRED
#find the highest difference where the user hasn't answered the question yet
#return the question

