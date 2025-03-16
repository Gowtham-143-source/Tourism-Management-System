from django.urls import path
from . import views 

urlpatterns = [
    path('packages/', views.packages, name='packages'),  # Homepage with all packages
    path('intern/', views.intern1, name='intern'),  # International tour page
    path('universe/', views.universe1, name='universe'),  # Universal tour page
    path('family/', views.family1, name='family'),  # Family tour page
    path('table/', views.table, name='table'),  # Tourism package details table
    path('form/', views.booking, name='form'),  # Booking form page
]
