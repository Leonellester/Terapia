from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import CrudForm
from .models import Terapia

def index(request):
	#return HttpResponse("Index")
	return render(request, 'crud/index.html', {})

def terapia_view(request):
	if request.method == 'POST':
		form = CrudForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('crud:consultar')
	else:
		form = CrudForm()
	return render(request, 'crud/crud_form.html', {'form':form})

def terapia_list(request):
		lista = Terapia.objects.all().order_by('id_terapia')
		contexto = {'lista':lista}
		return render(request, "crud/terapia_list.html", contexto)

def terapia_edit(request, id_terapia):
	lista = Terapia.objects.get(id_terapia=id_terapia)
	if request.method == 'GET':
		form = CrudForm(instance=lista)
	else:
		form = CrudForm(request.POST, instance=lista)
		if form.is_valid():
			form.save()
		return redirect('crud:consultar')
	return render(request, 'crud/crud_form.html', {'form':form})

def terapia_delete(request, id_terapia):
	lista = Terapia.objects.get(id_terapia=id_terapia)
	if request.method == 'POST':
		lista.delete();
		return redirect('crud:consultar')
	return render(request, 'crud/terapia_delete.html', {'lista':lista})