from django.shortcuts import render, redirect
from django.contrib import messages, sessions
from django.urls import reverse
from .models import User
# Create your views here.

def index(request):
	return render(request, 'logreg/index.html')

def process(request):
	if request.POST['action'] == 'Register':
		user_info = {
			'fname': request.POST['fname'],
			'lname': request.POST['lname'],
			'email': request.POST['email'],
			'password': request.POST['password'],
			'confirmpass': request.POST['confirmpass']
		}
		newUser = User.user_manager.register(user_info)
		if newUser['success'] == False:
			for key in newUser:
				messages.error(request, message = newUser[key], extra_tags=key)
			return redirect(reverse('log_index'))
		elif newUser['success'] == True:
			messages.success(request, "Registration Successfull, Please Log In", extra_tags='login')
			return redirect(reverse('log_index'))
	elif request.POST['action'] == 'Login':
		user_info = {
			'email': request.POST['email'],
			'password': request.POST['password'],
		}
		curUser = User.user_manager.login(user_info)
		if curUser['success'] == False:
			messages.error(request, "E-Mail or Password are incorrect", extra_tags='emailpass')
			return redirect(reverse('log_index'))
		elif curUser['success'] == True:
			request.session['loggedUser'] = {
				'fname': curUser['user'].first_name,
				'lname': curUser['user'].last_name,
				'id': curUser['user'].id
			}
			print request.session['loggedUser']
			return redirect(reverse('book_index'))
		pass
		
def logout(request):
	request.session.clear()
	return redirect(reverse('log_index'))
	pass