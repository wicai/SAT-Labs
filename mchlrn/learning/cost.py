#!usr/bin/env python
import numpy as np

def cost(self, theta, y, prob_feature, nu, npr, nx, R, lamb):
#gives the cost of using theta as the params, given prob_features and y.
#theta is nx x nu
#prob_features is nx x npr
#X is  npr x nx
#y is npr x nu
#returns J, the cost, and grad, the gradient
#compute J   
    J = (.5) * np.sum(np.power(np.multiply(R, ((np.dot(np.transpose(prob_feature),(theta))) - y)),2))
    print('J is')
    print(J)
#add regularization     
    J += lamb/2 * np.sum(np.power(theta,2))
#    J += lamb/2 * np.sum(np.dot(np.transpose(theta),theta)) #lol is that right
    print('J is')
    print(J)

    return J
                         
