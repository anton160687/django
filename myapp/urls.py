from django.urls import path
from . import views
from .views import HelloView, year_post, MonthPost, post_detail, user_list, order_list, add_order, order_success


urlpatterns = [
     path('', user_list, name='index'),
     path('about/', views.about, name='about'),
     path('orders/', order_list, name='orders'),
     path('add-order/', add_order, name='add_order'),
     path('order-success/', order_success, name='order_success'),
     path('hello2/', HelloView.as_view(), name='hello2'),
     path('posts/<int:year>/', year_post, name='year_post'),
     path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
     path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
]

