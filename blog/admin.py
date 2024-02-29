from django.contrib import admin
from django.utils.html import format_html
from .models import Blog

#show title, date, author, excerpt, and image in the admin panel
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date_pretty', 'author', 'summary', 'image_tag')
    
    def image_tag(self, obj):
        return format_html('<img src="{}" width="96" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


admin.site.register(Blog, BlogAdmin)

