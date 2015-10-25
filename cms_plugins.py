from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cmsplugin_fancy_filery.models import Gallery


class FancyFileryPlugin(CMSPluginBase):
    model = Gallery
    name = _('Fancy gallery')
    render_template = "cmsplugin_fancy_filery/base.html"
    cache = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(FancyFileryPlugin)

