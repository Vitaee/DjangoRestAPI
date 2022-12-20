from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import EmailMultiAlternatives


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.CharField(max_length=249, null=True, blank=True, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    regisDate = models.DateTimeField(default=timezone.now, verbose_name="Regis Date")
    created_by = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=['created_by', ]), ]


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "\nPlease go to this link:\n http://127.0.0.1:8000/newpass/{}".format(
        reset_password_token.key) + "\n and set your new password."

    from_email, to = 'canow712@gmail.com', f"{reset_password_token.user.email}"

    msg = EmailMultiAlternatives("Learning Django Rest | Reset your password.", email_plaintext_message, from_email,
                                 [to])
    msg.send()
