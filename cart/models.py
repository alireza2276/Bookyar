from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    first_name = models.CharField(_('first_name'), max_length=50)
    last_name = models.CharField(_('last_name'), max_length=50)
    address = models.CharField(_('address'), max_length=500)
    phone_number = models.CharField(_('phone_number'), max_length=12)
    email = models.EmailField(_('email'))
    description = models.TextField(_('your note'), null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - {self.address}"

    class Meta:
        verbose_name_plural = _('Orders')
