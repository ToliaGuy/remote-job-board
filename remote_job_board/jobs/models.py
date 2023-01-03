from django.db import models



class JobPost(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=100)

    def __str__(self):
        return self.title