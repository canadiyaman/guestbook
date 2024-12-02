from django.db.models import Subquery, OuterRef, Value, CharField, Count
from django.db.models.functions import Concat
from rest_framework import generics


from .serializers import EntrySerializer, UserSerializer
from .models import Entry, User
from .pagination import CustomEntryPagination


__all__ = ["EntryView", "UserView"]


class EntryView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all().order_by("-created_date")
    pagination_class = CustomEntryPagination


class UserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.annotate(
        total_entry_count=Count("entry"),
        last_entry=Subquery(
            Entry.objects.filter(user=OuterRef("pk"))
            .values("subject", "message")
            .annotate(
                combined=Concat(
                    "subject", Value(" | "), "message", output_field=CharField()
                )
            )[:1]
            .values("combined")
        ),
    )
