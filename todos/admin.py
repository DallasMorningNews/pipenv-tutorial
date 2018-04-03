from django.contrib import admin

from todos.models import List, ListItem


class ListItemInline(admin.TabularInline):
    extra = 3
    model = ListItem


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    inlines = [ListItemInline]
