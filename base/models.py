from django.db import models
from django.utils.text import slugify
# Create your models here.


class Project(models.Model):
    photo = models.ImageField(upload_to='post_images/', default='default.jpg', verbose_name='Project photo')
    title = models.CharField(max_length=50, verbose_name="Project name", help_text="maximum 50 characters")
    description = models.CharField(max_length=255, verbose_name="Description", help_text="maximum 255 characters", null=True, blank=True)
    url = models.URLField(max_length=255, verbose_name="Link to project", help_text="Project url or link", null=True, blank=True)
    slug = models.SlugField(max_length=255, verbose_name='URL', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'projects'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
