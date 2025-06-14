from dotenv import load_dotenv
import os
from django.shortcuts import render, HttpResponse
from google import genai
from .models import *
from .forms import * 

# Create your views here.
def index(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        
        if form.is_valid():
        
            history = Chat.objects.all()
            question = request.POST.get('question') 

            load_dotenv()
            API_KEY = os.getenv("GOOGLE_API_KEY")
            client = genai.Client(api_key=API_KEY)

            response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents= question
            )
            answer = response.text
            history = Chat.objects.all()
            form.save()
            return render(request=request, template_name='index.html', context={'form': form,'response': answer,'question':question, 'history':history, 'answer':answer })
    
    return render(request=request, template_name='index.html', context={'form': form,})
    

def about(request):
    pass 
    