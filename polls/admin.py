from django.contrib import admin
from polls.models import Question, Choice
import datetime

# Register your models here.

# # # choices stacked inline # # #


# class ChoiceInline(admin.StackedInline):
# 	model = Choice
# 	extra = 3  # number of choices


# # # choices in Tabular form # # #


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3  # number of choices


class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']
	# # pub_date moved to the top of the list
	# using fieldsets to make fields more readable.

	list_display = ('question_text', 'pub_date')
	# display list as question_text and pub_date

	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		# adds the arbitrary html class collapse.
	]
	inlines = [ChoiceInline]

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	list_filter = ['pub_date']

# hooks models to the admin site.
# admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)