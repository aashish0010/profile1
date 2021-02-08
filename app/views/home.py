from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        return render(request,'home.html')
    def post(self , request):
        return render(request,'home.html')

class Contact(View):
    def get(self, request):
        return render(request,'contact.html')
    def post(self, request):
        return render(request, 'contact.html')

class Profile(View):
    def get(self,request):
        return render(request,'profile.html')
    def post(self, request):
        return render(request, 'profile.html')