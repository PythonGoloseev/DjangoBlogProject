from django.contrib import admin

from .models import *

class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("id", "title", "start_at", "slug", "views_number", "created_at",)
    list_display_links = ("id", "title")
    readonly_fields = ("views_number", "created_at")


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Quiz_result)
admin.site.register(Answer)
admin.site.register(Question_audio)
