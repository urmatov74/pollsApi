from django.contrib import admin

# Register your models here.
from .models import Question, Poll, Vote, Variant, Report

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(Vote)
admin.site.register(Variant)
admin.site.register(Report)

