from django.shortcuts import render, redirect
from .forms import feedbackform
from .models import feedback
from datetime import datetime
from django.conf import settings
from django.utils import timezone
import pytz

def feedback_view(request): 
    image_url = settings.MEDIA_URL + 'image.jpg'
    if request.method =='POST':
        form = feedbackform(request.POST)
        if form.is_valid():
            feedback_instance = form.save()
            return redirect('thank_you', pk=feedback_instance.pk)
    else:
        form=feedbackform()
    return render(request, 'app/index.html', {'form':form, 'image_url': image_url})

def thank_you(request, pk):
    Feedback = feedback.objects.get(pk=pk)
    submitted_time = Feedback.submitted_at

    india_tz = pytz.timezone('Asia/Kolkata')
    local_time = submitted_time.astimezone(india_tz).strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"Converted local_time: {local_time}")
    return render(request, 'app/thank_you.html', {
        'feedback': Feedback,
        'submitted_at': local_time
    })
