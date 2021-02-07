from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)

from .models import *


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class AdministrationListView(PostListView):
    model = Administration
    template_name = 'administration/index.html'


class AdministrationDetailView(PostDetailView):
    model = Administration
    template_name = 'administration/administration_detail.html'


class TeacherListView(PostListView):
    model = Teacher
    template_name = 'teacher/index.html'


class TeacherDetailView(PostDetailView):
    model = Teacher
    template_name = 'teacher/teacher_detail.html'


class OurPrideListView(PostListView):
    model = OurPride
    template_name = 'our_pride/index.html'


class OurPrideDetailView(PostDetailView):
    model = OurPride
    template_name = 'our_pride/our_pride_detail.html'


class HonourListView(PostListView):
    model = Honour
    template_name = 'honour/index.html'


class HonourDetailView(PostDetailView):
    model = Honour
    template_name = 'honour/honour_detail.html'


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
