from django.urls import include, path

urlpatterns = [
    path('product/', include('products.urls')),
    path('user/', include('users.urls')),
    path('order/', include('orders.urls')),
    path('company/', include('company.urls')),
]
