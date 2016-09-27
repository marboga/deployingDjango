from django.shortcuts import render, redirect
from django.contrib import sessions
from django.urls import reverse
from .models import Author, Book, Review
from .forms import BookForm
from ..logreg.models import User

def index(request):
	context = {
		'books': Book.objects.all(),
		'reviews': Review.objects.all().order_by('-id')[:3]
	}
	return render(request, 'books/main.html', context)
	pass

def newBook(request):
	bForm = BookForm(auto_id=True)
	context = {
		'authors': Author.objects.all(),
		'bookForm': bForm.as_table()
	}
	return render(request, 'books/newBook.html', context)
	pass


def addBook(request):
	book = {
	'title': request.POST['title'],
	'user': User.objects.filter(id=request.session['loggedUser']['id']),
	'curAuthor': request.POST['curAuthor'],
	'newAuthor': request.POST['newAuthor'],
	'review': request.POST['review'],
	'rating': request.POST['rating'],
	}
	Book.book_manager.newBook(book)
	# print book
	return redirect(reverse('book_index'))
	pass

def show(request, id):
	getBook = Book.objects.filter(id=id)
	context = {
		'book': getBook[0]
	}
	print context['book'].title
	return render(request, 'books/book.html', context)
	pass

def userBook(request, id):

	pass
