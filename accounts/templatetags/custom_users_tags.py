from django import template
from TuliusCookBook.models import Recipe

register = template.Library()


@register.filter(name='count')
def count(user_id):
    receipt_count = Recipe.objects.filter(author=user_id).count()
    return receipt_count


@register.filter(name='game_list')
def game_list(user_id):
    receipts = Recipe.objects.filter(author=user_id)
    return receipts
