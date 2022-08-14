from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


# Create your models here.
class CustomAccauntManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(username=username, **extra_fields,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password):
        return self._create_user(username, password)

    def create_superuser(self, username, password):
        return self._create_user(username, password, is_staff=True, is_superuser=True)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=25, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = CustomAccauntManager()
    
    def __str__(self):
        return self.username


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('User', verbose_name='Автор',on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    text = models.CharField(max_length=255)
    author_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    news_id = models.ForeignKey('News', on_delete=models.CASCADE, null= True) 
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
