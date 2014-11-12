# -*- coding: utf-8 -*-
from django.contrib import admin
from mysite.books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')  #自定义显示列表
    list_filter = ('publication_date','publisher')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)    #自定义排列顺序
    fields = ('title', 'authors', 'publisher', 'publication_date','num_pages')  #自定义表单顺序
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)