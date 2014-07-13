def predict(Theta1, X):
#given trained weight Theta1, gives the predicted label of X 
    
#some useful values
    m = X.shape[0]
#append a column of ones to X
    np.append(np.ones((m,1)), X, axis = 1)
#multiply X * Theta
    y = 1/(1 + np.exp(-(np.dot(X, Theta1))))
    return y

