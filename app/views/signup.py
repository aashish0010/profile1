from django.shortcuts import render, redirect
from django.views import View
from app.models.customer import Customer
from django.contrib.auth.hashers import make_password


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')



    def post(self, request):
        postdata = request.POST
        fullname = postdata.get('fullname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        image = postdata.get('image')
        value = {
            'fullname': fullname,
            'phone': phone,
            'email': email,
            'password': password,
            'image': image,
        }
        error_message = None
        customer = Customer(fullname=fullname, email=email, password=password, phone=phone, image=image)
        error_message = self.Validation(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect("login")
        else:
            data = {
                'error': error_message,
                'value': value,
            }

        return render(request, 'signup.html', data)

    def Validation(self, customer):
        error_message = None

        if not customer.fullname:
            error_message = 'enter First name'
        elif len(customer.fullname) < 4:
            error_message = 'please enter more than 4'
        elif not customer.phone:
            error_message = 'enter phone number'
        elif not customer.email:
            error_message = 'enter email'
        elif not customer.password:
            error_message = 'enter password'
        elif not len(customer.password):
            error_message = 'enter password'

        return error_message
