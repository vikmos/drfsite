from email.policy import default
from rest_framework import serializers
from .models import Comment, News
from .models import User

class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'password', 'password2'] #'email',

    def save(self, *args, **kwargs):
        user = User(
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: "Пароли не совпадают"})
        
        user.set_password(password)
        user.save()
        return user

class NewsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = News
        fields = "__all__"
        
class CommentsSerializer(serializers.ModelSerializer):
    author_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comment
        fields = "__all__"