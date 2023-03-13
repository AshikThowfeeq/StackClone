from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


class Questions(models.Model):
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-created_date"]

    def __str__(self) -> str:
        return self.description

    @property
    def question_answers(self):
        return Answers.objects.filter(question=self).annotate(ucount=Count('up_vote')).order_by('-ucount')


class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=500)
    created_date=models.DateTimeField(auto_now_add=True)
    up_vote=models.ManyToManyField(User,related_name="answer")

    @property
    def upvote_count(self):
        return self.up_vote.all().count()


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to="profiles",null=True)
    bio=models.CharField(max_length=200)

    @property
    def question_count(self):
        return Questions.objects.filter(user=self.user).count()
