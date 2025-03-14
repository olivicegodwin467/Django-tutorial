from django.contrib import admin
from .models import Members

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = "first_name", "last_name", "country"

admin.site.register(Members, MemberAdmin)
