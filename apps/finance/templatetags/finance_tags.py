from django import template
from apps.finance.models import Notification

register = template.Library()

@register.inclusion_tag('finance/notifications_tag.html')
def recent_notifications():
    notifications = Notification.objects.order_by('-timestamp')[:10]
    return {'notifications': notifications}