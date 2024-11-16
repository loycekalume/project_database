from django.http import HttpResponse
from django.shortcuts import render, redirect

from sacco.models import Customer, Deposit


# Create your views here.

def test(request):
    # save customer
    # c1 = Customer(first_name='John', last_name='Smith',email='john@gmail.com',dob='2003-01-23',gender='Male',weight=63)
    # c1.save()
    #
    # c1 = Customer(first_name='James', last_name='Smith', email='james@gmail.com', dob='2003-01-23', gender='Male',
    #               weight=63)
    # c1.save()
    customer_count = Customer.objects.count()

    c1 = Customer.objects.get(id=1)
    print(c1)
    d1 = Deposit(amount=1000, status=True, customer=c1)
    d1.save()
    deposit_count = Deposit.objects.count()
    return HttpResponse(f"Ok,Done,we have {customer_count} customers and {deposit_count} deposits")


def customers(request):
    data = Customer.objects.all()  # select * from customers
    return render(request, "customers.html", {"customers":data})


def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect('customers')