from django.http import Http404
from django.views.generic import ListView, DetailView

from shop.models import Category, Sneaker


class HomeShop(ListView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HypeBeast'
        return context

    def get_queryset(self):
        pass


class CategoryShop(ListView):
    template_name = 'categories.html'
    model = Sneaker
    context_object_name = 'sneakers'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'HypeBeast'
        return context

    def get_queryset(self):
        return Sneaker.objects.filter(available=True)


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = Sneaker
    context_object_name = 'product'

    def get_object(self, queryset=None):
        try:
            return Sneaker.objects.get(pk=self.kwargs.get('pk'), slug=self.kwargs.get('slug'))
        except Sneaker.DoesNotExist:
            raise Http404()
