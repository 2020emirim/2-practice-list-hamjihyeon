from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from bookmark.models import Bookmark


class BookmarkList(ListView):  # bookmark_list.html
    model = Bookmark


class BookmarkCreateView(CreateView):  # bookmark-form.html
    model = Bookmark
    fields = ['site_name', 'url']  # <form>태그엔 fields가 들어가야됨.
    template_name_suffix = '_create'  # bookmark_create.html
    success_url = reverse_lazy('bookmark:list')  # DB에 저장된 후 늦게 호출해라.


class BookmarkDetailView(DetailView):
    model = Bookmark
