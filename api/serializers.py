from django.contrib.auth.models import User
from rest_framework import serializers
from stack.models import UserProfile,Questions,Answers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        

class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True,many=False)
    question_count=serializers.CharField(read_only=True)
    class Meta:
        model=UserProfile
        fields="__all__"


class AnswerSerializer(serializers.ModelSerializer):

    id=serializers.CharField(read_only=True)

    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    upvote_count=serializers.CharField(read_only=True)

    class Meta:
        model=Answers
        fields=["id","answer","user","created_date","upvote_count"]


class QuestionSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    question_answers=AnswerSerializer(read_only=True,many=True)
    class Meta:
        model=Questions
        fields=["id","description","image","user","created_date","question_answers"]


