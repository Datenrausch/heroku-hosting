from django.contrib import admin

from .models import *




class DataCollection(admin.TabularInline):
    model = DataCollection
    extra = 1



class MediumAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,               {'fields': ['mediumname'] }),
    ('Jobstatus', {'fields': ['freeoremployed']}),

]
    inlines = [DataCollection]
    #this is for the question page
    list_display = ['mediumname','freeoremployed']
    #fields = ['pub_date', 'question_text']
    list_filter = ['freeoremployed']
    search_fields = ['mediumname']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #this is for the question page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #fields = ['pub_date', 'question_text']
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Medium, MediumAdmin)
admin.site.register(Question, QuestionAdmin)
