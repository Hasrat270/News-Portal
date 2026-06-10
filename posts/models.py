from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('technology', 'Technology'),
        ('business', 'Business'),
        ('entertainment', 'Entertainment'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='technology')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    def save(self, *args, **kwargs):
        # First save the model instance
        super().save(*args, **kwargs)
        
        # If an image exists, optimize and resize it
        if self.image:
            try:
                img_path = self.image.path
                if os.path.exists(img_path):
                    img = Image.open(img_path)
                    
                    # Define maximum width for optimization
                    max_width = 800
                    if img.width > max_width:
                        ratio = max_width / float(img.width)
                        new_height = int(float(img.height) * float(ratio))
                        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                        img.save(img_path, quality=85, optimize=True)
            except Exception as e:
                # Fallback in case of PIL errors to prevent database transaction fail
                pass

