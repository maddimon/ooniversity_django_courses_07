from django.shortcuts import render
from .forms import QuadraticForm
import math

# Create your views here.
def quadratic_results(request):
    get = request.GET.dict()
    x1 = x2 = None
    form = QuadraticForm()
    if request.method == 'GET':
        if get:
            form = QuadraticForm(request.GET)
        
    context = {'form': form}
                
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        d = b**2 - 4*a*c
         
        if d == 0:
            x1 = x2 = -b / 2*a
        elif d > 0:
            x1 = (-b + math.sqrt(d)) / 2*a
            x2 = (-b - math.sqrt(d)) / 2*a
            
        context['d'] = d
        context['x1'] = x1
        context['x2'] = x2            
    
    return render(request, 'results.html', context)