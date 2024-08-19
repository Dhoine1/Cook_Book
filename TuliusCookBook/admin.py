from django.contrib import admin
from .models import *


class CatalogStoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link_to_story', 'link_to_image')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nikname', 'avatar', 'signature')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'author', 'story', 'time_creation')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'time_change')


admin.site.register(CatalogStories, CatalogStoriesAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
