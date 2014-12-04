from django.contrib import admin
from polls.models import Question

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']
	# pub_date moved to the top of the list

admin.site.register(Question, QuestionAdmin)
