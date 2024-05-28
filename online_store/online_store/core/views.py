from django.shortcuts import render
from django.views import generic as views
from .models import TechItem

class BasePageView(views.TemplateView):
    template_name = 'core/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category', 'all')

        if category == 'all':
            tech_items = TechItem.objects.all()
        else:
            tech_items = TechItem.objects.filter(category=category)

        context['tech_items'] = tech_items
        context['current_category'] = category

        return context
