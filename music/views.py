from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from models import Album, Song
from .forms import UserForm, SongAddForm

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

class SongView(View):
	form_class = SongAddForm
	template_name = 'music/songadd_form.html'

	def get(self, request, pk):
		form = self.form_class(None)
		return render(request, self.template_name, { 'form': form, 'album_id': pk })
	
	def post(self, request, pk):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			song = form.save(commit=False)
			song.album = Album.objects.get(pk=pk)
			song.save()

			return redirect('music:detail', pk)

	 	return render(request, self.template_name, { 'form': form, 'album_id': pk })

class SongDelete(DeleteView):
	model = Song
	success_url = reverse_lazy("music:index")

class SongEdit()

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



