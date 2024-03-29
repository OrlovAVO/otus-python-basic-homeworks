from django.contrib import admin
from .models import Book, Author, Genre, BookInstance


class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'author',
                    'display_genre',
                    )
    inlines = [BookInstanceInline]
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name',
                    'first_name',
                    'date_of_birth',
                    'date_of_death',)
    fields = ['first_name',
              'last_name',
              ('date_of_birth',
               'date_of_death'),
              ]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book',
                    'status',
                    'borrower',
                    'due_back',
                    'id'
                    )

    list_filter = ('status',
                   'due_back'
                   )

    fieldsets = (
        (None, {
            'fields': ('book',
                       'id'
                       )
        }),
        ('Доступность', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
