from django.urls import path
from django.views.generic.base import TemplateView


app_name='gview'


urlpatterns = [
    # Wired an index or anything view into the URLconf
    path(
        '', 
        TemplateView.as_view(template_name="gview/index.html"), 
        name="gview-index"
    ),
]