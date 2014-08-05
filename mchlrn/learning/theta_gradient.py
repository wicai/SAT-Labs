import numpy as np

def gradient(self, theta,y,prob_feature,nu,npr,nx,R,lamb):
    np.transpose(prob_feature)*theta
    theta_grad = np.tranpose(np.tranpose(np.multiply(R, (np.dot(np.tranpose(prob_feature),theta) - Y ))) * np.tranpose(prob_feature))
#that may or may not be correct lol
#add regularization
    theta_grad += lamb * theta
    return theta_grad
