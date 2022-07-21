from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from mysite.forms import MyForm
from mysite.models import Flowers

# Create your views here.

def mysite(request):

    q = request.GET.get('q',None)
    item = ''

    if q is None or q is '':
        flowers = Flowers.objects.all()
    elif q is not None:
        flowers = Flowers.objects.filter(name__contains = q)
    else:
        flowers = Flowers.objects.all() 

    ctx = {'flowers':flowers}

    return render(request,'mysite/mysite.html', ctx)

def detail(request, slug= None):
    flower = get_object_or_404(Flowers, slug = slug)
    ctx = {'flower':flower}

    return render(request,'mysite/detail.html', ctx)

def tag(request, slug=None):
    flowers = Flowers.objects.filter(tag__slug=slug)
    ctx = {"flowers":flowers}
    return render(request, 'mysite/mysite.html',ctx)

def create(request):
    if request.method == 'post':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    
    ctx = {'form':form}
    return render(request, 'mysite/edit.html', ctx)

def edit(request, sg=None):
    flower = get_object_or_404(Flowers, slug = sg)

    if request.method == "POST":
        form = MyForm(request.POST, instance = flower)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
    
    ctx = {'form':form}

    return render(request, 'mysite/edit.html', ctx)

def delete(request, pk = None):
    flower = get_object_or_404(Flowers, pk = pk)
    flower.delete()

    return HttpResponseRedirect('/')