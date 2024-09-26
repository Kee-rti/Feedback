from django.urls import path
from . import views


urlpatterns = [  
    path('',views.feedback_view, name='feedback_form'),
    path('thank-you/<int:pk>/', views.thank_you, name='thank_you'), 
]


