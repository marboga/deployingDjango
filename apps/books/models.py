from __future__ import unicode_literals
from django.db import models

class BookManager(models.Manager):
	def newBook(self, info):
		print info
		if info['curAuthor'] == 'N/A':
			newAuthorid = Author.objects.create(name=info['newAuthor'])
			newBookid = Book.objects.create(title=info['title'], fk_author=newAuthorid)
			newReview = Review.objects.create(review=info['review'], rating=info['rating'], fk_book=newBookid, fk_user=info['user'][0])
		else:
			curAuthorid = Author.objects.filter(id=info['curAuthor'])
			print curAuthorid[0]
			newBookid = Book.objects.create(title=info['title'], fk_author=curAuthorid[0])
			newReview = Review.objects.create(review=info['review'], rating=info['rating'], fk_book=newBookid, fk_user=info['user'][0])
		return
	pass



class Author(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
	title = models.CharField(max_length=255)
	fk_author = models.ForeignKey(Author)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	book_manager = BookManager()
	objects = models.Manager()

class Review(models.Model):
	review = models.CharField(max_length=255)
	rating = models.CharField(max_length=1)
	fk_book = models.ForeignKey(Book)
	fk_user = models.ForeignKey('logreg.User')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)