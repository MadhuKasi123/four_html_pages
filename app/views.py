from django.shortcuts import render

# Create your views here.
def madhu(request):
    return render(request,'one.html')

def muni(request):
    return render(request,'two.html')
def macha(request):
    return render(request,'3rd.html')
def royal(request):
    return render(request,'four.html')

