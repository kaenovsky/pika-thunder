from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Pokemon(object):

    def __init__(self, name, numb, color):
        self.name = name
        self.numb = numb
        self.color = color

def pokemon(request, name):

    if name == 'bulbasaur':
        pokemon = Pokemon("Bulbasaur", "1", "#7c5")
        
    elif name == 'charmander':
        pokemon = Pokemon("Charmander", "4", "#f42")

    elif name == 'pikachu':
        pokemon = Pokemon("Pikachu", "25", "#fc3")

    ext_doc = open("./pokemon/templates/pokemon.html")
    templ = Template(ext_doc.read())
    ext_doc.close()
    ctx = Context({ "pokemon_name" : pokemon.name, "pokemon_number" : pokemon.numb, "bg" : pokemon.color })
    document = templ.render(ctx)

    return HttpResponse(document)