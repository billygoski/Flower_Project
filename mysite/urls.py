from django.urls import path

from mysite import views

urlpatterns = [
    path('', views.mysite, name='mysite'),
    path('flower/<slug:slug>', views.detail, name='detail'),
    path('tags/<slug:slug>', views.tag, name='tag'),
    path('create/flower', views.create, name='create'),
    path('edit/flower/<slug:sg>', views.edit, name='edit'),
    path('delete/flower/<int:pk>', views.delete, name='delete'),
]