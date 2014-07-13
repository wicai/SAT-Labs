from django.db import models


#use get_image_path to get images
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)



#Models defined here:
#USER DATA DEFINED HERE
class User(models.Model):
    col_num = models.IntegerField()
    username = models.charField(models.Model)
    
    
class Answered_Math_Q(models.Model):
    unanswered_q = models.OneToOneField(Math_Q)
    user = models.ForeignKey(User)
    correct = models.IntegerField() # 0 is wrong, 1 is correct

#NEURAL NETWORKS DEFINED HERE

#one layer theta for neural network for math
class Math_Theta(models.Model):

class Math_Theta_Row(models.Model):
    row = models.IntegerField()
    matrix = models.ForeignKey(Math_Theta_1)

class Math_Theta_Item(models.Model):
    row = models.ForeignKey(Math_Theta_1_row)
    col = models.IntegerField()
    val = models.FloatField()

#PROCESSED QUESTIONS:
class Math_Q_Processed(models.Model):
    orig_q = models.OneToOneField(Math_Q)
    col_num = models.IntegerField()
    length = models.IntegerField()
    num_numbers = models.IntegerField()

#RAW QUESTIONS:
class Math_Q(models.Model): #A math question.  If it has a diagram, can be found in Math_Diagram, uses instance of Math_Q as foreign key
    question = models.CharField(max_length = 600)
    diagram_exists = models.BooleanField();
    student_produced = models.BooleanField(); #these are the math problems that use grids
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)

class Math_Diagram(models.Model): #the diagram of a math question
    question = models.ForeignKey(Math_Q)
    diagram = ImageField(upload_to = get_image_path, blank = TRUE, null = TRUE) #http://stackoverflow.com/questions/8189800/django-store-user-image-in-model

class Math_A(models.Model):
    q = models.ForeignKey(Math_Q)
    answer = models.IntegerField() #1 = A, 2 = B, 3 = C, 4 = D
    
class Math_SP_A(models.Model): #for student produced questions
    q = models.ForeignKey(Math_Q)
    answer = models.FloatField()

class Reading_Passage(models.Model): #a passage
    passage = models.CharField(max_length = 10000)
    
class Reading_Passage_Q(models.Model): #questions attached to a passage
    question = models.CharField(max_length = 600)
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)
    passage = models.ForeignKey(Reading_Passage)

class Reading_Passage_A(models.Model):
    q = models.ForeignKey(Reading_Passage_Q)
    answer = models.IntegerField() 

class Reading_Q(models.Model): #fill in the blank, vocab
    question = models.CharField(max_length = 600)
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)

class Reading_A(models.Model):
    q = models.ForeignKey(Reading_Q)
    answer = models.IntegerField() 

class Writing_Passage(models.Model): #a passage for a bunch of writing questions
    passage = models.CharField(max_length = 10000)
    
class Writing_Passage_Q(models.Model): #questions attached to a passage
    question = models.CharField(max_length = 600)
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)
    passage = models.ForeignKey(Writing_Passage)

class Writing_Passage_A(models.Model):
    q = models.ForeignKey(Writing_Passage_Q)
    answer = models.IntegerField() 

class Writing_Effective_Q(models.Model): #these "test correctness and effectiveness of expression."
    question = models.CharField(max_length = 600)
    underline_start = models.IntegerField()
    underline_end = models.IntegerField()
    a = models.CharField(max_length = 100)
    b = models.CharField(max_length = 100)
    c = models.CharField(max_length = 100)
    d = models.CharField(max_length = 100)

class Writing_Effective_A(models.Model): 
    q = models.ForeignKey(Writing_Effective_Q)
    answer = models.IntegerField()

class Writing_Grammar_Q(models.Model): #these "test your ability to recognize grammar and usage errors."
    question = models.CharField(max_length = 600)
    a_underline_start = models.IntegerField()
    a_underline_end = models.IntegerField()
    b_underline_start = models.IntegerField()
    b_underline_end = models.IntegerField()
    c_underline_start = models.IntegerField()
    c_underline_end = models.IntegerField()
    d_underline_start = models.IntegerField()
    d_underline_end = models.IntegerField()
    e_underline_start = models.IntegerField()
    e_underline_end = models.IntegerField()

class Writing_Grammar_A(models.Model):
    q = models.ForeignKey(Writing_Grammar_Q)
    answer = models.IntegerField()
