from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from users.forms import UserCreationForm
# users/views.py

from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('chat_room')  # Используйте имя URL вашей страницы чата


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)