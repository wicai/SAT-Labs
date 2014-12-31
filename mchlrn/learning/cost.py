#!usr/bin/env python
import numpy as np

#gives the cost of using theta as the params, given prob_features and y.
#theta is nx x nu
#prob_features is nx x npr
#X is  npr x nx
#y is npr x nu
#returns J, the cost


def cost(theta, *args):
    #print("START COST -------- -------- -------- -------- -------- -------- -------- -------- -------- --------")
    #for i in range(0, len(args)):
    #    print i
    #    print args[i]
    #    print ""
    #unwrap arguments
    y, prob_feature, nu, npr, nx, R, lamb = args
    #unroll theta
    theta = np.reshape(theta, (nx,-1))
    J = (.5) * np.sum(  np.power(  np.multiply(R, np.dot(np.transpose(prob_feature),(theta)) - y)   ,2   )  )
    #print('J is')
    #print(J)
    #add regularization     
    J += lamb/2 * np.sum(np.power(theta,2))
    #print('J w/reg is')
    #print(J)

    return J
                         
