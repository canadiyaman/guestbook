from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.name}"


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return f"{self.subject}, User ID: {self.user_id}"
