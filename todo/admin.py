from django.contrib import admin
from todo.models import Task, Tag


@admin.register(Task)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("tags",)


admin.site.register(Tag)
