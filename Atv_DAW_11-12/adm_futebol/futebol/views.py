from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipe, Jogador
from .forms import EquipeForm, JogadorForm

def equipe_list(request):
    equipes = Equipe.objects.all()
    return render(request, 'equipe_list.html', {'equipe': equipes})

def equipe_create(request):
    form = EquipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('equipe_list')
    return render(request, 'equipe_form.html', {'form': form})

def equipe_update(request, id):
    equipe = get_object_or_404(Equipe, id=id)
    form = EquipeForm(request.POST or None, instance=equipe)
    if form.is_valid():
        form.save()
        return redirect('equipe_list')
    return render(request, 'equipe_form.html', {'form': form})

def equipe_delete(request, id):
    equipe = get_object_or_404(Equipe, id=id)
    if request.method == 'POST':
        equipe.delete()
        return redirect('equipe_list')
    return render(request, 'equipe_confirm_delete.html', {'equipe': equipe})

def jogador_list(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogador_list.html', {'jogadores': jogadores})

def jogador_create(request):
    form = JogadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('jogador_list')
    return render(request, 'jogador_form.html', {'form': form})

def jogador_update(request, id):
    jogador = get_object_or_404(Jogador, id=id)
    form = JogadorForm(request.POST or None, instance=jogador)
    if form.is_valid():
        form.save()
        return redirect('jogador_list')
    return render(request, 'jogador_form.html', {'form': form})

def jogador_delete(request, id):
    jogador = get_object_or_404(Jogador, id=id)
    if request.method == 'POST':
        jogador.delete()
        return redirect('jogador_list')
    return render(request, 'jogador_confirm_delete.html', {'jogador': jogador})
