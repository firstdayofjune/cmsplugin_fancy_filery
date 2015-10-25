from django.contrib import admin

from cmsplugin_fancy_filery.models import Image


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    fk_name = 'gallery'