from django import template
import urllib.parse

register = template.Library()

@register.filter
def toggle_value(request, arg):
    url_parts = list(urllib.parse.urlparse(request.get_full_path()))
    query = dict(urllib.parse.parse_qsl(url_parts[4], keep_blank_values=True))
    query["pagina"] = arg
    url_parts[4] = urllib.parse.urlencode(query)
    return urllib.parse.urlunparse(url_parts)