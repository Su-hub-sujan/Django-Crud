from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import ListView
import  requests
import  json

# this function will add and shows  the data of the form
global  do_get
def do_get(url,params={}):
    #dict={'q':'sujan', 'roll': '11'}
    query=''
    #for key in dict.keys():
    # query += str(key) + '=' + str(dict[key]) + "&"
    #name=str(key)
    #value=str(dict[key])
    full_url = 'http://127.0.0.1:8000'

    #qs = 'q=sujan&roll=1'

    #full_url='http://127.0.0.1:8000/json?name&value'
    print(full_url)
    response=requests.get(full_url, params=params)
    return response




def json(request):
    qs={}
    qs=(User.objects.all())
    '''if(request.headers['sujan']=='Token ABCD'):
        return HttpResponse(qs,safe=False)
    else:
        return 'error'''



    #return JsonResponse(serializers.serialize('json',[data],fields=['name','email','password']), content_type='application/json')
    #return JsonResponse(qs,safe=False)
    data = serializers.serialize("json", qs, fields=('name', 'email', 'password'))
    return JsonResponse(data, content_type="application/json",safe=False)

# this function will add and shows  the data of the form
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)

            reg.save()
            fm = StudentRegistration()

    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm,'stu':stud})
# this section is for deleting the data
def  delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return  HttpResponseRedirect('/')

#this will edit or delete
def update(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()

    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration( instance=pi)
    return render(request,'enroll/update.html',{'forms':fm})

def token(request):
    qs=User.objects.values
    query =requests.get('http://127.0.0.1:8000',{'as':qs})





    #response = requests.get('http://127.0.0.1:8000/json/', headers={'sujan': 'Token ABCD'}).json()
    #if (requests.header.token == token):

    return JsonResponse(query,safe=False)

    #else:
      # return {'error':'invalid_token'}

# Create your views here.


