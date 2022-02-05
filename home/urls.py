from django.urls import path

from . import views

urlpatterns = [
   
    path('', views.homeIndex, name='homeIndex'),
    path('config/', views.stripe_config, name='stripe_config'),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessProcess, name='SuccessProcess'), # new
    path('cancelled/', views.CancleProcess, name='CancleProcess'), # new
]