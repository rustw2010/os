from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from linux.models import Category, Page
from linux.forms import CategoryForm, PageForm
# Create your views here.
def linux(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'linux/linux.html',context)

def category(request, categoryID):
    context = {}
    try:
        category = Category.objects.get(id=categoryID)
        context['category'] = category
        context['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
     pass
    return render(request, 'linux/category.html', context)

def addCategory(request):
    template = 'linux/addCategory.html'
    if request.method=='GET':
        return render(request, template, {'form':CategoryForm()})
  # request.method=='POST'
    form = CategoryForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    return redirect(reverse('linux:linux'))
 # Or try this: return wiki(request) 
 
def addPage(request, categoryID):
     template = 'linux/addPage.html'
     try:
         pageCategory = Category.objects.get(id=categoryID)
     except Category.DoesNotExist:
        return category(request, categoryID)
     context = {'category':pageCategory}
     if request.method=='GET':
        context['form'] = PageForm()
        return render(request, template, context)
    # request.method=='POST'
     form = PageForm(request.POST)
     context['form'] = form
     if not form.is_valid():
        return render(request, template, context)
     page = form.save(commit=False)
     page.category = pageCategory
     page.save()
     return redirect(reverse('linux:category', args=(categoryID, )))
 
def deleteCategory(request, categoryID):
    if request.method!='POST':
        return linux(request)
    # request.method=='POST':
    categoryToDelete = Category.objects.get(id=categoryID)
    if categoryToDelete:
        categoryToDelete.delete()
    return redirect(reverse('linux:linux'))

def deletePage(request, pageID):
    if request.method!='POST':
        return linux(request)
    # request.method=='POST':
    pageToDelete = Page.objects.get(id=pageID)
    if pageToDelete:
        categoryID = pageToDelete.category.id
        pageToDelete.delete()
    else:
        categoryID = ''
    return redirect(reverse('linux:category', args=(categoryID, )))


def updateCategory(request, categoryID):
    template = 'linux/updateCategory.html'
    try:
        category = Category.objects.get(id=categoryID)
    except Category.DoesNotExist:
        return linux(request)
    if request.method=='GET':
        form = CategoryForm(instance=category)
        return render(request, template, {'form':form, 'category':category})
    # request.method=='POST'
    form = CategoryForm(request.POST, instance=category)
    if not form.is_valid():
        return render(request, template, {'form':form, 'category':category})
    form.save()
    return redirect(reverse('linux:linux'))


def updatePage(request, pageID):
    template = 'linux/updatePage.html'
    try:
        page = Page.objects.get(id=pageID)
    except Page.DoesNotExist:
        return category(request, '')
    if request.method=='GET':
     form = PageForm(instance=page)
     return render(request, template, {'form':form, 'page':page})
    # request.method=='POST'
    form = PageForm(request.POST, instance=page)
    if not form.is_valid():
        return render(request, template, {'form':form, 'page':page})
    form.save()
    return redirect(reverse('linux:category', args=(page.category.id,)))