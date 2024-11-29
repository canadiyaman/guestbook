from django.urls import path

from core.views import EntryView, UserView

urlpatterns = [
    path("api/entries", EntryView.as_view(), name="entries"),
    path("api/users", UserView.as_view(), name="users"),
]
