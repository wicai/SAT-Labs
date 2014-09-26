from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django import forms

#selenium
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#models
from mchlrn.models import SATQuestion

#dates
import datetime
from datetime import date, timedelta

def home(request):
	return render_to_response('home.html')

class FileForm(forms.Form):
	upload_file = forms.FileField()

#starts at collegeboard qotd for start_date and goes
#BACKWARD to end_Date...
#if no end_date, just gets qotd for start_date
#returns a list of questions (not necessarily all were created, since get_or_create is used)
def qotd_selenium(start_date, end_date=None):
    driver = webdriver.PhantomJS(executable_path='mchlrn/static/phantomjs/phantomjs_mac')

    qotd_date = start_date
    if not end_date:
        end_date = start_date
    questions = []

    while qotd_date >= end_date:
        date_string = qotd_date.isoformat().replace('-', '')
        url = "http://sat.collegeboard.org/practice/sat-question-of-the-day?questionId=%s&oq=1" % date_string
        driver.get(url)

        #name and check if already in database
        name = 'SAT Question of the Day - %s' % date_string
        q, created = SATQuestion.objects.get_or_create(name=name)

        try:
            #question
            question = driver.find_element_by_xpath("//*[@id='qotdQuestionContainer']/div/p[4]")
            text = question.get_attribute('innerHTML')
            q.question = text

            #category
            cat_text = driver.find_element_by_xpath("//*[@id='main']/div[4]/div[2]/div[1]/p").text.split(" > ")

            if cat_text[0] == 'Critical Reading':
                q.category = 'Reading'
            else:
                q.category = cat_text[0]

            q.sub_category = cat_text[1]

            #instructions
            instructions = driver.find_element_by_xpath("//*[@id='qotdQuestionContainer']/div/p[2]/em")
            text = instructions.get_attribute('innerHTML')
            q.instructions = text
            q.css = 'css/sat_merge.css'

            #answers
            A = driver.find_element_by_xpath("//*[@for='qotdChoicesA']")
            B = driver.find_element_by_xpath("//*[@for='qotdChoicesB']")
            C = driver.find_element_by_xpath("//*[@for='qotdChoicesC']")
            D = driver.find_element_by_xpath("//*[@for='qotdChoicesD']")
            E = driver.find_element_by_xpath("//*[@for='qotdChoicesE']")
            q.answer_A = A.get_attribute('innerHTML')[3:]        
            q.answer_B = B.get_attribute('innerHTML')[3:]        
            q.answer_C = C.get_attribute('innerHTML')[3:]     
            q.answer_D = D.get_attribute('innerHTML')[3:]        
            q.answer_E = E.get_attribute('innerHTML')[3:]        
            q.channel = 'SAT Question of the Day'
            q.channel_url = url

            #correct answer and explanation
            click_A = driver.find_element_by_id('qotdChoicesA')
            click_A.click()
            submit = driver.find_element_by_id('qotdSubmit')
            submit.click()

            #selected wrong answer
            try:
                show_correct = driver.find_element_by_id('qotdShowAnswer')
                show_correct.click()
                correct_answer = driver.find_element_by_xpath("//*[@id='qotdQuestionResult']/strong").text[-1]
            #selected correct answer
            except:
                #A was correct
                correct_answer = 'A'

            q.correct_answer = correct_answer

            #explanation
            explanation = driver.find_element_by_xpath("//*[@id='qotdExplDesc']/p[2]").get_attribute('innerHTML')
            q.explanation = explanation
                
            #save and append the question
            q.save()

        except Exception as inst:
            #delete the question, there was an error
            q.delete()
            driver.close()
            return HttpResponse(inst)

        questions.append(q)

        #decrease the date by one day
        qotd_date = qotd_date - timedelta(days=1)
        
    #close the driver
    driver.close()

    #return the questions
    return questions

class DateRangeForm(forms.Form):
    start_date = forms.DateField(initial=date.today)
    end_date = forms.DateField(initial=date(2013, 6, 1))

