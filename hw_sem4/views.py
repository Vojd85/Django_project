from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import forms
from . import models 

def index(request):
    products = models.Product.objects.all()
    return render(request, 'hw_sem3/index.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            if image:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['amount']
            product = models.Product(name=name, price=price, count=count, description=description, image=image)
            product.save()
            return redirect('index')
    else:
        form = forms.ProductForm()
    return render(request, 'hw_sem4/add_edit_product.html', {'form': form, 'title': 'Добавление продукта'})

def change_product(request, product_id):
    product = models.Product.objects.filter(pk=product_id).first()
    form = forms.ProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if image:
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product.image = image
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.price = form.cleaned_data['price']
        product.count = form.cleaned_data['count']
        product.save()
        return redirect('index')
    else:
        form = forms.ProductForm(initial={'name': product.name, 'description': product.description,
                                          'price': product.price, 'count': product.count, 'image': product.image})

    return render(request, 'hw_sem4/add_edit_product.html', {'form': form, 'title': 'Изменение продукта'})
