from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "mainapp/index.html"


class AboutView(TemplateView):
    template_name = "mainapp/about.html"


class ContactView(TemplateView):
    template_name = "mainapp/contact.html"


class ProductsView(TemplateView):
    template_name = "mainapp/products.html"


class ProductDetailView(TemplateView):
    template_name = "mainapp/productdetail.html"


class ShoppingCartView(TemplateView):
    template_name = "mainapp/shoppingcart.html"


