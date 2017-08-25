from django.contrib import admin
from .models import Post, Comment

class PostmodelAdmin(admin.ModelAdmin):
    list_display = ['author','title','created_date']
    list_display_links = ['created_date']
    list_editable = ['title']
    list_filter = ['created_date','title']
    search_fields = ['title','text']

    class Meta:
        model=Post


admin.site.register(Post, PostmodelAdmin)
admin.site.register(Comment)