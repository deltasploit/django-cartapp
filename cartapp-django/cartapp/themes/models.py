from datetime import datetime
from django.db import models
from datetime import datetime


# Create your models here.
class Theme(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.title


class ThemeVariable(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self) -> str:
        return self.name


class ThemeTemplate(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    html_content = models.TextField()
    variables = models.ManyToManyField(ThemeVariable)
    # TODO add type

    def __str__(self) -> str:
        return self.title



