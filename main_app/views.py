from curses.ascii import HT
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Art

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def art_gallery(request):
    art = Art.objects.filter(user=request.user)
    return render(request, 'art/index.html',
    {'art': art})

@login_required
def art_detail(request, art_id):
    art = Art.objects.get(id=art_id)
    return render(request, 'art/detail.html', {'art': art})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# class views
class ArtCreate(LoginRequiredMixin, CreateView):
    model = Art
    fields = ['name', 'date', 'mediums', 'description', 'img']
    success_url = '/art/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    # def get_form(self, form_class):
    #     form = super(ArtCreate, self).get_form(form_class)
    #     form.fields['date_field'].eidget.attrs.update({'class': 'datepicker'})
    #     return form
class ArtUpdate(LoginRequiredMixin, UpdateView):
    model = Art
    fields = ['name', 'date', 'mediums', 'description', 'img']
class ArtDelete(LoginRequiredMixin, DeleteView):
    model = Art
    success_url = '/art_gallery/'