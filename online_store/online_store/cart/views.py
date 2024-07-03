from django.shortcuts import render

def cart_summary(request):
    return render(request, 'cart/summary.html', {})

def cart_add(request):
    pass

def cart_delete(request):
    pass