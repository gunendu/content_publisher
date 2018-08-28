from django.db import models

# Create your models here.

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    author_name = models.CharField(max_length=255,blank=True, null=True)
    upvote = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.author_name

    class Meta:
        db_table = 'article'
