from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, default="Empty title")
    description = models.CharField(max_length=250, default="Empty description")
    url = models.URLField(blank=True)
    # MEDIA_ROOT default location is <project_root>/media/
    image = models.ImageField(
        upload_to="portfolio/images/", default="portfolio/images/pal_gwang.png"
    )