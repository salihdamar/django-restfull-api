from django.http import JsonResponse
from django.shortcuts import render
from .models import Product


def product_list(request):
    products= Product.objects.all()
    data= {'products': list(products.values())}
    return JsonResponse(data)


def product_details(resquest, pk):
    try:
        product= Product.objects.get(pk=pk)
        data={
            'id': product.id,
            'name': product.name,
            'slug': product.slug,
            #'category': product.category.id, #hata verdi düzenle burayı
            'stock': product.stock,
            'description': product.description,
            'price': str(product.price),
            'is_home': product.is_home,
            'is_active': product.is_active,

        }
        return JsonResponse(data)
    
    except Product.DoesNotExist:
        return JsonResponse({'eror':'Productnot found'},status=404)
       