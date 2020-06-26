from django.contrib import admin

# Register your models here.
from .models import Nouveaute, Categorie, Article, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'message', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('nom', 'email', 'message')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Article)
admin.site.register(Categorie)
admin.site.register(Nouveaute)