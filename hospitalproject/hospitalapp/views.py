from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import People


# Create your views here.
def home(request):
    obj = Place.objects.all()
    obj1 = People.objects.all()
    return render(request, "index.html", {'result': obj , 'result1': obj1})


# def people(request):
#     obj1 = People.objects.all()
#
#     return render(request, "index.html", {'result1': obj1})

# def operations(request):
#    x = int(request.GET['num 1'])
#    y = int(request.GET['num 2'])
#    addition1 = x + y
#    subtraction1 = x - y
#    multiplication1 = x * y
#    division1 = x / y

#    return render(request, "result.html",
#                  {'result1': addition1, 'result2': subtraction1, 'result3': multiplication1, 'result4': division1})
# def about(request):
#    return render(request,"result.html")
# def contact(request):
#    return HttpResponse("This is contact page")
# def details(request):
#    return render(request,"details.html")
# def thanks(request):
#    return HttpResponse("This is thanks page")
