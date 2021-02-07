from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_per_page = 20


admin.site.register(Post, PostAdmin)
admin.site.register(Administration)
admin.site.register(Teacher)
admin.site.register(OurPride)
admin.site.register(Honour)
