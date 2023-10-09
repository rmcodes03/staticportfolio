from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.CharField(max_length=1000)
    blog_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%I' + ':' + '%M %p' + ', %d %b %Y')
