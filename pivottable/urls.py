from django.conf.urls import url
from django.urls.conf import path
from pivottable import views

# SET THE NAMESPACE!
app_name = 'pivottable'

# Be careful setting the name to just /login 
# use userlogin instead!

urlpatterns=[
    path('',views.home, name='home'),
    
]