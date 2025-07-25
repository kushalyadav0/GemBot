from dotenv import load_dotenv
import os
from django.shortcuts import render, HttpResponse
from google import genai
from .models import *
from .forms import * 
from django.contrib.auth.decorators import login_required

# Create your views here.   
@login_required
def gembot_view(request):
    form = InputForm()
    if request.method == 'POST':
        form = InputForm(request.POST)
        
        if form.is_valid():
            question = request.POST.get('question') 

            load_dotenv()
            API_KEY = os.getenv("GOOGLE_API_KEY")
            client = genai.Client(api_key=API_KEY)

            response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents= question
            )
            answer = response.text
            # creating a cht instance manually to assign request.user 
            Chat.objects.create(
               user=request.user,
               question=question,
               answer=answer
           )
            history= Chat.objects.filter(user=request.user).order_by('-timestamp')
            return render(request,'index.html',{'form': InputForm,
                                                'response': answer,
                                                'question':question, 
                                                'history':history,
                                                })
    
    return render(request,'index.html', {'form': form,})
   