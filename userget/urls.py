from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ArticleDetailView
from .views import ProductList
from .views import category_list

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [

    # http://127.0.0.1:8000/api/users/ Задание 1
    #  Создайте ViewSet, который позволяет получить список всех пользователей из базы данных. Пользователи должны иметь возможность получить список всех пользователей в формате JSON, используя метод GET.
    path('api/', include(router.urls)),

    # http://127.0.0.1:8000/products/
    # Задание 2
    # Создайте APIView, которое позволяет получить список всех товаров из базы данных.
    # Пользователи должны иметь возможность получить список всех товаров в формате JSON, используя метод GET.
    path("products/", ProductList.as_view(), name="product-list"),

    # Задание 3
    # http://127.0.0.1:8000/categories/
    # Создайте функцию с декоратором @api_view(['GET']), которая позволяет получить список всех категорий из базы данных.
    # Пользователи должны иметь возможность получить список всех категорий в формате JSON, используя метод GET.
    path("categories/", category_list, name="category-list"),

    # Задание 4
    # http://127.0.0.1:8000/articles/1/
    # Создайте GenericAPIView с использованием RetrieveUpdateDestroyAPIView,
    #    которое позволяет просматривать информацию об отдельной статье по её уникальному идентификатору (ID).
    #   Пользователи должны иметь возможность получить информацию о статье в формате JSON,
    #   используя метод GET, обновить данные статьи, используя метод PUT или PATCH, и удалить статью,
    #   используя метод DELETE..
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),



]

