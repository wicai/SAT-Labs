from mchlrn.models import SATQuestion, Sat_Q_Processed, Answered_Sat_Q
from django.contrib import admin
from django.contrib.auth.models import User
from mchlrn.models import UserData

class SATQuestionAdmin(admin.ModelAdmin):
	list_display = ('name', 'id')
	search_fields = ['name', 'id']

class UserDataInline(admin.TabularInline):
	model = UserData

class UserAdmin(admin.ModelAdmin):
	inlines = [
	UserDataInline,
	]

admin.site.register(Answered_Sat_Q)
admin.site.register(SATQuestion, SATQuestionAdmin)
admin.site.register(Sat_Q_Processed)
admin.site.register(UserData)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)