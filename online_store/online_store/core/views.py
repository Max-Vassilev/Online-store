from django.shortcuts import render
from django.views import generic as views
from .models import TechItem  # Import the TechItem model

class BasePageView(views.TemplateView):
    template_name = 'core/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pass all instances of TechItem to the template
        tech_items = TechItem.objects.all()
        context['tech_items'] = tech_items

        return context


