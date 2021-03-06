from django.conf.urls import (
    patterns,
    url,
)
from django.views.generic import TemplateView

urlpatterns = patterns(
    'scapegoat.views',
    url(r'^$', TemplateView.as_view(template_name='scapegoat/index.html'), name='index_view'),
)
