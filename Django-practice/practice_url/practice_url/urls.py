from django.contrib import admin
from django.urls import path, include
from practice import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first),
    path('second',views.second),
    path('product/',include('product.urls')),
    path('board/',include('board.urls')),
]
