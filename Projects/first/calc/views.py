from django.shortcuts import render
from django.http import HttpResponse

def Hello(request):
    return render(request,'home.html')

# Create your views here.
def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    # print(val2)
    # print(res)

    return render(request, 'result.html', {'result':res})