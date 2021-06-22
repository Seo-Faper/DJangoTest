from django.shortcuts import render
from .models import Game

def index(request):
    game_list = Game.objects.order_by('-game_dir')
    context = {'game_list': game_list}
    return render(request, 'navy_GBA/main.html',context)