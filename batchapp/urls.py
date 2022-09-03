from django.urls import path

from batchapp import views

urlpatterns = [

    path('xyz/',views.insert),
    path('xyz/',views.insert),
    path('xyz/', views.insert)
]
