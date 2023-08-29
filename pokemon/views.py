from django.http import HttpResponse

def pikachu(request):
    return HttpResponse("pika pika!")

def charmander(request):
    return HttpResponse("charmander!")

def bulbasaur(request):
    return HttpResponse("bulbasaur!")