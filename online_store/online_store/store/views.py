from django.core.paginator import Paginator
from django.views import generic as views
from .models import TechItem

class BasePageView(views.TemplateView):
    template_name = 'store/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = self.kwargs.get('category')
        if category:
            tech_items = TechItem.objects.filter(category=category)
        else:
            tech_items = TechItem.objects.all()

        paginator = Paginator(tech_items, 18)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['current_category'] = category

        return context
    
class ProductDetailView(views.DetailView):
    model = TechItem
    template_name = 'store/product.html'
    context_object_name = 'product'

class AboutPageView(views.TemplateView):
    template_name = 'store/about.html'

class ContactsPageView(views.TemplateView):
    template_name = 'store/contacts.html'
