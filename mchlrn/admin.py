from mchlrn.models import SATQuestion, Sat_Q_Processed
from django.contrib import admin

class SATQuestionAdmin(admin.ModelAdmin):
	list_display = ('name', 'id')
	search_fields = ['name', 'id']
admin.site.register(SATQuestion, SATQuestionAdmin)
admin.site.register(Sat_Q_Processed)