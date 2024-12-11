from django.urls import path

from .rest import (
    ProductView,
)



urlpatterns = [

    path('product/<int:product_id>', ProductView.as_view(), name='product'),
]