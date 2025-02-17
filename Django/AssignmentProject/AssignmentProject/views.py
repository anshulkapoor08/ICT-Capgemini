from django.views.decorators.http import require_http_methods
from django.http import HttpResponse ,HttpResponseNotFound

@require_http_methods(["GET"])    
def hello(request):  
    return HttpResponse("<h1>Hello, Welcome to Django!</h1>")

def greetings(request, msg="Good Morning"):  
    message="<h1>Hello, Welcome to Django!</h1><Br>" +msg
    return HttpResponse(message)