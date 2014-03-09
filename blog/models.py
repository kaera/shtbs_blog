from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	date = models.DateTimeField('Date')
	content = models.TextField(max_length=10000)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return '/blog/%i/' % self.id

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        db_index=True,)
    username = models.CharField(verbose_name='Nickname',  max_length=255, unique=True)
    avatar = models.ImageField(verbose_name='Avatar',  upload_to='media/user_avatars', blank=True, null=True)
    first_name = models.CharField(verbose_name='First name',  max_length=255, blank=True)
    last_name = models.CharField(verbose_name='Second',  max_length=255, blank=True)
    
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name,)

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email


