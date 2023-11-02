from django.urls import path, include

urlpatterns = [
    path('product/', include('products.urls')),
    path('user/', include('users.urls')),
    path('order/', include('orders.urls')),
    path('company/', include('company.urls')),
]
