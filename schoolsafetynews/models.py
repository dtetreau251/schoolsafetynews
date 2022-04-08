from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255, blank = True, null = True)
    description = models.CharField(max_length=255, blank = True, null = True)
    image_url = models.CharField(max_length=255, blank = True, null = True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)