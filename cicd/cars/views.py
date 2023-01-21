from django.http import HttpResponse

def index(request):
    HttpResponse('Sample view')