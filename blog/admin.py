from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = ['make_published','toggle_publish']

    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='p')
        for post in queryset:
            post.status = 'p'
    
    def toggle_publish(self, request, obj, parent_obj=None):
        if obj.status == 'd':
            obj.status = 'p'
        else:
            obj.status = 'd'

        obj.save()
        status = 'unpublished' if obj.status == 'd' else 'published'
        messages.info(request, _("Article {}.".format(status)))

    def get_toggle_publish_label(self, obj):
        label = 'publish' if obj.status == 'd' else 'unpublish'
        return 'Toggle {}'.format(label)

    def get_toggle_publish_css(self, obj):
        return (
            'btn-green' if obj.status == Article.DRAFT else 'btn-red')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)