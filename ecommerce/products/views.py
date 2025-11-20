from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def home(request):
    return render(request, "products/home.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # pass message
            return redirect("products:add_category")
    else:
        form = CategoryForm()
    return render(request,"products/category_form.html",{'form':form})

def category_list(request):
    categories = Category.objects.all()
    return render(request,"products/category_list.html",{'categories':categories})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})
