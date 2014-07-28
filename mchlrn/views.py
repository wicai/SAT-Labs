from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django import forms

#pdfs
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter 
from StringIO import StringIO

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
    driver = webdriver.PhantomJS(executable_path='/Users/Jefferson/Documents/MyBestPlan/electra/phantomjs')

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

        if created:
            #question
            question = driver.find_element_by_xpath("//*[@id='qotdQuestionContainer']/div/p[4]")
            text = question.get_attribute('innerHTML')
            q.question = text

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
            q.answer_A = A.get_attribute('innerHTML')        
            q.answer_B = B.get_attribute('innerHTML')        
            q.answer_C = C.get_attribute('innerHTML')        
            q.answer_D = D.get_attribute('innerHTML')        
            q.answer_E = E.get_attribute('innerHTML')        
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
            return render_to_response('collegeboard/qotdbatch.html', 
                {'questions': questions})
    else:
        form = DateRangeForm()
    return render_to_response('genericformprompt.html',
        {'form': form, 'description': 'Enter Date Range for College Board Questions of the Day'},
        context_instance=RequestContext(request))

def question_of_the_day(request):
    #20130601 earliest day...
    #navigating to page
    driver = webdriver.PhantomJS(executable_path='/Users/Jefferson/Documents/MyBestPlan/electra/phantomjs')
    today = date.today()
    today_string = today.isoformat().replace('-', '')
    url = "http://sat.collegeboard.org/practice/sat-question-of-the-day?questionId=%s&oq=1" % today_string
    driver.get(url)

    #name and check if already in database
    name = 'SAT Question of the Day - %s' % today_string
    q, created = SATQuestion.objects.get_or_create(name=name)

    if created:
        #question
        question = driver.find_element_by_xpath("//*[@id='qotdQuestionContainer']/div/p[4]")
        text = question.get_attribute('innerHTML')
        q.question = text

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
        q.answer_A = A.get_attribute('innerHTML')        
        q.answer_B = B.get_attribute('innerHTML')        
        q.answer_C = C.get_attribute('innerHTML')        
        q.answer_D = D.get_attribute('innerHTML')        
        q.answer_E = E.get_attribute('innerHTML')        
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
        #selected correct answer
        except:
            #nuthin
            pass

        correct_answer = driver.find_element_by_xpath("//*[@id='qotdQuestionResult']/strong").text[-1]
        q.correct_answer = correct_answer
        #explanation
        explanation = driver.find_element_by_xpath("//*[@id='qotdExplDesc']/p[2]").get_attribute('innerHTML')
        q.explanation = explanation
            
        #save the question
        q.save()

    #close the driver
    driver.close()

    return render_to_response("collegeboard/questionoftheday.html",
        {'question': q})

def get_college_board_questions(request):
    a = 5

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