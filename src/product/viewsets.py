from rest_framework import viewsets
from .models import Product, ProductImage, ProductVariant, ProductVariantPrice, Variant
from .serializers import ProductSerializer, ProductImageSerializer, ProductVariantSerializer, ProductVariantPriceSerializer, VariantSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductVariantViewSet(viewsets.ModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

class ProductVariantPriceViewSet(viewsets.ModelViewSet):
    queryset = ProductVariantPrice.objects.all()
    serializer_class = ProductVariantPriceSerializer

class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer