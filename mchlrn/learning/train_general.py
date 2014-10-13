#TODO: test
#public libraries
import numpy as np
import scipy.optimize as opt
#learning library
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
from mchlrn.models import User as USR
from mchlrn.models import Answered_Sat_Q as ASQ

#from mchlrn.models import User as USR
from mchlrn.models import Answered_Math_Q as AMQ


#given a model, returns all its fields
def get_model_fields(model):
    return model._meta.fields

#load the array from the databases
def train():    
    problem_list = SQP.objects.all()
    u_list = USR.objects.all()
    npr = len(problem_list)  #dangerously close to np = numpy
    nx = len(get_model_fields(SQP)) -3 + 1 #number of features we are checking w the matrix + 1 for bias.  -3 is for self, colnum and orig_q
    nu = u_list.count()
    # create matrices
    r = np.zeros(npr * nu).reshape(npr, nu) #question answered is 1, not answered is 0
    y = np.zeros(npr * nu).reshape(npr, nu) - 1 #default value is -1
    prob_feature = np.zeros(nx * npr).reshape(nx, npr)
    theta = np.random.random((nx, nu))
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
            #len proc should always be 0 here
            y[proc[0].col_num, uind] = a.correct
            r[proc[0].col_num, uind] = 1
        uind+=1

    #test that r is correct
    print("r is:")
    print(r)
    print("y is:")
    print(y)

    #normalize y
    mu = np.reshape(np.mean(y*r,1),(npr,1))
    y -= mu #mean normalizationizedered!

    #theta is already randomized and initialized
    #time to train theta
#    theta = fmin_bfgs(cost, theta, fprime=gradient, args=(theta,y,prob_feature,nu,npr,nx,r,.5))  #magically optimize theta  #TODO last term is lambda you should figure out how to not hardcode

    theta = opt.minimize(cost, theta, args = (theta,y,prob_feature,nu,npr,nx,r,.5), method = 'BFGS', jac = gradient)
    #store theta
    if (ST.objects.all().count() != 0): #gotta remove everything that's there
        for a in ST.objects.all():
            a.delete()
    st = ST.objects.create() #create the new Sat_Theta
    for i in range(0, nx): #for each row of theta
        theta_row = STR.objects.create(row = i, matrix = mt) #create a Math_Theta_Row
        for ii in range(0, nu):
            col = STI.objects.create(col = ii, val = theta[i,ii], row = theta_row)
            
    pred = np.tranpose(np.tranpose(theta) * X) + mu #user predictions
    #store pred
    if (SP.objects.all().count() != 0): #gotta remove everything that's there
        for a in SP.objects.all():
            a.delete()
    mp = SP.objects.create() #create the new Math_Pred
    for i in range(0, npr): #for each row of theta
        pred_row = SPR.objects.create(row = i, matrix = mp) #create a Math_Pred_Row
        for ii in range(0, nu):
            col = SPI.objects.create(col = ii, val = theta[i,ii], row = pred_row)

    
              





