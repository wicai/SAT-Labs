from django.contrib.auth.models import User
from mchlrn.models import UserData as usr
from mchlrn.models import Answered_Sat_Q as asq
from mchlrn.models import SATQuestion as sq

'''
0:11, 63
1:2, 14
2:7, 54
3:34, 111
4:15, 43
5:0, 25
6:1, 31

A is for people who are handling the questions with lots of numbers and get all or some of them right, getting none of them wrong
B is for people who suck with lots of numbers, and get them all wrong
C is for people who haven't answered any questions
D is for people who answer one question - we want to see what the predictions are
'''
fake_sq_list = sq.objects.filter(channel = 'fake') #list of fake sat questions

#remove all users
usr_list = User.objects.all()
for i in range(0, len(usr_list)):
    usr_list[i].delete()

#remove all users and answered sat questions
usr_data_list = usr.objects.all()
for i in range(0, len(usr_data_list)):
    usr_data_list[i].delete()

afake_sq_list = asq.objects.all()
for i in range(0, len(afake_sq_list)):
    afake_sq_list[i].delete()

#A people
#make a user

#make the user data
ra1 = User.objects.create_user('ashley astonishing', email=None, password=None)
a1 = usr.objects.create(user=ra1, col_num = -1)
a1.save()
a11 = asq.objects.create(unanswered_q = fake_sq_list[0], user=a1, correct = 1)
a12 = asq.objects.create(unanswered_q = fake_sq_list[2], user=a1, correct = 1)
a13 = asq.objects.create(unanswered_q = fake_sq_list[3], user=a1, correct = 1)
a14 = asq.objects.create(unanswered_q = fake_sq_list[4], user=a1, correct = 1)
a15 = asq.objects.create(unanswered_q = fake_sq_list[5], user=a1, correct = 0)
a16 = asq.objects.create(unanswered_q = fake_sq_list[6], user=a1, correct = 0)
a11.save()
a12.save()
a13.save()
a14.save()
a15.save()
a16.save()

ra2 = User.objects.create_user('arthur the aardvark', email=None, password=None)
a2 = usr.objects.create(user=ra2, col_num = -1)
a2.save()
a21 = asq.objects.create(unanswered_q = fake_sq_list[0], user=a2, correct = 1)
a22 = asq.objects.create(unanswered_q = fake_sq_list[2], user=a2, correct = 1)
a23 = asq.objects.create(unanswered_q = fake_sq_list[3], user=a2, correct = 1)
a24 = asq.objects.create(unanswered_q = fake_sq_list[4], user=a2, correct = 1)
a25 = asq.objects.create(unanswered_q = fake_sq_list[5], user=a2, correct = 0)
a26 = asq.objects.create(unanswered_q = fake_sq_list[6], user=a2, correct = 1)
a21.save()
a22.save()
a23.save()
a24.save()
a25.save()
a26.save()

ra3 = User.objects.create_user('america', email=None, password=None)
a3 = usr.objects.create(user=ra3, col_num = -1)
a3.save()
a33 = asq.objects.create(unanswered_q = fake_sq_list[3], user=a3, correct = 1)
a34 = asq.objects.create(unanswered_q = fake_sq_list[4], user=a3, correct = 1)
a35 = asq.objects.create(unanswered_q = fake_sq_list[5], user=a3, correct = 0)
a36 = asq.objects.create(unanswered_q = fake_sq_list[6], user=a3, correct = 0)
a33.save()
a34.save()
a35.save()
a36.save()


#b people
rb1 = User.objects.create_user('bogdan bogdanovitch', email=None, password=None)
b1 = usr.objects.create(user=rb1, col_num = -1)
b1.save()
b11 = asq.objects.create(unanswered_q = fake_sq_list[0], user=b1, correct = 0)
b12 = asq.objects.create(unanswered_q = fake_sq_list[2], user=b1, correct = 0)
b13 = asq.objects.create(unanswered_q = fake_sq_list[3], user=b1, correct = 0)
b14 = asq.objects.create(unanswered_q = fake_sq_list[4], user=b1, correct = 0)
b11.save()
b12.save()
b13.save()
b14.save()

