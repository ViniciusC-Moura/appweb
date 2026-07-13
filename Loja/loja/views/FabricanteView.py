from django.shortcuts import render, redirect
from loja.models import Produto, Fabricante, Categoria
from datetime import timedelta, datetime
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from loja.forms.FabricanteForm import FabricanteForm

def edit_fabricante_view(request, id):
    fabricante = get_object_or_404(Fabricante, id=id)

    if request.method == "POST":
        form = FabricanteForm(request.POST, instance=fabricante)

        if form.is_valid():
            form.save()
            return redirect("/fabricante")
    else:
        form = FabricanteForm(instance=fabricante)

    return render(request, "fabricante/fabricante-edit.html",
        {
            "form": form,
            "fabricante": fabricante
        },
    )

def list_fabricante_view(request, id=None):
    fabricante = request.GET.get("fabricante")

    fabricantes = Fabricante.objects.all()
    #produtos = Produto.objects.first()
    #produtos = Produto.objects.filter(Produto=produto)

    if id is not None:
        fabricantes = fabricantes.filter(id=id)

    print(fabricantes)
    context = {'fabricantes': fabricantes}
    return render(request, template_name='fabricante/fabricante.html', context=context, status=200)

    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)

def details_fabricante_view(request, id=None):
    # Processa o evento GET gerado pela action
    fabricantes = Fabricante.objects.all()
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    print(fabricante)
    context = {'fabricante': fabricante}
    return render(request, template_name='fabricante/fabricante-details.html', context=context, status=200)

def delete_fabricante_view(request, id=None):
    # Processa o evento GET gerado pela action
    fabricantes = Fabricante.objects.all()
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    print(fabricante)
    context = {'fabricante': fabricante}
    return render(request, template_name='fabricante/fabricante-delete.html', context=context, status=200)

def delete_fabricante_postback(request, id=None):
    # Processa o post back gerado pela action
    if request.method == 'POST':
        # Salva dados editados
        id = request.POST.get("id")
        fabricante = request.POST.get("Fabricante")
        print("postback-delete")
        print(id)
        try:
            Fabricante.objects.filter(id=id).delete()
        except Exception as e:
            print("Erro salvando edição de fabricante: %s" % e)
    return redirect("/fabricante")

def create_fabricante_view(request):
    if request.method == "POST":
        form = FabricanteForm(request.POST)

        if form.is_valid():
            fabricante = form.save(commit=False)
            fabricante.alterado_em = fabricante.criado_em
            fabricante.save()
            return redirect("/fabricante")
    else:
        form = FabricanteForm()

    return render(request, "fabricante/fabricante-create.html", {"form": form},)