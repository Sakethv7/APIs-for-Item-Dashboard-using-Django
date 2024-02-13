from django.urls import path
from api import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('test_token', views.test_token, name='test_token'),
    path('dataget/', views.dataget, name='dataget'),
    # path('', views.ApiOverview, name='home'),
    path('create', views.add_items, name='create'),
    path('getAllItems/', views.get_all_items, name='get_all_items'),
    path('getAllItemsbyParameters/', views.get_all_itemsbyParameters, name='get_all_items_by_parameters')
]
