import numpy as np

def gradient(self, theta,y,prob_feature,nu,npr,nx,R,lamb):
    print('theta is')
    print(theta.shape)
    print(theta)
    print('y is')
    print(y.shape)
    print(y)
    print('prob_feature is')
    print(prob_feature.shape)
    print(prob_feature)
    print('nu is')
    print(nu)
    print('npr is')
    print(npr)
    print('nx is')    
    print(nx)
    print('R is')
    print(R.shape)
    print(R)
    print('lamb is')
    print(lamb)
    print('prob_feature is')
    print(prob_feature.shape)
    print(prob_feature)
    #                                      15x7         7x15                       7x3                      3x15
    theta_grad = np.transpose((np.dot(np.transpose(np.multiply(R, (np.dot(np.transpose(prob_feature),theta) - y))),np.transpose(prob_feature))))
    print('theta_grad is')
    print(theta_grad.shape)
    print(theta_grad)
#that may or may not be correct lol
#add regularization
    theta_grad += lamb * theta
    print('theta_grad is now')
    print(theta_grad.shape)
    print(theta_grad)

    return theta_grad.flatten()

