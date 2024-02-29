from django.contrib import admin
from django.urls import path
from liste import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test, name='test'),
    path('prestation/add/', views.prestation_create, name='prestation-create'),
    path('devis/add/', views.devis_create, name='devis-create'),
]
