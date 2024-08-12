from django.db import models
from users.models import UserProfile, Organization


# class Task(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True) 
#     organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True )
#     title = models.CharField(max_length=100) 
#     description = models.TextField(null=True, blank=True)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         order_with_respect_to = 'user'