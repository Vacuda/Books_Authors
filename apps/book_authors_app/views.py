from django.shortcuts import render, redirect, HttpResponse
from .models import Book
from .models import Author

####Books###################################################

def books_main(request):
    b=Book.objects.all()
    context = {
        "books": b,
    }
    return render(request,'book_authors_app/books_main.html', context)

def add_book(request):
    Book.objects.create(title=request.POST['title_add'], desc=request.POST['desc_add'])
    return redirect('/books_main')

def delete_book(request):
    x=Book.objects.get(id=request.POST['id_incoming'])
    x.delete()
    return redirect('/books_main')

def view_book(request):
    return redirect(f'/books_view/{request.POST["id_incoming"]}')


def books_view(request, id):
    x=Book.objects.get(id=id)
    y=Book.objects.get(id=id).authors.all()
    z=Author.objects.all()
    # For every author in this book's authors, 
    # excludes them from all authors(z), by getting the id of the current author
    # to get a list of authors not on list
    for i in y:
        z=z.exclude(id=i.id)
    context = {
        "book": x,
        "authors_on": y,
        "authors_off": z,
    }
    return render(request,'book_authors_app/books_view.html', context)

def link_author(request):
    Book.objects.get(id=request.POST['current_id']).authors.add(request.POST['id_incoming'])
    return redirect(f'/books_view/{request.POST["current_id"]}')

def remove_author(request):
    Book.objects.get(id=request.POST['current_id']).authors.remove(request.POST['id_incoming'])
    return redirect(f'/books_view/{request.POST["current_id"]}')


####Authors###################################################

def authors_main(request):
    a=Author.objects.all()
    context = {
        "authors": a,
    }
    return render(request,'book_authors_app/authors_main.html', context)

def add_author(request):
    Author.objects.create(first_name=request.POST['first_name_add'], last_name=request.POST['last_name_add'], notes=request.POST['notes_add'])
    return redirect('/authors_main')

def delete_author(request):
    x=Author.objects.get(id=request.POST['id_incoming'])
    x.delete()
    return redirect('/authors_main')
def view_author(request):
    return redirect(f'/authors_view/{request.POST["id_incoming"]}')


def authors_view(request, id):
    x=Author.objects.get(id=id)
    y=Author.objects.get(id=id).books.all()
    z=Book.objects.all()
    # For every book in this author's books, 
    # excludes them from all books(z), by getting the id of the current book
    # to get a list of books not on list
    for i in y:
        z=z.exclude(id=i.id)
    context = {
        "author": x,
        "books_on": y,
        "books_off": z,
    }
    return render(request,'book_authors_app/authors_view.html', context)

def link_book(request):
    Author.objects.get(id=request.POST['current_id']).books.add(request.POST['id_incoming'])
    return redirect(f'/authors_view/{request.POST["current_id"]}')

def remove_book(request):
    Author.objects.get(id=request.POST['current_id']).books.remove(request.POST['id_incoming'])
    return redirect(f'/authors_view/{request.POST["current_id"]}')