from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from bookmark.models import Bookmark


class BookmarkList(ListView):  # bookmark_list.html
    model = Bookmark


class BookmarkCreateView(CreateView):  # bookmark-form.html
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'  # bookmark_create.html
    success_url = reverse_lazy('bookmark:list')
