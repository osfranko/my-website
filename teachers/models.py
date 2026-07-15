from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)

    def __str__(self):
        return self.name