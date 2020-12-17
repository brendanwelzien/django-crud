from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import blog
from django.urls import reverse_lazy

class BlogListView(ListView): # requirements --> needs to know its template, model
    template_name = 'blog-list.html'
    model = blog
    
class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = blog

class BlogCreateView(CreateView):
    template_name = 'blog-create.html'
    model = blog
    fields = ['name', 'author', 'buyer']
    success_url = reverse_lazy('blog_list')

class BlogUpdateView(UpdateView):
    template_name = 'blog-update.html'
    model = blog
    success_url = reverse_lazy('blog_list')

class BlogDeleteView(DeleteView):
    template_name = 'blog-delete.html'
    model = blog
    success_url = reverse_lazy('blog_list')