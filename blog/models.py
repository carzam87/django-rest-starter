from django.db import models
from cloudinary.models import CloudinaryField


# create blog models here
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField( upload_to="images/", blank=True)
    # add author field to the blog model related to the user model
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    