from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext as _
#from sorl.thumbnail import ImageField

#from . import settings as dcf_settings


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(
        _('Contact phone'), max_length=30, null=True, blank=True)
    receive_news = models.BooleanField(
        _('receive news'), default=True, db_index=True)

   # return self.user.item_set.count() < dcf_settings.ITEM_PER_USER_LIMIT

    @staticmethod
    def get_or_create_for_user(user):
        if hasattr(user, 'profile'):
            return user.profile
        else:
            return Profile.objects.create(user=user)


class Item(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, max_length=100)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    text = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='images')
    is_active = models.BooleanField(_('active'), default=True, db_index=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    file = models.ImageField(_('image'), upload_to='images')
