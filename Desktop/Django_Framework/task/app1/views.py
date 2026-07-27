from django.http import HttpResponse

def welcome1(request):
    return HttpResponse("<h1>Welcome to App1 Page</h1>")