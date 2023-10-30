
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from rest_framework import views, generics
from rest_framework.response import Response
from .models import Product, Article, Category
from .serializers import ProductSerializer, ArticleSerializer, UserSerializer

@api_view(['GET'])
def category_list(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class UserViewSet(ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer



class ProductList(views.APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)




class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ A view that returns the detail of an article in JSON format. """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer