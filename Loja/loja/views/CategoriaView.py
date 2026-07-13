from django.shortcuts import render, redirect
from loja.models import Produto, Fabricante, Categoria
from datetime import timedelta, datetime
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

def edit_categoria_postback(request, id=None):
    if request.method == 'POST':
        # Salva dados editados
        id = request.POST.get("id")
        categoria = request.POST.get("Categoria")
        print(id)
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            obj_categoria.Categoria = categoria
            print(obj_categoria.Categoria)
            obj_categoria.save()
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")

def edit_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categoria = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-edit.html', context=context, status=200)

def list_categoria_view(request, id=None):
    categoria = request.GET.get("categoria")

    categorias = Categoria.objects.all()
    #produtos = Produto.objects.first()
    #produtos = Produto.objects.filter(Produto=produto)

    if id is not None:
        categorias = categorias.filter(id=id)

    print(categorias)
    context = {'categorias': categorias}
    return render(request, template_name='categoria/categoria.html', context=context, status=200)

    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)

def details_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-details.html', context=context, status=200)

def delete_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-delete.html', context=context, status=200)

def delete_categoria_postback(request, id=None):
    # Processa o post back gerado pela action
    if request.method == 'POST':
        # Salva dados editados
        id = request.POST.get("id")
        categoria = request.POST.get("Categoria")
        print("postback-delete")
        print(id)
        try:
            Categoria.objects.filter(id=id).delete()
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")

def create_categoria_view(request, id=None):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        categoria = request.POST.get("Categoria")
        print(categoria)
        try:
            obj_categoria = Categoria()
            obj_categoria.Categoria = categoria
            obj_categoria.alterado_em = obj_categoria.criado_em
            obj_categoria.save()
            print("Categoria %s salvo com sucesso" % categoria)
        except Exception as e:
            print("Erro inserindo categoria: %s" % e)
        return redirect("/categoria")
    return render(request, template_name='categoria/categoria-create.html', status=200)