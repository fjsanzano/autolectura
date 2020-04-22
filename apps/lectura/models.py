from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# class Article(models.Model):
#     article_id = models.AutoField(primary_key=True)
#     article_heading = models.CharField(max_length=250)
#     article_body = models.TextField()


class CommercialOffice(models.Model):
    class Meta:
        ordering = ('name',)
        verbose_name = _('Commercial Office')

    name = models.CharField(verbose_name=_('Name'), help_text=_('Commercial Office name'), max_length=64,  default='000000', unique=True)
    email = models.CharField(verbose_name=_('E-Mail'), help_text=_('Commercial Office E-mail'), max_length=64)
    telephone = models.CharField(verbose_name=_('Telephone'), help_text=_('Commercial Office Telephone'), max_length=64)

    def __str__(self):
        return self.name


class MeterReading(models.Model):
    class Meta:
        ordering = ('contract_number',)
        verbose_name = _('Meter Reading')

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    contract_number = models.CharField(verbose_name=_('Contract number'), help_text=_('Commercial Office name'),
                                       max_length=64,  default='000000', unique=True)
    commercial_office_id = models.ForeignKey(CommercialOffice, on_delete=models.CASCADE,
                                             verbose_name=_('Commercial Office'),)
    route = models.IntegerField(verbose_name=_("Collection route"), null=True,)
    number = models.IntegerField(verbose_name=_("Folio"), null=True,)

    reading = models.CharField(verbose_name=_('Name'), help_text=_('Commercial Office name'), max_length=6,  default='00000', )

    def __str__(self):
        return self.contract_number + '/' + self.reading
