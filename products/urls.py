from django.urls import path, include
from products.views import catalog, change_product, add_product, purchased, made_purchased, returned, returned_list, submit, reject

app_name = 'products'

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('change_product/<int:product_id>/',change_product, name='change_product'),
    path('add_product',add_product, name='add_product'),
    path('purchased/<int:product_id>/', purchased, name='purchased'),
    path('made_purchased/', made_purchased, name='made_purchased' ),
    path('returned/<int:purchase_id>/', returned, name='returned'),
    path('returned_list/', returned_list, name='returned_list'),
    path('submit/<int:returned_id>/', submit, name='submit'),
    path('reject/<int:returned_id>/', reject, name='reject'),
]