from django.urls import path
from . import views

app_name = "join"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('detail/<jpk>', views.detail, name="detail"),
    path('delete/<jpk>', views.delete, name="delete"),
    path('create/', views.create, name="create"),
    path('jlikey/<jpk>', views.jlikey, name="jlikey"),
    path('unjlikey/<jpk>', views.unjlikey, name="unjlikey")
]