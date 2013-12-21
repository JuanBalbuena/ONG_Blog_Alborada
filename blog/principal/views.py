from django.shortcuts import render
from principal.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse

class FormularioComentario(ModelForm):
    class Meta:
        model = Comentario
        exclude = ["identrada"]

def poncomentario(request, pk):
    """Add a new comment."""
    p = request.POST

    if 'mensaje' in p:
        autor = "Anónimo"
        if p["autor"]: autor = p["autor"]

        comentario = Comentario(identrada=Entrada.objects.get(pk=pk))
        cf = FormularioComentario(p, instance=comentario)
        cf.fields["autor"].required = False

        comentario = cf.save(commit=False)
        comentario.autor = autor
        comentario.save()
    return HttpResponseRedirect (reverse('principal.views.entrada', args=[pk]))

def entrada(request, pk):
    identrada = Entrada.objects.get(pk=int(pk))
    comentario = Comentario.objects.filter(identrada = identrada)
    d = dict(entrada = identrada, comentario = comentario, form=FormularioComentario(), usuario=request.user)
    d.update(csrf(request))
    return render(request, "entrada.html", d)

def index(request):	
	autores = Autor.objects.all().order_by('id')
	entradas = Entrada.objects.all().order_by('-id')
	paginator = Paginator(entradas, 6)

	page = request.GET.get('page')
	try:
	    entradas = paginator.page(page)
	except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
	    entradas = paginator.page(1)
	except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
	    entradas = paginator.page(paginator.num_pages)

	return render(request, 'index.html', {'entradas':entradas})

