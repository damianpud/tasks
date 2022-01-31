from django.template import Library
from django.utils.html import escape
from django.utils.safestring import SafeString

register = Library()


@register.simple_tag
def post_format(post):
    return f'{post.title} Author: {post.author} - ({post.created.strftime("%Y-%m-%d %H:%M")})'


@register.filter
def attr_as_p(obj, attrname):
    label = escape(attrname.capitalize())
    value = escape(getattr(obj, attrname))
    return SafeString(f'<p><strong>{label}:</strong> {value}</p>')
