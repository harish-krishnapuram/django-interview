from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import ProductForm
# Create your views here.
def createProduct(request):
    empty_form = ProductForm()
    if request.method=='GET':
        return render(request,'product/create.html',{'form':empty_form})

    if request.method=='POST':
        form_data = ProductForm(request.POST,request.FILES)
        print('post request')
        if form_data.is_valid():
            form_data.save()
            print('test')
            return HttpResponse('product inserted successfully')
        else:
            print(form_data.errors)
            return HttpResponse('some error happened')