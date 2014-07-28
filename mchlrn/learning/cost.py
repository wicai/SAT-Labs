#!usr/bin/env python
import numpy as np

def cost(theta, y, prob_feature, nu, npr, nx, R, lamb):
#gives the cost of using theta as the params, given prob_features and y.
#theta is nx x nu
#prob_features is nx x npr
#X is  npr x nx
#y is npr x nu
#returns J, the cost, and grad, the gradient
#compute J
    J = 1 / 2 * np.sum(np.power(np.multiply(R, ((np.dot(np.tranpose(prob_feature)*(theta))+mu) - Y)),2))
#add regularization                       
    J += lamb/2 * np.sum(np.power(theta,2))
    return J
                         
