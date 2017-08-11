from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from models import Album, Song
from .forms import UserForm
from django.utils.crypto import get_random_string

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):

        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class CreateAlbum(CreateView):
	model = Album
	fields = ['artist','album_title','genre','album_logo']

	def form_valid(self, form):
		album = form.save(commit=False)
		unique_id = get_random_string(length=32)
		unique_id = unique_id+str(album.pk)
		album.artist = self.request.POST.get('artist')
		album.album_title = self.request.POST.get('album_title')
		album.genre = self.request.POST.get('genre')
		album.u_id = unique_id
		album.save()

		return redirect('music:index')

class CreateSong(CreateView):
	model = Song
	template_name = 'music/songadd_form.html'
	fields = ['song_title','file_type','is_favorite']


class SongDelete(DeleteView):
	model = Song
	success_url = reverse_lazy("music:index")



class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist','album_title','genre','album_logo']


class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy("music:index")

class UserFormView(View):
	form_class = UserForm
	template_name =  'music/registration_form.html'

	#display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, { 'form': form } )

	#process form data
	def post(self, request):
		form  = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit = False)

			#clean (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#return User if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:

					login(request, user)

					return redirect('music:index')

		return render(request, self.template_name, { 'form': form } )



