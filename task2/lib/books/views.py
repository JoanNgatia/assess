from django.shortcuts import render

# Create your views here.
from models import Book


def get_books(request):
    try:
        q = request.GET['name']
        books = Book.objects.filter(title=q)
    except KeyError:
        books = Book.objects.all()
    return render(request, 'list.html', {'books': books})
