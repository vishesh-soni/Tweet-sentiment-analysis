import re
from django.shortcuts import render
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
import textblob

# import time

# Create your views here.

def index(request):
    # output = request.POST.get('name')
    # context = {"output":output}
    return render(request,'index.html')
    # return render(request,'index.html')

def cleanText(text):
    text = re.sub('@[A-Za-z0-9]+', '',text)
    text = re.sub('#', '',text)
    text = re.sub('RT[\s]+', '',text)
    text = re.sub('https?:\/\/\S+', '',text)

def getPolarity(text):
    return textblob.TextBlob(text).sentiment.polarity

def predict(request):
    if request.method == 'POST':
        temp = request.POST.get('text')
        
        # text = cleanText(temp)
        output = getPolarity(str(temp))

        if output>0.2:
            out = "POSITIVE"
        elif output<0.2:
            out = " NEGATIVE"
        else:
            out = "NEUTRAL"

        context = {
            'temp':temp,
            'out':out
        }
    
        return render(request,'predict.html',context)
