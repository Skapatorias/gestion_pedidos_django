from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {"posts":posts})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)  #FILTRA LA CATEGORIA
    posts = Post.objects.filter(categorias=categoria)   #MUESTRA LOS POST DE LA CATEGORIA FILTRADA
    return render(request, 'blog/categorias.html', {"categoria": categoria, "posts": posts})
