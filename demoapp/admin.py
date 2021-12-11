from django.contrib import admin

from .models import Register, contact,Student,ContactUs,Books

# Register your models here.
admin.site.register(contact)
admin.site.register(Student)
admin.site.register(ContactUs)
admin.site.register(Books)
admin.site.register(Register)
