from django.db import models


class TypeActivity(models.Model):
    name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    icon = models.CharField(max_length=500)


class Location(models.Model):
    name = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()


class TypeUserRelationShip(models.Model):
    name = models.CharField(max_length=50)


class User(models.Model):
    username = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=500, null=True)
    is_active = models.BooleanField()
    oauth = models.CharField(max_length=500, null=True)


class Post(models.Model):
    type = models.ForeignKey(TypeActivity, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    image = models.CharField(max_length=500, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class UserRelationship(models.Model):
    user_first = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    user_second = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dependent')
    type = models.ForeignKey(TypeUserRelationShip, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)


class Report(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    offender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