def qotd_batch(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            questions = qotd_selenium(start_date, end_date=end_date)
            return render_to_response('questionscreated.html', 
                {'questions': questions})
    else:
        form = DateRangeForm()
    return render_to_response('genericformprompt.html',
        {'form': form, 'description': 'Enter Date Range for College Board Questions of the Day'},
        context_instance=RequestContext(request))

class NumForm(forms.Form):
    num = forms.IntegerField(initial=0)

def batch_4tests(request):
    if request.method == 'POST':
        form = NumForm(request.POST)
        if form.is_valid():
            skip = form.cleaned_data['num']
            driver = webdriver.PhantomJS(executable_path='mchlrn/static/phantomjs/phantomjs_mac')
            driver.get("http://www.4tests.com/exams/questions.asp?exid=23654430&googlebot=6")
            questions = []

            num = 1
            
            while True:
                try:
                    q = None
                    if num > skip:
                        cat_ele = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td[1]/b")
                        cat_text = cat_ele.text.split(' ')[1]
                        if cat_text == 'Critical':
                            category = "Reading"
                        else:
                            category = "Math"
                        question = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[1]/td[2]/font").get_attribute('innerHTML')
                        answer_A = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[3]/td[2]/font").get_attribute('innerHTML')
                        answer_B = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[4]/td[2]/font").get_attribute('innerHTML')
                        answer_C = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[5]/td[2]/font").get_attribute('innerHTML')
                        answer_D = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[6]/td[2]/font").get_attribute('innerHTML')
                        try:  
                            answer_E = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[7]/td[2]/font").get_attribute('innerHTML')
                        except:
                            answer_E = None
                            pass

                        view_answer = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/a")
                        view_answer.click()

                        explanation = driver.find_element_by_xpath("//*[@id='frmQuestion']/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td").get_attribute('innerHTML')
                        correct_answer_ele = driver.find_element_by_class_name('answerred').get_attribute('innerHTML')
                        if answer_A == correct_answer_ele:
                            correct_answer = 'A'
                        elif answer_B == correct_answer_ele:
                            correct_answer = 'B'
                        elif answer_C == correct_answer_ele:
                            correct_answer = 'C'
                        elif answer_D == correct_answer_ele:
                            correct_answer = 'D'
                        elif answer_E == correct_answer_ele:
                            correct_answer = 'E'

                        channel = '4Tests SAT Test'
                        channel_url = driver.current_url

                        name = channel + ' ' + str(num) + ' - ' + category

                        q, created = SATQuestion.objects.get_or_create(name=name)

                        q.question = question
                        q.answer_A = answer_A
                        q.answer_B = answer_B
                        q.answer_C = answer_C
                        q.answer_D = answer_D
                        q.answer_E = answer_E
                        q.correct_answer = correct_answer
                        q.channel = channel
                        q.channel_url = channel_url
                        q.category = category
                        q.explanation = explanation

                        q.save()

                    next = driver.find_element_by_xpath("//*[@title='Next Question']")
                    next.click()

                    num += 1

                except Exception as inst:
                    if q:
                        q.delete()
                    driver.close()
                    return HttpResponse(inst)
                    break

                #end of while

            driver.close()

            return render_to_response('questionscreated.html',
                {'questions': questions})
    else:
        form = NumForm()
    return render_to_response('genericformprompt.html',
        {'form': form, 'description': 'Enter Number of Questions to Skip'},
        context_instance=RequestContext(request))


def question_of_the_day(request):
    #20130601 earliest day...
    #navigating to page
    driver = webdriver.PhantomJS(executable_path='mchlrn/static/phantomjs/phantomjs_mac')
    today = date.today()
    start_date = today
    end_date = today
    q = qotd_selenium(start_date, end_date=end_date)[0]
    return render_to_response('collegeboard/questionoftheday.html', 
                {'question': q})


def parse_PDF(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            efl = request.FILES['upload_file'].read()
            memory_file = StringIO(efl)
            parser = PDFParser(memory_file)
            document = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            codec = 'utf-8'
            device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)
                data = retstr.getvalue()
            #u = data.decode('cp1251')
            #s = u.encode('utf-8')
            return render_to_response('pdfs/parsePDF.html', 
                {'parse': data})
        else:
        	return render_to_response('genericformprompt.html',
            	{'form': form, 'description': 'Select a PDF...', 'enctype':'multipart/form-data'})
    else:
        form = FileForm()
        return render_to_response('genericformprompt.html',
            {'form': form, 'description': 'Select a PDF...', 'enctype':'multipart/form-data'},
            context_instance=RequestContext(request))