from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home, name='home'),
    path('found/', views.report_found, name='report_found'),
    path('lost/', views.report_lost, name='report_lost'),
    path('item-submitted/', views.item_submitted, name='item_submitted'),
    #path('match-result/', views.match_result, name='match_result'),  # Optional: If you want to explicitly have this URL
]