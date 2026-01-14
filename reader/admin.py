from django.contrib import admin
from .models import Reader, Bookborrowed

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display= ("id","Full_name","Email","Address","contact_no")
    search_fields= ("contact_no","id")
    list_filter= ("Full_name",) 

    

@admin.register(Bookborrowed)
class BookborrowwedAdmin(admin.ModelAdmin):
    list_display= ("book","reader","due_date","remaining_days")
    search_fields= ("due_date","book")
    list_filter=("book",)

    def remaining_days(self,obj):
        return obj.remaining_days()



