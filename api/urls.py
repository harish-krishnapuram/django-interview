from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products-viewset',views.ProductViewSet)


urlpatterns = [
    #function based apis end point
    path('get/',views.product_list),
    path('get/<int:pk>/',views.product_detail),

    #classbased apiviews
    path("products/", views.ProductList.as_view()),
    path("products/<int:pk>/", views.ProductDetail.as_view()),

    #generic apiviews
    path("products-gen/", views.ProductListGen.as_view()),
    path("products-gen/<int:pk>/", views.ProductDetailGen.as_view()),
]

urlpatterns = urlpatterns+router.urls