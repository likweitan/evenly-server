from django.contrib import admin

# Register your models here.
from .models import Expense, Group, Participant

admin.site.register(Expense)
admin.site.register(Group)
admin.site.register(Participant)