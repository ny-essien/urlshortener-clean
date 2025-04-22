from django.db import models
from django.contrib.auth.models import User
import string
import random

def generate_short_code():
    """Generate a random 6-character alphanumeric code."""
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(characters, k=6))
        if not Link.objects.filter(short_code=code).exists():
            return code

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

    def get_short_url(self, request):
        """Return the full short URL for this link."""
        return request.build_absolute_uri(f'/{self.short_code}/')
