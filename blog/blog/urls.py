from django import views
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('list/', views.PostList.as_view(), name='list'),
    path('detail/<int:pk>', views.PostDetail.as_view(), name='detail'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='update'),
]
