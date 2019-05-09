from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Hello Friend How Are You ? </h1>")