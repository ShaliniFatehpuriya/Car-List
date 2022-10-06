from contextlib import redirect_stdout
from multiprocessing import context
from statistics import mode
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from . import models

# Create your views here.
def list(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request,'cars/list.html',context=context)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand,year=year)
        #if user submitted new car go to list.html
        return HttpResponseRedirect(reverse('cars:list'))
    else:
        return render(request,'cars/add.html')
    
def delete(request):
    if request.POST:
        pk = request.POST['pk']

        try:
            models.Car.objects.get(pk=pk).delete()
            return HttpResponseRedirect(reverse('cars:list'))
        except:
            print('PK not found')
            return HttpResponseRedirect(reverse('cars:list'))
    else:
        return render(request,'cars/delete.html')