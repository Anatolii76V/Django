from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order


def create_client(request):
    if request.method == 'POST':
        Client.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            address=request.POST['address'],
            registration_date=request.POST['registration_date']
        )
        return redirect('client_list')
    return render(request, 'create_client_form.html')


def create_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            added_date=request.POST['added_date']
        )
        return redirect('product_list')  # Перенаправление на список товаров
    return render(request, 'create_product_form.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def create_order(request):
    if request.method == 'POST':
        client_id = request.POST['client_id']
        product_ids = request.POST.getlist('product_ids')
        total_amount = request.POST['total_amount']
        order_date = request.POST['order_date']

        client = get_object_or_404(Client, pk=client_id)
        products = Product.objects.filter(pk__in=product_ids)

        order = Order.objects.create(
            client=client,
            total_amount=total_amount,
            order_date=order_date
        )
        order.products.set(products)
        return redirect('order_list')  # Перенаправление на список заказов

    clients = Client.objects.all()
    products = Product.objects.all()
    return render(request, 'create_order_form.html', {'clients': clients, 'products': products})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})
