from django.shortcuts import render, redirect
from .models import Customer, Product, Order
from .forms import OrderForm, CreateUserForm, CustomerForm, ProductForm
from django.forms import inlineformset_factory
from .filter import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_user, admin_only
from django.contrib.auth.models import Group


# Create your views here.
@login_required(login_url='login')
@admin_only
def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_order = orders.count()

    delivered = orders.filter(status='Yetkazib berildi').count()
    pending = orders.filter(status='Yetkazib berilyapdi').count()
    context = {'customers': customers, 'orders': orders, 'total_orders': total_order, 'delivered': delivered,
               'pending': pending}

    return render(request, 'home.html', context)


@unauthenticated_user
def registerview(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Siz muvaffaqiyatli ro'yhatdan o'tdingiz" + username)
            return redirect('login')
    context = {'form': form}

    return render(request, 'register.html', context)


@unauthenticated_user
def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Sizning Username yoki Parolingiz xato")
    context = {}

    return render(request, 'login.html', context)


def logoutview(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def product(request):
    products = Product.objects.all()
    orders = Order.objects.all()

    total_order = orders.count()

    delivered = orders.filter(status='Yetkazib berildi').count()
    pending = orders.filter(status='Yetkazib berilyapdi').count()
    context = {
        'products': products, 'total_orders': total_order, 'delivered': delivered, 'pending': pending
    }
    return render(request, 'product.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    myfilter = OrderFilter(request.GET, queryset=orders)
    orders = myfilter.qs

    total_order = orders.count()

    delivered = orders.filter(status='Yetkazib berildi').count()
    pending = orders.filter(status='Yetkazib berilyapdi').count()
    context = {
        'customer': customer,
        'orders': orders,
        'total_orders': total_order,
        'delivered': delivered,
        'pending': pending,
        'myfilter': myfilter,
    }
    return render(request, 'customer.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'customer'])
def createorder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == "POST":
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}

    return render(request, 'order_form.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateorder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update_order.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def deleteorder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'order': order}

    return render(request, 'delete_order.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['customer'])
def userview(request):
    orders = request.user.customer.order_set.all()

    total_order = orders.count()
    delivered = orders.filter(status='Yetkazib berildi').count()
    pending = orders.filter(status='Yetkazib berilyapdi').count()

    context = {'orders': orders, 'total_orders': total_order,
               'delivered': delivered,
               'pending': pending, }

    return render(request, 'user.html', context)


def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form}

    return render(request, 'account_settings.html', context)


def productform(request):
    products = Product.objects.all()
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,products)
        if form.is_valid():
            form.save()
            return redirect('product')

    context = {
        'form':form
    }
    return render(request, 'product_form.html', context)
