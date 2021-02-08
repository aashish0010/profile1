from django.shortcuts import render ,redirect
from django.views import View
from app.models.customer import Customer
from django.contrib.auth.hashers import check_password



class Login(View):
    def get(self,request):
        return render(request,'login.html')


    def post(self,request):
        fullname = request.POST.get('fullname')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                request.session['fullname'] = customer.fullname


                return redirect('profile')
            else:
                error_message = 'password is invalid'

        else:
            error_message = 'Email is invalid...'
        return render(request,'login.html',{'error' : error_message})