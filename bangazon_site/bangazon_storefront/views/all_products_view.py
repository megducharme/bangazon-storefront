from django.shortcuts import render
# from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required
from bangazon_storefront.models.product_types_model import *
from bangazon_storefront.models.products_model import *

def all_products(request, productTypes_id):
    all_products = Product.objects.filter(product_type=productTypes_id)
    product_type_name = ProductTypes.objects.get(id=productTypes_id)
    context =  {'products' : all_products, "productTypes_id": productTypes_id, "product_type_name":product_type_name.category_name} 
    return render(request, 'bangazon_storefront/all_products.html', context)
