from django.db import models
from acc.models import User
from django.utils import timezone

# Create your models here.
class Join(models.Model):
    jsubject = models.CharField(max_length=100)
    jwriter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jwriter", default='')
    jcontent = models.TextField()
    jpubdate = models.DateTimeField(default=timezone.now)
    jlikey = models.ManyToManyField(User, blank=True, related_name="jlikey")
    
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"
    
    def __str__(self):
        return self.jsubject

class jReply(models.Model):
    jboard = models.ForeignKey(Join, on_delete=models.CASCADE)
    jreplyer = models.ForeignKey(User, on_delete=models.CASCADE)
    jcomment = models.TextField()

    def __str__(self):
        return f"{self.jboard}_{self.jreplyer} 님의 댓글"