def gradient(theta,y,prob_feature,nu,npr,nx,R,lamb):
    theta_grad = np.tranpose(np.tranpose(np.multiply(R, (np.dot(np.tranpose(prob_features)*theta) - Y ))) * np.tranpose(prob_feature))
#that may or may not be correct lol
#add regularization
    theta_grad += lamb * theta
    return theta_grad
