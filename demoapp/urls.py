from typing import ValuesView
from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
    path('add/',views.add,name='add'),
    path('upload_book/',views.upload_book,name='upload_book'),
    path('book_list/',views.book_list,name='book_list'),
    path('send_email/',views.send_email,name='send_email'),
    path('delete_book/<int:pk>',views.delete_book,name='delete_book'),

    path('csv_download/',views.csv_download,name='csv_download'),
    path('get_pdf/',views.get_pdf,name='get_pdf'),
]
