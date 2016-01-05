from django.shortcuts import render
from mac.models import Category, Page

def mac(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request, 'mac/mac.html', context)

def category(request, categoryID):
    context = {}
    try:
        category = Category.objects.get(id=categoryID)
        context['category'] = category
        context['pages'] = Page.objects.filter(category=category)
    except Category.DoesNotExist:
        pass
    return render(request, 'mac/category.html', context)