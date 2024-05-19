from django.contrib import admin

from .models import Book, Author, Address, Country
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_filter = ("rating", "is_bestselling")
    list_display = ("title", "author", "rating")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)