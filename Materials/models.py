from django.db import models

class Material(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('download_material', args=[self.id])
