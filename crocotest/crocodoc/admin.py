
# django admin
from django.contrib import admin
# the app
from crocodoc.models import Example

class ExampleAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'document',
                    'thumbnail',]

    ordering = ['id']

admin.site.register(Example, ExampleAdmin)
