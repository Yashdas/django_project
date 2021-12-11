from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Books, ContactUs
from .forms import StudentForm
from .forms import BookForm
from .forms import Student
import csv


from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    #return HttpResponse("<h1 align='center' style='margin-top:50px; color:#ea3e3e;'>Welcome to my first project in django</h1>")
    #return HttpResponse("<script>alert('Welcom to my first project in django');</script>")
    dict = {'name':'Yashobanta','id':15,'email':'yashdas11@gmail.com'}
    request.session['sname']='yashobanta das'
    return render(request,'Home/index.html',dict)

def aboutus(request):
    #name = request.session['sname']
    #return HttpResponse(name)
    form = StudentForm(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            print('Data save successfully')

    return render(request,'Home/aboutus.html',{'form':form})

def contact(request):
    if request.method == "POST":

        uname = request.POST['name']
        uemail = request.POST['email']
        ucomment = request.POST['comment']
        
        conData=ContactUs(name=uname,email=uemail,comment=ucomment)
        conData.save()
        print('Data save successfully')
    records = ContactUs.objects.all()
    d={'contact_record':records}
    
    return render(request,'Home/contact.html',d)

def add(request):
    result =5;
    return render(request,'Home/result.html',{'name':result})

def upload_book(request):
    
    if request.method == "POST":
        book_form = BookForm(request.POST,request.FILES)

        if book_form.is_valid():
            book_form.save()
            print('Data save successfully')
            return redirect('book_list')
    else:
        book_form = BookForm()

    return render(request,'Home/upload_book.html',{'book_form':book_form})

def book_list(request):
    records = Books.objects.all()
    d={'book_record':records}
    return render(request,'Home/book_list.html',d)

def delete_book(request,pk):
    if request.method == "POST":
        book_record = Books.objects.get(pk=pk)
        book_record.delete()

    return redirect('book_list')

def send_email(request):

    if request.method == "POST":
        subject = 'welcome to Django'
        message = request.POST['comment']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['dassubhadra1988@gmail.com']
        send_mail( subject, message, email_from, recipient_list,fail_silently=False )
    return render(request,'Home/send_email.html')

def csv_download(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student.csv"'
    st = Student.objects.all()
    writer = csv.writer(response)
    for s in st:
        writer.writerow([s.rno,s.name,s.email,s.mobile])
    return response

def get_pdf(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="student.csv"'
    st = Student.objects.all()
    writer = csv.writer(response)
    for s in st:
        writer.writerow([s.rno,s.name,s.email,s.mobile])
    return response
