from django.shortcuts import render, get_object_or_404

from shop.models import Category, Sneaker


def index(request):
    return render(request, 'index.html', {'title': 'HypeBeast'})


def show_categories(request):
    return render(request, 'categories.html', {'categories': Category.objects.all(),
                                               'title': 'HypeBeast', 'items': Sneaker.objects.all()})


# def product(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Sneaker.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'shop/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products,
#                    'title': 'HypeBeast'})


def product_detail(request, id, slug):
    sneaker = get_object_or_404(Sneaker, id=id, slug=slug)
    context = {'product': sneaker,
               'title': sneaker.title}
    # available=True)
    return render(request, template_name='product.html', context=context)
