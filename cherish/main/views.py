from django.shortcuts import render

def main(request):
    context = {'message':'Django 很棒'}
    return render(request, 'main/main.html', context)