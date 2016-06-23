from django.shortcuts import render

# Create your views here.
from models import Book


def get_books(request):
    try:
        q = request.GET['name']
        books = Book.objects.filter(title=q)
    except KeyError:
        try:
            t = int(request.GET['limit'])
            books = Book.objects.all()[:t]
        except KeyError:
            books = Book.objects.all()
    return render(request, 'list.html', {'books': books})
