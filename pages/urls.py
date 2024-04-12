# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:exercise_angina>/<str:oldpeak>/<int:chest_pain_type_asy>/<int:chest_pain_type_ata>/<int:st_slope_flat>', results, name='results'),

]
