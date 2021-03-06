from django.db import models
from django.contrib.auth.models import User

#   apk models

class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    #Posle cemo dodati i slike
    img = models.ImageField(null=True, blank=True)
    #likes = models.IntegerField(default=0)  #podesicemo da se ovo inkrementira
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    class Meta:
        #model = Article
        #fields = ['title', 'content']
        #articles = 'articles'
        pass


    def __str__(self):
        return f'{self.title}'