from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Make sure this is here

class FoundItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='found_items/', blank=True, null=True)
    date = models.DateField() # This already exists 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='unclaimed')
    submitted_at = models.DateTimeField(auto_now_add=True)  # Use default instead of auto_now_add

    def _str_(self):
        return self.item_name
 
class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()  # This already exists
    submitted_at = models.DateTimeField(auto_now_add=True)
