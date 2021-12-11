from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.

class contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    comment=models.TextField()

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,blank = False,null = False)
    email=models.EmailField(max_length=255,blank = False,null = False)
    comment=models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    rno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank = False,null = False)
    email=models.EmailField(max_length=255,blank = False,null = False)
    mobile=models.CharField(max_length=255)
     
    def __str__(self):
        return self.name

class Books(models.Model):
    title=models.CharField(max_length=50,blank = False,null = False)
    author=models.CharField(max_length=50,blank = False,null = False)
    pdf=FileField(upload_to='pdfs/',blank=True,null=True)
    def __str__(self):
        return self.title

class Register(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255,blank = False,null = False)
    email=models.EmailField(max_length=255,blank = False,null = False)
    mobile=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    def __str__(self):
        return self.name


