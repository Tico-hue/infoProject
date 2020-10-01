from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Usuario
from ..productos.models import Producto
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, f'Tu cuenta ha sido creada, ya podes ingresar')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
		if p_form.is_valid():
			p_form.save()
			messages.success(request, f'Tu cuenta ha sido actualizada')
			return  get_user_profile(request,request.user)
			
	else:
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {
		'p_form': p_form
	}
	return render(request, 'usuarios/profile.html',context)


def get_user_profile(request, username):
	user = Usuario.objects.get(username=username)
	context = {}
	todos = Producto.objects.filter(usuario_id__id__icontains=user.id)
	context['productos'] = todos
	return render(request, 'usuarios/user_profile.html', {'profile_user':user,'productos':todos})
