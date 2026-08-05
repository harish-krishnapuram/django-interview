from django.shortcuts import render

# Create your views here.

def calculate(request):
    if request.method=='GET':
        return render(request,'calc.html')
    if request.method=='POST':
        v1 = int(request.POST['v1'])
        v2 = int(request.POST['v2'])
        res = v1+v2
        return render(request,'calc/calculator.html/',{'res':res})