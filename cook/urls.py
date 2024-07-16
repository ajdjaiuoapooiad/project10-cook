from django.urls import path
from . import views

app_name='cook'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('upload/',views.CreateView.as_view(),name='upload'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
]