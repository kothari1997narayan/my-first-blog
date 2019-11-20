from django.contrib import admin
from .models import Post, Comment

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = ['make_published']
    def make_published(self, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "1 story was"
    else:
        message_bit = "%s stories were" % rows_updated
    self.message_user(request, "%s successfully marked as published." % message_bit)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)