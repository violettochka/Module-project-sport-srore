from django.shortcuts import render, HttpResponseRedirect
from products.models import Products, Purchase, Return
from products.forms import AddProductsForm, ChangeProductsForm, BuyProductsForm, ReturnProductsForm
from django.urls import reverse
from users.models import User
from django.contrib import messages

def main(request):
    context = {'title': 'Главная страница'}
    return render(request, 'products/main.html', context)


def catalog(request):
    current_user = request.user
    initial_values = {
        'user': current_user,
    }
    form = BuyProductsForm(initial=initial_values)
    products = Products.objects.all()
    context = {
        'title': 'Каталог',
        'products': products,
        'form' : form,
        'initial_values': initial_values
    }
    return render(request, 'products/catalog.html', context)


def purchased(request, product_id):
    product = Products.objects.get(id=product_id)
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = BuyProductsForm(data=request.POST)
        if form.is_valid():
            product.quantity -= int(request.POST['count'])
            product.save()
            if current_user.wallet >= product.price * int(request.POST['count']):
                current_user.wallet -= product.price * int(request.POST['count'])
                current_user.save()
                form.save()
                messages.success(request, 'Товар был успешн куплен')
                return render(request, 'products/main.html')
            else:
                messages.error(request, "У вас недостаточно денег на счету!")
                return render(request, 'products/main.html')
    else:
        form = BuyProductsForm()
    
    context = {'product': product,  'form': form}
    return render(request, 'products/catalog.html', context)


def made_purchased(request):
    purchases = Purchase.objects.filter(user=request.user)
    form = ReturnProductsForm()
    context = {'purchases': purchases, 'form': form}
    return render(request, 'products/made_purchased.html', context)


def returned(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    if request.method == 'POST':
        form = ReturnProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = ReturnProductsForm()
    context = {'form': form, 'purchase': purchase}
    return render(request, 'products/made_purchased.html', context)




def add_product(request):
    if request.method == 'POST':
        form = AddProductsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AddProductsForm()
    context = {'form': form}
    return render(request, 'products/add_product.html', context)


def change_product(request, product_id):
    product = Products.objects.get(id=product_id)
    if request.method == 'POST':
        form = ChangeProductsForm(data=request.POST,  instance=product, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main'))
    else:
        form = ChangeProductsForm(instance=product)
    context = { 'title': 'Изменение товара',
                'product': product,
                'form': form,
                }
    return render(request, 'products/change_product.html', context)


def returned_list(request):
    returned_purchases = Return.objects.all()
    context = {'purchases': returned_purchases}
    return render(request, 'products/returned_list.html', context)

def submit(request, returned_id):
    returned_product = Return.objects.get(id=returned_id)
    purchase = Purchase.objects.get(product=returned_product.purchase.product)
    product = Products.objects.get(name=returned_product.purchase.product.name)
    user = User.objects.get(username=returned_product.purchase.user.username)
    if request.method == 'POST':
        product.quantity += returned_product.purchase.count
        product.save()
        user.wallet += product.price * purchase.count
        user.save()
        returned_product.delete()
        purchase.delete()

        return render(request, 'products/main.html')


def reject(request, returned_id):
    returned_product = Return.objects.get(id=returned_id)
    if request.method == 'POST':
        returned_product.delete()
        return render(request, 'products/main.html')

