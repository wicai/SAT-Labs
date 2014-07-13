import numpy as np
from project.map.models import Math_Q_Processed as MQP
from project.map.models import Math_Theta as MT
from project.map.models import Math_Theta_Row as MTR
from project.map.models import Math_Theta_Item as MTI
from project.map.models import User 
from project.map.models import Answered_Math_Q as AMQ

#given a model, returns all its fields
def get_model_fields(model):
    return model._meta.fields

#load the array from the databases

def train():
    problem_list = MQP.objects.all()
    npr = problem_list.count()  #dangerously close to np = numpy
    nx = len(get_model_fields(MQP)) + 1 #number of features we are checking w the matrix + 1 for bias
    user_list = User.objects.all()
    nu = u_list.count()
    # create matrices
    y = np.zero(npr * nu).reshape(npr, nu) - 1
    prob_feature = np.zero(nx * npr).reshape(nx, npr)
    theta = np.random.random((nx, nu))

    # load databases into matrices
    i = 0

    #prob_feature, npr x nx
    prob_feature[0,:] = 1 #bias term
    for p in problem_list:
        prob_feature[1, i] = p.length
        prob_feature[2, i] = p.num_num
        p.col_num = i
        i++

    #y, npr x  nu
    i = 0
    for u in user_list:
        u.col_num = i
        a_list = AMQ.objects.filter(user = u)
        for a in a_list:
            proc = MQP.objects.filter(orig_q = a.unanswered_q)
            y[proc.col_num, i] = a.correct
        i++
    
    #theta is already randomized and initialized
    #time to train theta
        

def cost(theta, y, prob_feature, nu, npr, nx, R, grad, lambda){
#TODO
# make grad inside cost and return it

#gives the cost of using theta as the params, given prob_features and y.
#theta is nx x nu
#prob_features is nx x npr
#y is npr x nu
#returns J, the cost, and grad, the gradient

#compute the prediction matrix, which is npr x nu (same as y) by taking theta tranpose times X
J = 1 / 2 * sum((R .* (np.tranpose(prob_feature)*(theta) - Y).^2)(:));}
