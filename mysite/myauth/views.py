from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView,  UpdateView
from .models import Profile
from .forms import ProfileForm
from django import forms


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('myauth:login')


class MainView(TemplateView):
    model = Profile
    template_name = "myauth/main.html"


class CalculatorView(TemplateView):
    template_name = "myauth/calculator.html"


def registration(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = ProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("Зашел")
            form1.save()
            form2.save()
            # получаем имя пользователя и пароль из формы
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password1')
            name = form2.cleaned_data.get('name')
            surname = form2.cleaned_data.get('surname')
            middle_name = form2.cleaned_data.get('middle_name')
            email = form2.cleaned_data.get('email')
            organization = form2.cleaned_data.get('organization')
            inn = form2.cleaned_data.get('inn')
            site = form2.cleaned_data.get('site')
            branch = form2.cleaned_data.get('branch')
            country = form2.cleaned_data.get('country')
            city = form2.cleaned_data.get('city')
            position = form2.cleaned_data.get('position')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            Profile.objects.create(user=request.user, name=name, surname=surname, middle_name=middle_name,
                                   email=email, organization=organization, inn=inn, site=site, branch=branch,
                                   country=country, city=city, position=position)
            return render(request, 'myauth/main.html')
    else:
        form1 = UserCreationForm()
        form2 = ProfileForm()
    return render(request, 'myauth/register.html', {'form1': form1, 'form2': form2})


class ProfileDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        profile = Profile.objects.get(user=request.user)
        context = {
            "profile": profile
        }
        return render(request, 'myauth/profile.html', context=context)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm

    def form_valid(self, form: forms.Form):
        if form.is_valid():
            return super(ProfileUpdateView, self).form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self):
        return reverse('myauth:profile', kwargs={'pk': self.object.id})