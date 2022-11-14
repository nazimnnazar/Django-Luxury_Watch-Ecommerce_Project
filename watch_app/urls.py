from django.urls import path
from . import views

urlpatterns =[
    #Cart  
    path('cart_Details/', views.cartdetails, name='cart_Details'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min/<int:product_id>/', views.min_cart, name='mincart'),
    path('remove/<int:product_id>/', views.remove, name='remove'),



    path('',views.index,name='frontpage'),
    
    path('<slug:c_slug>/',views.product,name='product'),
    path('<slug:c_slug>/<slug:product_slug>',views.product_views,name='productviews'),
    path('login',views.Login,name='Login'),
   
    path('register',views.register,name='register'),
    path('product',views.product,name='product'),

    # path('pro',views.pro,name='pro'),
    path('contact',views.contact,name='contact'),
   


]