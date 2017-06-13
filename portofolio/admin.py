# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Portofol

# Register your models here.
class PortoModelAdmin(admin.ModelAdmin):
    list_display = ["title","updated",'timestamp']
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated","timestamp"]

    search_fields = ["title","content"]
    class Meta:
        model = Portofol

admin.site.register(Portofol, PortoModelAdmin)
