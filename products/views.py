from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Feedback
from .forms import FeedbackForm
# Create your views here.


def index(response):
    user='hanzel'
    products_num = 7
    # suits = Product.objects.filter(brand=1)
    suits = Product.objects.filter(brand__title="Pitonjet")
    # brand = Brand.objects.get(title="Pitonjet")
    # piton = brand.product_set.all()
    # piton = brand.product.all()
    # print(piton)
    products_index = Product.objects.all().order_by("-id")[:3]
    return render(response,"products/home.html", {
        "products":products_index,
    })

def signup(response):
    return render(response,"products/signup.html", {})

def products(response, product):
    if product == "suits":
        return HttpResponse(f"This is {product} list page")
    else:
        return HttpResponse("the page doesnot exit")
    
def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug=product_slug)
    form = FeedbackForm()
    reviews = Feedback.objects.filter(product=product)
    if request.method == 'GET':
        return render(request, "products/product.html", {
            'product': product,
            'form':form,
            'reviews':reviews,
        } )
    
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(
                name = form.cleaned_data['name'],
                rating = form.cleaned_data['rating'],
                product = product,
                text = form.cleaned_data['text'],
            )
            feedback.save()
            # print(form.cleaned_data)
            messages.success(request, "Your feedback was submitted sucessful")
            form = FeedbackForm()

        return render(request, "products/product.html", {
            'product': product,
            'form':form,
            'reviews':reviews,
        } )
    