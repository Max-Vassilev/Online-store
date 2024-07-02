from django.views import generic as views

class CartSummary(views.TemplateView):
    template_name = 'cart/summary.html'
