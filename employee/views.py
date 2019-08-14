from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the polls index.")

"""def check_user(request):
    if request.method=="POST":
        username=request.username
        password= request.password
            """