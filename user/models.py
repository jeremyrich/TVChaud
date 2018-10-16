from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=False)
    password = models.CharField(max_length=255, blank=True, null=False)
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Favorites(models.Model):
    favorite_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=False)
    tv_id = models.IntegerField(blank=True, null=False)
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorites'


class Friendship(models.Model):
    friendship_id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=False)
    user2 = models.IntegerField(blank=True, null=False)
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friendship'


class FriendRequest(models.Model):
    friend_request_id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=False)
    to_user = models.IntegerField(blank=True, null=False)
    message = models.TextField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friend_request'


class NotificationType(models.Model):
    notification_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=85, blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_type'


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=False)
    message = models.TextField(blank=True, null=True)
    notification_type = models.ForeignKey(NotificationType, models.DO_NOTHING, blank=True, null=False)
    seen = models.BooleanField(blank=True, null=False)
    insert_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification'
