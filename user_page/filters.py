import django_filters
from admin_page.models import Product
from django_filters import CharFilter

class ProductFilter(django_filters.Filter):
    product_name = CharFilter(field_name='product_name',lookup_expr = 'icontains')
    
    class Meta:
        model=Product
        fields = ''
        exclude = ['product_price','stock','product_image_url','product_description','category','created_at']