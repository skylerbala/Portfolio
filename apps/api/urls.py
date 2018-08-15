from django.conf.urls import include, url
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('project.api.urls')),
]