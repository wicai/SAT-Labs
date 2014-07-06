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
    #Our matrix X, the training example is n x nf
    x = loadx()
    nf = x.shape(1)
    
    users = loady();
    theta = loadtheta(nf)

def loady():
    #n by nu
    list = User.objects.all()
    nu = list.count()
    

def loadx():
    list = MQP.objects.all()
    n = list.count() 
    nf = len(get_model_fields(MQP)) #number of features we are checking w the matrix
    X = arrange(n * nu).reshape(n, nf)
    return X


def loadtheta(nf):
    
    Theta = arrange(nf * nu)
