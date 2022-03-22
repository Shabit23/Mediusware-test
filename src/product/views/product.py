from django.views import generic
from django.db.models import Q
from django.shortcuts import render, redirect
from product.models import Variant, Product, ProductVariant, ProductVariantPrice

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context


def list_products(request):
    variants = ProductVariant.objects.order_by('variant_title').values_list('variant_title', flat=True).distinct()
    styles = variants.filter(variant__title__contains="Style")
    colors = variants.filter(variant__title__contains="Color")
    sizes = variants.filter(variant__title__contains="Size")
    

    if request.method == "POST":
        title = request.POST['title']
        variant = request.POST['variant']
        price_from = request.POST['price_from']
        price_to = request.POST['price_to']
        date = request.POST['date']
        product_list = []
        products = ProductVariantPrice.objects.filter(product__title__contains=title)
        variantes = ProductVariantPrice.objects.filter(Q(product_variant_one__variant_title__contains=variant) | Q(product_variant_two__variant_title__contains=variant) | Q(product_variant_three__variant_title__contains=variant))
        prices = ProductVariantPrice.objects.filter(price__range=(price_from, price_to))
        dates = ProductVariantPrice.objects.filter(created_at__contains=date)

        for product in products:
            for price, variant, date in zip(prices, variantes, dates):
                if product.product == price.product:
                    product_list.append(product)
                if product.product == variant.product:
                    product_list.append(product)
                # if product.product == date.product:
                #     product_list.append(product)
   
        paginator = Paginator(product_list, 10)
        page = request.GET.get('page')
        products_all = paginator.get_page(page)
        nums = products_all.paginator.num_pages

        return render(request, 'products/list.html', {
            'nums': "0" * nums,
            'product_list': product_list,
            'products_all': products_all,
            # 'products': products[0].product,
            # 'prices': prices,
            'styles': styles,
            'colors': colors,
            'sizes': sizes
        })

    else:
        return render(request, 'products/list.html', {
            'styles': styles,
            'colors': colors,
            'sizes': sizes
        })


# def add_product(request):
#     submitted = False
#     if request.method == "POST":
        