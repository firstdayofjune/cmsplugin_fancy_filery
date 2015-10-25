from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField


class Gallery(CMSPlugin):
    title = models.TextField(default='Gallery')

    def get_all_visible(self):
        return self.images.filter(display=True)

    def __str__(self):
        return self.title

    def copy_relations(self, old_instance):
        for image in old_instance.images.all():
            # instance.pk = None; instance.pk.save() is the standard Django way
            # of copying a saved model instance
            image.pk = None
            image.plugin = self
            image.save()


class Image(CMSPlugin):
    filer = FilerImageField(verbose_name=_('image'), help_text=_('Please upload a jpeg or png image'), null=True)
    title = models.TextField(default='Image')
    description = models.TextField(null=True)
    gallery = models.ForeignKey(Gallery, default=0, related_name='images')
    gallery_position = models.IntegerField(default=0)
    display = models.BooleanField(default=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.filer)