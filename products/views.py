from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import View, DetailView

from .models import Product, Category
from cart.models import Cart, CartProduct


class HomeView(View):
    products = Product.objects.all()

    def get(self, request):
        return render(request, 'shop/home.html', {'products': self.products})


class ProductDetailView(DetailView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class CategoryDetailView(DetailView):

    model = Category
    queryset = Category.objects.all()
    template_name = "shop/category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = context['object'].product_set.all()
        return context
