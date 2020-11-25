from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import *
from cart.forms import AddProductForm
from cart.cart import Cart


def product_in_category(request, category_slug=None):
    # 맥락변수 3종을 목록 화면으로 전달
    current_category = None
    categories = Category.objects.all()
    cart = Cart(request)
    products = Product.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html',
                  {'current_category': current_category, # 지정된 카테고리 객체
                   'categories': categories,             # 모든 카테고리 객체
                   'products': products,
                   'cart': cart})                # 모든 또는 지정된 카테고리의 상품


@login_required
def product_detail(request, id, product_slug=None):
    # 지정된 상품 객체를 상세 화면으로 전달
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product,
                                                'add_to_cart': add_to_cart,
                                                'cart': cart})


class PrivateView(TemplateView):
    template_name = 'private.html'

    def __int__(self):
        pass


class UseView(TemplateView):
    template_name = 'use.html'

    def __int__(self):
       pass