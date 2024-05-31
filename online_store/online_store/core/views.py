from django.core.paginator import Paginator
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

        paginator = Paginator(tech_items, 18)
        print()
        print(f"Paginator: {paginator}")
        page_number = self.request.GET.get('page')
        print(f"Page number: {page_number}")
        page_obj = paginator.get_page(page_number)

        print("Here:")
        for item in page_obj:
            print(item)

        context['page_obj'] = page_obj
        context['current_category'] = category

        return context
