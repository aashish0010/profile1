from django.urls import path
from .views.signup import Signup
from .views.login import Login
from .views.home import Home ,Contact ,Profile
from .views.logout import Logout

urlpatterns = [
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('',Home.as_view(), name = 'home'),
    path('contact', Contact.as_view(), name = 'contact'),
    path('logout',Logout.as_view(),name = 'logout'),
    path('profile',Profile.as_view() , name ='profile')

]
