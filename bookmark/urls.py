from django.urls import path

from bookmark.views import BookmarkList

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkList.as_view(), name='list'),  # {% url bookmark:list %}

]
