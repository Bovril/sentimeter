from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("username", "interactions")

    search_fields = ["user__username"]

