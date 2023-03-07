from django.contrib import admin
from . import models

#When we are in admin page we can see the group and group members and also we can edit those in the same page
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
