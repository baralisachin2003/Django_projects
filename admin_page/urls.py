from django.urls import path
from . import views

urlpatterns = [
    path('addcategory/',views.add_category),
    path('addproduct/',views.add_product),
    path('product/',views.show_product),
    path('category/',views.show_category),
    path('delete_category/<int:category_id>',views.category_delete),
    path('update_category/<int:category_id>',views.category_update),
    path('delete_product/<int:product_id>',views.product_delete),
    path('update_product/<int:product_id>',views.product_update),
    path('userorder/',views.user_order),
]