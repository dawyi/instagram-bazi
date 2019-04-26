from django.db import models

# Create your models here.

class Page(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True, db_index=True)
    url = models.URLField(null=True, blank=True)
    insta_id = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=31, null=True, blank=True)

    is_varified = models.BooleanField(null=True, blank=True)
    is_private = models.BooleanField(null=True, blank=True)
    is_join_recently = models.BooleanField(null=True, blank=True)
    is_business_account = models.BooleanField(null=True, blank=True)
    business_category_name =  models.CharField(max_length=255, null=True, blank=True)

    num_posts = models.IntegerField(default = 0)
    num_follower = models.IntegerField(default = 0)
    num_following = models.IntegerField(default = 0)
    biography = models.CharField(max_length=1023, null=True, blank=True)
    # step 2
    list_following = models.ManyToManyField('Page', related_name='follow')
    list_follower =  models.ManyToManyField('Page', related_name='followed_by')
    #list_pics = []
