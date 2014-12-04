from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.


class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']
	# # pub_date moved to the top of the list
	# using fieldsets to make fields more readable.

	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		# adds the arbitrary html class collapse.
	]
	inlines = [ChoiceInline]

# hooks models to the admin site.
# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)