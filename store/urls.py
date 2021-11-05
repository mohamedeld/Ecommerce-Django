from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='product_store'),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_detail'),
]