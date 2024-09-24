from django import template
import datetime
from TuliusCookBook.models import Recipe, Section, Comment
from Country.models import CountryComment

register = template.Library()


@register.filter(name='receipt_count')
def is_group(story_id):
    receipt_count = Recipe.objects.filter(story=story_id).count()
    return receipt_count


@register.filter(name='receipts')
def is_group(story_id):
    receipts = Recipe.objects.filter(story=story_id)
    return receipts


@register.filter(name='comment_count')
def is_group(receipt_id):
    comment_count = Comment.objects.filter(recipe=receipt_id).count()
    return comment_count


@register.filter(name='sections')
def is_group(story_id):
    sections = Section.objects.all()
    return sections


@register.filter(name='comment_changed')
def is_group(comment_id):
    comment_changed = Comment.objects.get(id=comment_id)
    rezult = (comment_changed.time_change - comment_changed.time_creation).total_seconds()
    return True if rezult >= 1 else False


@register.filter(name='comment_changed_country')
def is_group(comment_id):
    comment_changed_country = CountryComment.objects.get(id=comment_id)
    rezult = (comment_changed_country.time_change - comment_changed_country.time_creation).total_seconds()
    return True if rezult >= 1 else False


@register.filter(name='comment_count_country')
def is_group(receipt_id):
    comment_count_country = CountryComment.objects.filter(receipt=receipt_id).count()
    return comment_count_country
