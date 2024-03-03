from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "My Model"
        verbose_name_plural = "My Models"
        ordering = ['-created_at']  # Corrected the attribute name
