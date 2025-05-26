from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Blog
from .forms import BlogForm
from .serializer import BlogSerializer


def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'index.html', context)


@login_required
def myblogs(request):
    blogs = Blog.objects.filter(author=request.user)
    context = {
        'blogs': blogs
    }
    return render(request, 'myblogs.html', context)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'edit.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        blog = self.get_object()
        return self.request.user == blog.author


# API tomoni
class CreateListBlog(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class UpDelRetBlog(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



