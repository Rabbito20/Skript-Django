from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required, permission_required
#from .models import Article
#from .forms import ArticleForm
from django.http import HttpResponse

#   apk views

#Svi postovi
class HomeView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'apk/index.html'
    context_object_name = 'blogz'   # apk_apk - not sure
    #   Sortiramo - prvo ide najskorijeo bjavljen post
    ordering = ['-created_at']
    paginate_by = 3

#Single post
class EntryView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'apk/article_detail.html'

#Kreiranje posta
class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'apk/create_blog_view.html'
    fields = ['title', 'content']

    #   Validacija autora
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)