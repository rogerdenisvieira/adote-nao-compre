from django.contrib import admin
from AdoteNaoCompreSITE.models.dog import Dog
from AdoteNaoCompreSITE.models.post import Post
from AdoteNaoCompreSITE.models.breed import Breed
from AdoteNaoCompreSITE.models.state import State
from AdoteNaoCompreSITE.models.advertisement import Advertisement

admin.site.register(Dog)
admin.site.register(Post)
admin.site.register(Breed)
admin.site.register(State)
admin.site.register(Advertisement)

