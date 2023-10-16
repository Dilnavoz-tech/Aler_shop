from django.shortcuts import render
from django.views import View

from main.models import Product, Picture


class HomeView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        products = Product.objects.all()
        print(products)
        product_data = []
        for product in products:
            image = Picture.objects.filter(product=product).first()
            product.image = image
            product_data.append(product)
        self.context.update({'products': product_data})
        return render(request, self.template_name, self.context)


class ProfileView(View):
    def get(self,request):
        return render(request, 'profile.html')


class BlogView(View):
    def get(self,request):
        return render(request, 'blog.html')


class PropertyGridView(View):
    def get(self,request):
        return render(request, 'property.html')


class AboutView(View):
    def get(self,request):
        return render(request, 'about.html')