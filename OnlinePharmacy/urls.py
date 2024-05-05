"""
URL configuration for OnlinePharmacy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('product.urls')),
    path('admin/', admin.site.urls),
    path('core/',include('product.urls')),
    path('accounts/', include('login.urls')),
    path('signup/', include('signup.urls')),  
    path('forgot_password/', include('forgot_password.urls')),
    path('admin_tasks/', include('admin_tasks.urls')),
    path('add_products/', include('add_products.urls')),
    path('delete_products/',include('delete_products.urls')),
    path('update_price/',include('update_price.urls')),
    path('feedback/',include('feedback.urls')),
    path('login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('payment/',include('payment.urls')),
]