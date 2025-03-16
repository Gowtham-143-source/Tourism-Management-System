from django.urls import path
from .views import book, book_list, view_booking, payment, refund

urlpatterns = [
    path('book/', book, name='book'),
    path('booklist/', book_list, name='booklist'),
    path('view/', view_booking, name='view_booking'),
    path('payment/', payment, name='payment'),
    path('refund/', refund, name='refund'),
]
