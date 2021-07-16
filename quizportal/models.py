from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ROLES = (
        ('A', 'Admin'),
        ('U', 'User')
    )
    role = models.CharField(max_length=1, choices=ROLES)
    mobile = models.CharField(max_length=10)


class Test(models.Model):
    test_name = models.CharField(max_length=30, unique=True)
    test_date = models.DateTimeField(null=True)
    start = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.test_name


class Question(models.Model):
    select_test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='que')
    text_question = models.CharField(max_length=300, null=True,blank=True)
    img_question = models.ImageField(null=True, blank=True)


class Option(models.Model):
    select_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='opts')
    select_option = models.CharField(max_length=30)
    option_status = models.BooleanField(default=False)

    def __str__(self):
        return self.select_option


class UserAttempts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='answers')

    unique_together = [['user', 'test']]

    def __str__(self):
        return self.user.first_name + '-' + self.test.test_name


class UserResponses(models.Model):
    attempt = models.ForeignKey(UserAttempts, on_delete=models.CASCADE, related_name='response')
    omr_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    answer = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True)



