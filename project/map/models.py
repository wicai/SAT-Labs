from django.db import models
import os

#use get_image_path to get images
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

#Models defined here:
class Math_Q(models.Model): #A math question.  If it has a diagram, can be found in Math_Diagram, uses instance of Math_Q as foreign key
    question = models.CharField(max_length = 600)
    diagram_exists = models.BooleanField();
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)

class Math_Diagram(models.Model): #the diagram of a math question
    question = models.ForeignKey(Math_Q)
    diagram = ImageField(upload_to = get_image_path, blank = TRUE, null = TRUE)

class Reading_Passage(models.Model): #a passage
    passage = models.CharField(max_length = 10000)
    
class Reading_Passage_Q(models.Model): #questions attached to a passage
    question = models.CharField(max_length = 600)
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)
    passage = models.ForeignKey(Reading_Passage)

class Reading_Q(models.Model): #fill in the blank, vocab
    question = models.CharField(max_length = 600)
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)

class Writing_Passage

class mathp(models.Model):
    p_id = 
    text = models.charField(max_length = 600)
    diagram = ImageField(upload_to=get_image_path, blank=True, null=True) #http://stackoverflow.com/questions/8189800/django-store-user-image-in-model
    #when inserting the text of the problem, we should insert it, get its ID that django assigned to it, and then save the picture with that string
    

