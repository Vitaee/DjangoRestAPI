from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return self.title