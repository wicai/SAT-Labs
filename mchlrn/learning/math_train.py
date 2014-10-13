#!/usr/bin/env python
#public libraries
import numpy as np
from scipy.optimize import fmin_bfgs
#learning library
import cost as cost_function
import theta_gradient as t_gradient
#models
from mchlrn.models import Math_Q_Processed as MQP
from mchlrn.models import Math_Theta as MT
from mchlrn.models import Math_Theta_Row as MTR
from mchlrn.models import Math_Theta_Item as MTI
from mchlrn.models import Math_Pred as MP
from mchlrn.models import Math_Pred_Row as MPR
from mchlrn.models import Math_Pred_Item as MPI
from mchlrn.models import User 
from mchlrn.models import Answered_Math_Q as AMQ

#given a model, returns all its fields
def get_model_fields(model):
    return model._meta.fields

#load the array from the databases
def train():    
    problem_list = MQP.objects.all()
    npr = problem_list.count()  #dangerously close to np = numpy
    nx = len(get_model_fields(MQP)) + 1 #number of features we are checking w the matrix + 1 for bias
    user_list = User.objects.all()
    nu = user_list.count()
    # create matrices
    r = np.zeros(npr * nu).reshape(npr, nu) #question answered is 1, not answered is 0
    y = np.zeros(npr * nu).reshape(npr, nu) - 1
    prob_feature = np.zeros(nx * npr).reshape(nx, npr)
    theta = np.random.random((nx, nu))

    # load databases into matrices
    i = 0

    #prob_feature, npr x nx
    prob_feature[0,:] = 1 #bias term
    for p in problem_list:
        prob_feature[1, i] = p.length
        prob_feature[2, i] = p.num_num
        p.col_num = i
        i+=1

    #y, npr x  nu
    i = 0
    for u in user_list:
        u.col_num = i
        a_list = AMQ.objects.filter(user = u)
        for a in a_list:
            proc = MQP.objects.filter(orig_q = a.unanswered_q)
            y[proc.col_num, i] = a.correct
            r[proc.col_num, i] = 1
            i+=1
    #normalize y
    mu = np.reshape(np.mean(y,1),(npr,1))
    y -= mu #mean normalizationizedered!


    #theta is already randomized and initialized
    #time to train theta
    lamb = .5
    theta_opt = fmin_bfgs(cost_function.cost, theta, fprime = t_gradient.gradient, args=(theta,y,prob_feature,nu,npr,nx,r,lamb))  #magically optimize theta 
    #store theta
    if (MT.objects.all().count() != 0): #gotta remove everything that's there
        for a in MT.objects.all():
            a.delete()
    mt = MT.objects.create() #create the new Math_Theta
    for i in range(0, nx): #for each row of theta
        theta_row = MTR.objects.create(row = i, matrix = mt) #create a Math_Theta_Row
        for ii in range(0, nu):
            col = MTI.objects.create(col = ii, val = theta[i,ii], row = theta_row)
            
    pred = np.tranpose(np.tranpose(theta) * X) + mu #user predictions
    #store pred
    if (MP.objects.all().count() != 0): #gotta remove everything that's there
        for a in MP.objects.all():
            a.delete()
    mp = MP.objects.create() #create the new Math_Pred
    for i in range(0, npr): #for each row of theta
        pred_row = MPR.objects.create(row = i, matrix = mp) #create a Math_Pred_Row
        for ii in range(0, nu):
            col = MPI.objects.create(col = ii, val = theta[i,ii], row = pred_row)

    
              





