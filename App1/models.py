from enum import Enum
from django.contrib.auth.models import User
from django.db import models

class Status(Enum):
    NEW = 'new'
    IN_PROGRESS = 'in progress'
    COMPLETED = 'completed'


ROLE_CHOICES = [
    ('admin', 'Administrator'),
    ('user', 'Regular User'),
]



class Team(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Name)

class Profile(models.Model):
    Id = models.AutoField(primary_key=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Team",null=True, blank=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20,default="user")

    def __str__(self):
        return str(self.User.username)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    myStatus = models.CharField(
        max_length=100,
        choices=[(status.value, status.name) for status in Status],
        default=Status.NEW.value)
    AssignedUser = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Teams = models.ForeignKey(Team, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name