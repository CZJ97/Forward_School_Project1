"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pivottable.views import home
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from welcome import views
# from analysis import views
from project1.settings import DEBUG, STATIC_URL, STATIC_DIR, MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^welcome/',include('welcome.urls')),
    url(r'^logout/$',views.user_logout, name='logout'),
    url(r'^pivottable/',include('pivottable.urls')),
    url(r'^analysis/',include('analysis.urls'))

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
