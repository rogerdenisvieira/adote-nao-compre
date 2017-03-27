
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('AdoteNaoCompreSITE.urls')),
    url(r'^admin/', admin.site.urls),
]

handler403 = 'AdoteNaoCompreSITE.controllers.generic_controller.unauthorizedHandler'
handler404 = 'AdoteNaoCompreSITE.controllers.generic_controller.pageNotFoundHandler'
