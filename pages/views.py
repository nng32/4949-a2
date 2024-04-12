# pages/views.py
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .production import get_results

def homePageView(request):
    return render(request, 'home.html')

def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')


def homePost(request):
    # Create variable to store choice that is recognized through entire function.
    exercise_angina = -999
    oldpeak = -999
    chest_pain_type_asy = -999
    chest_pain_type_ata = -999
    st_slope_flat = -999

    try:
        print('exercise_angina' in request.POST)
        # Extract value from request object by control name.
        exercise_angina = 1 if 'exercise_angina' in request.POST else 0
        oldpeak = float(request.POST['oldpeak'])
        chest_pain_type_asy = 1 if 'chest_pain_type_asy' in request.POST else 0
        chest_pain_type_ata = 1 if 'chest_pain_type_ata' in request.POST else 0
        st_slope_flat = 1 if 'st_slope_flat' in request.POST else 0


    # # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': 'There is an error with the form. Correct all errors and try again.'})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={
            'exercise_angina': exercise_angina,
            'oldpeak': oldpeak,
            'chest_pain_type_asy': chest_pain_type_asy,
            'chest_pain_type_ata': chest_pain_type_ata,
            'st_slope_flat': st_slope_flat
        }))


def results(request, exercise_angina, oldpeak, chest_pain_type_asy, chest_pain_type_ata, st_slope_flat):
    print("*** Inside results()")
    prediction = get_results(exercise_angina, oldpeak, chest_pain_type_asy, chest_pain_type_ata,
                                        st_slope_flat)
    return render(request, 'results.html', {
            'exercise_angina': "Yes" if exercise_angina else "No",
            'oldpeak': oldpeak,
            'chest_pain_type_asy': "Yes" if chest_pain_type_asy else "No",
            'chest_pain_type_ata': "Yes" if chest_pain_type_ata else "No",
            'st_slope_flat': "Yes" if st_slope_flat else "No",
            'prediction': 'Not at risk' if prediction[0] == 0 else 'At risk'
        })

