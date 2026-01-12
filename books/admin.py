from django.contrib import admin
from .models import Books


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display= ("id","Title","Published_date","Author","ISBN","Stock")
    search_fields=("id","Author")
    list_filter=("Author",)






