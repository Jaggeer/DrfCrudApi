from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework import viewsets
from .models import Product, ProductType, Price
from .serializers import ProductSerializer, ProductTypeSerializer, PriceSerializer

# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['patch'], detail=True, url_path=r'updateAmount/(?P<decrease>[0-9]+)')
    def updateAmount(self, request, pk=None, decrease=0):
        product = Product.objects.get(pk=pk)
        amount = int(getattr(product, "amount"))
        amount = amount - int(decrease)
        product.amount = amount
        product.save()
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    
class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer