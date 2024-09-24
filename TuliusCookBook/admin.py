from django.contrib import admin
from .models import *


class CatalogStoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link_to_story', 'link_to_image')
    list_per_page = 20
    list_filter = ('title',)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nikname', 'avatar', 'signature')
    list_per_page = 20
    list_filter = ('nikname', 'user',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'author', 'story', 'time_creation')
    list_per_page = 20
    list_filter = ('dish_name', 'time_creation',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'time_creation', 'time_change')
    list_per_page = 20
    list_filter = ('author', 'time_creation',)


class FactAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'time_creation')
    list_per_page = 20


admin.site.register(CatalogStories, CatalogStoriesAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Fact, FactAdmin)
