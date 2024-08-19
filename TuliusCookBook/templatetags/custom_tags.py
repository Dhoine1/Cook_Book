from django import template
from TuliusCookBook.models import Recipe, Section

register = template.Library()


@register.filter(name='receipt_count')
def is_group(story_id):
    receipt_count = Recipe.objects.filter(story=story_id).count()
    return receipt_count


@register.filter(name='receipts')
def is_group(story_id):
    receipts = Recipe.objects.filter(story=story_id)
    return receipts


@register.filter(name='sections')
def is_group(story_id):
    sections = Section.objects.all()
    return sections
