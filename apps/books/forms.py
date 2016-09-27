from django import forms
from .models import Author

def getAuthorList():
	authList = [('N/A', 'Select Author')]
	authors = Author.objects.all()
	for author in authors:
		authList.append((author.id, author.name))
	print authList
	return authList

ratings = [
	(1,"1"),
	(2, "2"),
	(3, "3"),
	(4, "4"),
	(5, "5"),
]

class BookForm(forms.Form):
	title = forms.CharField(label='Book Title', required=True)
	curAuthor = forms.ChoiceField(label='Select a Current Author', choices=getAuthorList())
	newAuthor = forms.CharField(label='Or Add a new Authro', required=False)
	review = forms.CharField(widget=forms.Textarea, label='Review')
	rating = forms.ChoiceField(label='Rating', choices=ratings)

class ReviewForm(forms.Form):
	review = forms.CharField(widget=forms.Textarea, label='Review')
	rating = forms.ChoiceField(label='Rating', choices=ratings)