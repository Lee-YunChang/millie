from django.urls import path

from .rest import (
    ProductView,
    ProductDetailView,
)

urlpatterns = [


    path('products', ProductView.as_view(), name='product-list'),

    path('products/<int:product_id>/coupon/<str:coupon_code>', ProductDetailView.as_view(), name='product-detail'),

    path('products/category/<int:category_id>/', ProductView.as_view(), name='product-by-category'),
]
