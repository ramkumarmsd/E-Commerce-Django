"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from shopworld import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.trending,name='trend'),
    path('home', views.home, name='home'),
    path('products/<str:pname>',views.products,name='products'),
    path('productview/<str:cname>/<str:name>',views.productview,name='productview'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('carts',views.carts,name='carts'),
    path('cart_page',views.cart_page,name='cart_page'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('favourites',views.favourites,name='favourites'),
    path('favourite_page',views.favourite_page,name='favourite_page'),
    path('remove_fav/<str:fid>',views.remove_fav,name='remove_fav'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)