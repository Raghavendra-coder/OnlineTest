from django.contrib import admin
from .models import User, Test, Question, Option, UserAttempts, UserResponses
# Register your models here.


class UserAttemptsAdmin(admin.ModelAdmin):
    list_display = ('user', 'test',)


class UserResponseAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'omr_question', 'answer')
    list_filter = ('attempt',)


admin.site.register(User)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserAttempts, UserAttemptsAdmin)
admin.site.register(UserResponses, UserResponseAdmin)
