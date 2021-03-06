#TODO: test
#public libraries
import numpy as np
import scipy.optimize as opt
#learning library
import datetime
from mchlrn.learning.cost import cost
from mchlrn.learning.theta_gradient import gradient
#models
from mchlrn.models import Sat_Q_Processed as SQP
from mchlrn.models import Sat_Theta as ST
from mchlrn.models import Sat_Theta_Row as STR
from mchlrn.models import Sat_Theta_Item as STI
from mchlrn.models import Sat_Pred as SP
from mchlrn.models import Sat_Pred_Row as SPR
from mchlrn.models import Sat_Pred_Item as SPI
from mchlrn.models import UserData as USR
from mchlrn.models import Answered_Sat_Q as ASQ

#given a model, returns all its fields
def get_model_fields(model):
    return model._meta.fields


def train(some_user):    
    start = datetime.datetime.now()
    print "1------------------1"
    print (datetime.datetime.now() - start)
    #load the array from the databases
    problem_list = SQP.objects.all()
    u_list = USR.objects.all()
    npr = len(problem_list)  #number of problems
    nx = len(get_model_fields(SQP)) - 4 + 1 #number of features we are considering  w the matrix + 1 for bias.
    #  -4 is for self, colnum, orig_q, avg_score
    nu = u_list.count() #num_users
    # create matrices
    r = np.zeros(npr * nu).reshape(npr, nu) #question answered is 1, not answered is 0
    y = np.zeros(npr * nu).reshape(npr, nu)
    prob_feature = np.zeros(nx * npr).reshape(nx, npr)
    theta = np.random.random((nx, nu))/10
    # the idea is that we want to train theta such that we minimize prob_featureT * theta - y * r
    # load databases into matrices
    #prob_feature, npr x nx
    i = 0
    prob_feature[0,:] = 1 #bias term
    for p in problem_list:
        prob_feature[1, i] = p.length
        prob_feature[2, i] = p.num_numbers
        p.col_num = i
        i+=1
        p.save()
    #y, npr x  nu, and r, same dimension
    uind = 0
    for u in u_list:
        u.col_num = uind
        u.save()
        a_list = ASQ.objects.filter(user = u)
        for a in a_list:
            proc = SQP.objects.filter(orig_q = a.unanswered_q) #find the processed question that corresponds to this one
            y[proc[0].col_num, uind] = a.correct
            r[proc[0].col_num, uind] = 1
        uind+=1
    print "2------------------2"
    print (datetime.datetime.now() - start)

    #normalize y
    mu = np.zeros(npr).reshape(npr,1)
    for i in range(0, y.shape[0]): #for each question
        num_zeros = 0.0
        num_ones = 0.0
        for ii in range(0, y.shape[1]): #for each user
            if (y[i][ii] == 1):
                num_ones += 1
            if (y[i][ii] == 0):
                num_zeros += 1
        if (num_zeros == 0 and num_ones == 0):
            mu[i][0] = 0.0
        else:
            mu[i][0] = num_ones/(num_zeros + num_ones)
        #change avg score to whatever is in mu
        cur_prob = SQP.objects.filter(col_num = i)[0]
        cur_prob.avg_score = mu[i][0]
        cur_prob.save()

    y -= mu * r

    #theta is already randomized and initialized
    #time to train theta
    #theta = fmin_bfgs(cost, theta, fprime=gradient, args=(theta,y,prob_feature,nu,npr,nx,r,.5))  #magically optimize theta  #TODO last term is lambda you should figure out how to not hardcode
    args = (y,prob_feature,nu,npr,nx,r,.5)
    print "3------------------3"
    print (datetime.datetime.now() - start)

    theta = opt.fmin_bfgs(cost, theta, args = args)
    print "4------------------4"
    print (datetime.datetime.now() - start)

    theta = theta.reshape(nx,nu)
    
    #store theta
    if (ST.objects.all().count() != 0): #gotta remove everything that's there
        for a in ST.objects.all():
            a.delete()
    st = ST.objects.create() #create the new Sat_Theta
    st.save()

    for i in range(0, nx): #for each row of theta
        theta_row = STR.objects.create(row = i, matrix = st) 
        theta_row.save()
        for ii in range(0, nu):
            col = STI.objects.create(col = ii, val = theta[i,ii], row = theta_row)
            col.save()
            
    pred = np.transpose(np.dot(np.transpose(theta),prob_feature)) 
    print "5------------------5"
    print (datetime.datetime.now() - start)

    if (SP.objects.all().count() != 0): #gotta remove everything that's there
        for a in SP.objects.all():
            a.delete()
    sp = SP.objects.create() #create the new SAT_Pred
    sp.save()
    print "6------------------6"
    print (datetime.datetime.now() - start)

    for i in range(0, npr): #for each problem
        pred_row = SPR.objects.create(row = i, matrix=sp) #create a SAT_PRED_ROW
        pred_row.save()
        #get the index of our current user
        user_data = USR.objects.get(user=some_user)
        u_index = user_data.col_num
        """for ii in range(0, nu):
            col = SPI.objects.create(col = ii, val = pred[i,ii], row = pred_row)
            col.save()
        """
        col = SPI.objects.create(col = u_index, val = pred[i,u_index], row = pred_row)
        col.save()
    print "7-----------------7"
    print (datetime.datetime.now() - start)
