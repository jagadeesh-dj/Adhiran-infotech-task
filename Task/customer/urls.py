from django.urls import path
from customer import views
urlpatterns=[
    path('',views.Customer_list),
    path('customers/<int:pk>/',views.Customers),
    path('products/<int:pk>/',views.Product),
    path('productview/',views.Product_view),
    path('order/<int:pk>/',views.Orders),
    path('orderview/',views.Order_view),


]