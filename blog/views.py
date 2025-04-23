from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#         }
#     return render(request, 'blog/home.html', context)

# default template convention: <app_name>/<model>_<view>.html

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    template_name = 'blog/home.html'
    paginate_by = 10

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_post.html'
    paginate_by = 10
    
    def get_queryset(self):
        self.user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=self.user).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posted_user'] = User.objects.get(username=self.kwargs['username'])
        return context
        

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    # template convention: <app_name>/<model>_form.html
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # template convention: <app_name>/<model>_form.html
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # template convention: <app_name>/<model>_confirm_delete.html
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})