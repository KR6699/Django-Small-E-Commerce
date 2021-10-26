from django.urls import path
from store.middlewares.auth import auth_middleware
from .views import *
urlpatterns = [
    path('',index),
    path('signup/',signup,name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('cart/',Cart.as_view(),name='cart'),
    path('check-out',CheckOut.as_view(),name='check-out'),
    path('orders', auth_middleware(OrderView.as_view()),name='orders'),
]