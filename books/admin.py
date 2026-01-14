from django.contrib import admin
from .models import Books


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display= ("id","Title","Published_date","Author","ISBN","Stock", "copies_available")
    search_fields=("id","Author")
    list_filter=("Author",)


    def get_copies_available(self,obj):
        return obj.copies_available()
        



