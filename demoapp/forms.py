from django.db import models
from django.forms import ModelForm, fields
from .models import Books, Student

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class BookForm(ModelForm):
    class Meta:
        model=Books
        fields='__all__'