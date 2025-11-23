# кастомная обрезка текста для новостей
from django import template
from django.utils.html import strip_tags
from django.utils.text import Truncator

register = template.Library()

@register.filter(name='truncate_html')
def truncate_html(value, num_words):
    """
    Безопасно обрезает HTML-текст по количеству слов,
    убирает незакрытые теги и возвращает валидный HTML.
    """
    if not value:
        return ''

    # 1. Обрезаем по словам (Truncator умеет работать с HTML)
    truncated = Truncator(value).words(int(num_words), html=True)

    # 2. На всякий случай дополнительно чистим возможные битые теги
    # (Truncator уже делает это хорошо, но можно подстраховаться)
    return truncated