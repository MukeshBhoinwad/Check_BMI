from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def Home(request):
    return render(request,'Home.html')
def AgeCalculater(request):
    age = request.POST.get('age', 'default')
    date1=date.today()
    date2=date1.year
    age1=int(date2)-int(age)
    mukesh={'puk':age1}

    return render(request,'AgeCalculater.html',mukesh)
def BMI(request):
    Weight = request.POST.get('Weight', 'default')
    Hight = request.POST.get('Hight', 'default')
    bmi= float(Weight) / (float(Hight) ** 2)
    mukesh={'puk':bmi}
    return render(request, 'BMI.html',mukesh)
