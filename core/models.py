from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from ckeditor_uploader.fields import RichTextUploadingField

from core.custom_models import OrderField
# Create your models here.


User = get_user_model()
class Subject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = RichTextUploadingField()
    class Meta:
        ordering=['title',]
    
    def __str__(self):
        return self.title
    

class Course(models.Model):
    class DIFFICULTY_LEVEL(models.TextChoices):
        EASY = "Easy", 'Easy'
        MEDIUM = "Medium", 'Medium'
        HARD = "Hard", 'Hard'
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = RichTextUploadingField()
    preview = models.ImageField(upload_to="courses/preview", default="default/default_preview.jpg")
    level = models.CharField(max_length=6, choices=DIFFICULTY_LEVEL.choices, default=DIFFICULTY_LEVEL.EASY)
    duration = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f'#{self.order}. {self.title}'

class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="contents")
    contentText = RichTextUploadingField(null=True, blank=True)
    contentFile = models.FileField(upload_to="contents/files", null=True, blank=True)
    contentImage = models.FileField(upload_to="contents/images", null=True, blank=True)
    contentVideo = models.FileField(upload_to="contents/images", null=True, blank=True)
    order = OrderField(blank=True, for_fields=['module'])
    

    class Meta:
        ordering = ['order']
    
