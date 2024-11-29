from rest_framework import serializers

from .models import Entry, User

__all__ = ["UserSerializer", "EntrySerializer"]


class UserSerializer(serializers.ModelSerializer):
    last_entry = serializers.SerializerMethodField()
    total_entry_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = ["name", "last_entry", "total_entry_count"]

    def get_last_entry(self, obj):
        return getattr(obj, "last_entry", None)


class EntrySerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(write_only=True)

    class Meta:
        model = Entry
        fields = ["user_name", "user", "subject", "message"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        user_name = validated_data.pop("user_name")
        user, created = User.objects.get_or_create(name=user_name)
        entry = Entry.objects.create(user=user, **validated_data)
        return entry
