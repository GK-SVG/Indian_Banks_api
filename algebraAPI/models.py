from django.db import models

# Create your models here.
class QuestionAnswer(models.Model):
    question=models.TextField()
    answerTXT=models.TextField(null=True,blank=True,default='')
    answerIMG=models.ImageField(null=True,blank=True,default='')

    def __str__(self):
        return self.question
    