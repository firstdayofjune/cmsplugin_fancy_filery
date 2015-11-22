from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField


class Gallery(CMSPlugin):
    title = models.CharField(_('title'), max_length=70, default=_('Gallery'))
    style = models.TextField(_('style', max_length=70, default=('Tiles')))
    def get_all_visible(self):
        return self.images.filter(display=True)

    def __str__(self):
        return self.title

    def copy_relations(self, old_instance):
        for image in old_instance.images.all():
            # a new image has to be created to prevent the images from being deleted when publishing the page
            live_image = Image()
            live_image.gallery = self
            live_image.gallery_position = image.gallery_position
            live_image.filer = image.filer
            live_image.title = image.title
            live_image.description = image.description
            live_image.display = image.display
            live_image.save()

class Image(CMSPlugin):
    gallery = models.ForeignKey(Gallery, default=0, related_name='images')
    gallery_position = models.IntegerField(default=0)
    filer = FilerImageField(verbose_name=_(_('Filer Image')), help_text=_('Please upload a jpeg or png image'), null=True)
    title = models.CharField(_('title'), max_length=70, default=_('Image'))
    description = models.TextField(null=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.filer)