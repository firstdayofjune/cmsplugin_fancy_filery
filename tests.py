from django.test import TestCase

from cmsplugin_fancy_filery.models import Image, Gallery
from filer.models.imagemodels import Image as FilerImage


# Create your tests here.
class ImageAndGalleryModelTest(TestCase):

    def test_creating_and_requesting_images(self):
        filer1 = FilerImage()
        filer1.save()
        image = Image()
        image.filer = filer1
        image.title = 'This is the first image'
        image.description = 'This first image has been taken, at a place yet unknown.'
        image.save()

        filer2 = FilerImage()
        filer2.save()
        image_wo_desc = Image()
        image_wo_desc.filer = filer2
        image_wo_desc.title = 'Image without description'
        image_wo_desc.save()

        saved_images = Image.objects.all()
        self.assertEqual(len(saved_images), 2)

        first_img = saved_images[0]
        self.assertEqual(first_img.filer, filer1)
        self.assertEqual(first_img.title, 'This is the first image')
        self.assertEqual(first_img.description, 'This first image has been taken, at a place yet unknown.')

        second_img = saved_images[1]
        self.assertEqual(second_img.filer, filer2)
        self.assertEqual(second_img.title, 'Image without description')
        self.assertIsNone(second_img.description)


    def test_gallery_contains_images(self):
        gallery = Gallery()
        gallery.title = 'My Gallery'
        gallery.save()

        saved_gallery = Gallery.objects.first()
        self.assertEqual(saved_gallery, gallery)
        self.assertEqual(saved_gallery.title, 'My Gallery')

        image1 = Image()
        image1.title = 'This is the first image'
        image1.description = 'This first image has been taken, at a place yet unknown.'
        image1.gallery = saved_gallery
        image1.save()

        image2 = Image()
        image2.title = 'This is the second image'
        image2.gallery = saved_gallery
        image2.save()

        gallery_images = saved_gallery.image_set.all()
        print(saved_gallery.get_all_visible())
        self.assertEqual(len(gallery_images), 2)
        self.assertEqual(image1, gallery_images[0])
        self.assertEqual(image2, gallery_images[1])

