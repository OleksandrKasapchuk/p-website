from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic import View, ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(TemplateView):
	template_name = 'mainapp/index.html'


class GalleryView(ListView):
	model = Post
	template_name = 'mainapp/gallery.html'
	context_object_name = "posts"