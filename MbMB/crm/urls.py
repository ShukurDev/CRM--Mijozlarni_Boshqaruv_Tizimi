from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerview, name='register'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),

    path('', views.dashboard, name='home'),
    path('user', views.userview, name='user'),


    path('product/', views.product, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('account/',views.accountSettings,name='account'),

    path('create_order/<str:pk>/', views.createorder, name='create_order'),
    path('update_order/<str:pk>/', views.updateorder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteorder, name='delete_order'),

    path('create_product/',views.productform,name='product_form'),

    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


