from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from product.views.product import CreateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView
from .routers import router

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', views.product.list_products, name='list.product'),
    path('api/', include(router.urls)),
    path('add_product', TemplateView.as_view(template_name='index.html')),
]
