from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

class PostsListView(ListView):
	"""docstring for PostListView"""
	model = Post

class PostDetailView(DetailView):
	model = Post


