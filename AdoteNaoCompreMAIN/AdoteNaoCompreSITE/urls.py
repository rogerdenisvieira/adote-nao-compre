from django.conf import settings
from django.conf.urls import url, handler404, handler403
from django.views.static import serve
from AdoteNaoCompreSITE.controllers import home_controller, account_controller, dog_controller, generic_controller, user_controller, wish_controller

urlpatterns = [
    url(r'^$', home_controller.index),
    url(r'^account/login', account_controller.login_user, name='login'),
    url(r'^restricted', generic_controller.restricted),
    url(r'^dog/search/', dog_controller.search, name='dog_search'),
    url(r'^account/logout', account_controller.logout_user, name='logout'),
    url(r'^user/create', user_controller.create, name="user_create"),
    url(r'^user/show/(?P<id>[0-9]+)', user_controller.show, name="user_show"),
    url(r'^user/profile/', user_controller.show_profile, name="user_profile"),
    url(r'^dog/list', dog_controller.list, name="dog_list"),
    url(r'^dog/create', dog_controller.create, name="dog_create"),
    url(r'^dog/delete', dog_controller.delete, name="dog_delete"),
    url(r'^dog/show/(?P<id>[0-9]{2})', dog_controller.show, name='dog_show'),
    url(r'^dog/edit/(?P<id>[0-9]{2})', dog_controller.edit, name='dog_edit'),
    #url(r'^wish/check', wish_controller.check_wishlist, name='wish_check'),
    url(r'^wish/create', wish_controller.create, name='wish_create'),
    url(r'^wish/list', wish_controller.list, name="wish_list"),
    url(r'^wish/delte', wish_controller.delete, name="wish_delete"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

handler403 = 'AdoteNaoCompreSITE.controllers.generic_controller.unauthorizedHandler'
handler404 = 'AdoteNaoCompreSITE.controllers.generic_controller.pageNotFoundHandler'