from django.db import models
from django.conf import settings
# Create your models here.
MEMBERSHIP_CHOICES = (('Premium', 'pre'),('Free', 'free'))
class Membership(models.Model):
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(
    choices=MEMBERSHIP_CHOICES, default='Free',
    max_length=30
      )
    price = models.DecimalField(default=0)
def __str__(self):
       return self.membership_type
# Create your models here.
