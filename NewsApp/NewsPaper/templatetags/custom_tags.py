# ✅создали файл самостоятельно для тегов
from datetime import datetime
# импорт шаблон
from django import template

# зарегали тег
register = template.Library()


# строчковый временной тег
@register.simple_tag()
def current_time(format_string='%b %d %Y'):
    return datetime.utcnow().strftime(format_string)
