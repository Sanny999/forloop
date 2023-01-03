from django.shortcuts import render


def looping(request):
    d={'name':'Rebel star'}
    return render(request,'looping.html',d)

