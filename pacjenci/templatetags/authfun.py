from django import template
register = template.Library()

@register.filter(name='isInGroup')
def isInGroup(user,groupname):
    return user.groups.filter(name=groupname).exists()
