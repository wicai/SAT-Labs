from django.db import models

#use get_image_path to get images
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

#Models defined here:
ANSWERS = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('U', 'No Answer'),          
)

CATEGORIES = (
    ('Math', 'Math'),
    ('Reading', 'Reading'),
    ('Writing', 'Writing'),        
)

class SATQuestion(models.Model):
#template: sq.objects.create(name = '', question = '', answer_A = '', answer_B = '', answer_C = '', answer_D = '', answer_E = '', correct_answer = '', explanation = '', instructions = '', channel = '', channel_url = '', difficulty = '', css = '')
    name = models.CharField(max_length=128)

    question = models.CharField(max_length=1024)

    #Note: blank answers are used when only selecting A, B, etc. is necessary
    #In some cases (i.e. collegeboard's SAT question of the day, this appears in the data as &nbsp)
    answer_A = models.CharField(max_length=256, blank=True, null=True)
    answer_B = models.CharField(max_length=256, blank=True, null=True)
    answer_C = models.CharField(max_length=256, blank=True, null=True)
    answer_D = models.CharField(max_length=256, blank=True, null=True)
    answer_E = models.CharField(max_length=256, blank=True, null=True)

    #A - E
    correct_answer = models.CharField(max_length=1, choices=ANSWERS)
    explanation = models.CharField(max_length=2048, null=True, blank=True)
    instructions = models.CharField(max_length=512, null=True, blank=True)
    channel = models.CharField(max_length=128)
    channel_url = models.CharField(max_length=128, null=True, blank=True)
    difficulty = models.IntegerField(null=True, blank=True)
    css = models.CharField(null=True, blank=True, max_length=128)
    
    #Math, Reading, Writing
    category = models.CharField(max_length=16, null=True, blank=True, choices=CATEGORIES)
    #Improving sentences, passage-based reading, etc.
    sub_category = models.CharField(max_length=64, null=True, blank=True)

    def __unicode__(self):
        return self.name

#USER DATA DEFINED HERE
class User(models.Model):
    col_num = models.IntegerField()
    username = models.CharField(max_length=256)
    
class Answered_Math_Q(models.Model):
    unanswered_q = models.OneToOneField('Math_Q')
    user = models.ForeignKey(User)
    correct = models.IntegerField() # 0 is wrong, 1 is correct

class Answered_Sat_Q(models.Model):
    unanswered_q = models.ForeignKey('SATQuestion')
    user = models.ForeignKey(User)
    correct = models.IntegerField()
#NEURAL NETWORKS DEFINED HERE

#one layer theta for neural network for Jeff's spiffy new SAT question
class Sat_Pred(models.Model):
    #placeholder (i have no idea what this is)
    a = 5

class Sat_Pred_Row(models.Model):
    row = models.IntegerField()
    matrix = models.ForeignKey(Sat_Pred)

class Sat_Pred_Item(models.Model):
    row = models.ForeignKey(Sat_Pred_Row)
    col = models.IntegerField()
    val = models.FloatField()

class Sat_Theta(models.Model):
    #placeholder
    a = 5

class Sat_Theta_Row(models.Model):
    row = models.IntegerField()
    matrix = models.ForeignKey(Sat_Theta)

class Sat_Theta_Item(models.Model):
    row = models.ForeignKey(Sat_Theta_Row)
    col = models.IntegerField()
    val = models.FloatField()

#PROCESSED QUESTIONS:
class Sat_Q_Processed(models.Model):
    orig_q = models.OneToOneField('SATQuestion')
    col_num = models.IntegerField()
    length = models.IntegerField()
    num_numbers = models.IntegerField()
    avg_score = models.FloatField()

#one layer theta for neural network for math
class Math_Pred(models.Model):
    #placeholder
    a = 5

class Math_Pred_Row(models.Model):
    row = models.IntegerField()
    matrix = models.ForeignKey(Math_Pred)

class Math_Pred_Item(models.Model):
    row = models.ForeignKey(Math_Pred_Row)
    col = models.IntegerField()
    val = models.FloatField()

class Math_Theta(models.Model):
    #placeholder
    a = 5

class Math_Theta_Row(models.Model):
    row = models.IntegerField()
    matrix = models.ForeignKey(Math_Theta)

class Math_Theta_Item(models.Model):
    row = models.ForeignKey(Math_Theta_Row)
    col = models.IntegerField()
    val = models.FloatField()

#PROCESSED QUESTIONS:
class Math_Q_Processed(models.Model):
    orig_q = models.OneToOneField('Math_Q')
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
    diagram = models.ImageField(upload_to = get_image_path, blank=True, null=True) #http://stackoverflow.com/questions/8189800/django-store-user-image-in-model

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