rb2 = User.objects.create_user('bob ma', email=None, password=None)
b2 = usr.objects.create(user=rb2, col_num = -1)
b2.save()
b21 = asq.objects.create(unanswered_q = fake_sq_list[0], user=b2, correct = 0)
b22 = asq.objects.create(unanswered_q = fake_sq_list[2], user=b2, correct = 0)
b23 = asq.objects.create(unanswered_q = fake_sq_list[3], user=b2, correct = 0)
b24 = asq.objects.create(unanswered_q = fake_sq_list[5], user=b2, correct = 1)
b21.save()
b22.save()
b23.save()
b24.save()

rb3 = User.objects.create_user('billy bam', email=None, password=None)
b3 = usr.objects.create(user=rb3, col_num = -1)
b3.save()
b31 = asq.objects.create(unanswered_q = fake_sq_list[0], user=b3, correct = 0)
b32 = asq.objects.create(unanswered_q = fake_sq_list[2], user=b3, correct = 0)
b33 = asq.objects.create(unanswered_q = fake_sq_list[3], user=b3, correct = 0)
b34 = asq.objects.create(unanswered_q = fake_sq_list[5], user=b3, correct = 1)
b35 = asq.objects.create(unanswered_q = fake_sq_list[6], user=b3, correct = 1)
b31.save()
b32.save()
b33.save()
b34.save()
b35.save()

rb4 = User.objects.create_user('boring banter', email=None, password=None)
b4 = usr.objects.create(user=rb4, col_num = -1)
b4.save()
b41 = asq.objects.create(unanswered_q = fake_sq_list[0], user=b4, correct = 0)
b42 = asq.objects.create(unanswered_q = fake_sq_list[2], user=b4, correct = 0)
b43 = asq.objects.create(unanswered_q = fake_sq_list[3], user=b4, correct = 0)
b44 = asq.objects.create(unanswered_q = fake_sq_list[4], user=b4, correct = 0)
b41.save()
b42.save()
b43.save()
b44.save()

#c people
rc1 = User.objects.create_user('chatchy chatch', email=None, password=None)
c1 = usr.objects.create(user=rc1, col_num = -1)
c1.save()

#d people
rd1 = User.objects.create_user('dirk dagger', email=None, password=None)
d1 = usr.objects.create(user=rd1, col_num = -1)
d1.save()
d11 = asq.objects.create(unanswered_q = fake_sq_list[0], user=d1, correct = 1)
d11.save()

rd2 = User.objects.create_user('dazzle', email=None, password=None)
d2 = usr.objects.create(user=rd2, col_num = -1)
d2.save()
d21 = asq.objects.create(unanswered_q = fake_sq_list[1], user=d1, correct = 1)
d21.save()

rd3 = User.objects.create_user('damn dam', email=None, password=None)
d3 = usr.objects.create(user=rd3, col_num = -1)
d3.save()
d31 = asq.objects.create(unanswered_q = fake_sq_list[2], user=d1, correct = 1)
d31.save()

rd4 = User.objects.create_user('dalai dolama', email=None, password=None)
d4 = usr.objects.create(user=rd4, col_num = -1)
d4.save()
d41 = asq.objects.create(unanswered_q = fake_sq_list[3], user=d1, correct = 1)
d41.save()

rd5 = User.objects.create_user('dragon', email=None, password=None)
d5 = usr.objects.create(user=rd5, col_num = -1)
d5.save()
d51 = asq.objects.create(unanswered_q = fake_sq_list[4], user=d1, correct = 1)
d51.save()

rd6 = User.objects.create_user('dominate deer', email=None, password=None)
d6 = usr.objects.create(user=rd6, col_num = -1)
d6.save()
d61 = asq.objects.create(unanswered_q = fake_sq_list[5], user=d1, correct = 1)
d61.save()

rd7 = User.objects.create_user('dayum dude', email=None, password=None)
d7 = usr.objects.create(user=rd7, col_num = -1)
d7.save()
d71 = asq.objects.create(unanswered_q = fake_sq_list[6], user=d1, correct = 1)
d71.save()

 


