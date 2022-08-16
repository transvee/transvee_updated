from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import NewUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm


@csrf_exempt
def login_user(request):
	if request.method == "POST":
		email = request.POST.get("email")
		password = request.POST.get("password")
		user = authenticate(request,email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home-1')
		else:
			messages.success(request, ('There was an Error Logging in/ Incorrect details, Try Again!!!'))
			return redirect('login')
	else:
		return render(request, 'authenticate/login.html',{})

def logout_user(request):
	logout(request)
	messages.success(request, ('You Were Logged Out!!!'))
	return redirect('home')



@csrf_exempt
def register_user(request):


	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Registration successful." )
			return redirect("home-1")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="authenticate/register_user.html", context={"form":form})

	


