from django.contrib import admin
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.post import Post
from AdoteNaoCompreSITE.models.breed import Breed

admin.site.register(Dog)
admin.site.register(Post)
admin.site.register(Breed)

