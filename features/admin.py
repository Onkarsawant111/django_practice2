from django.contrib import admin
from features.models import Uses

# Register your models here.
class Useradmin(admin.ModelAdmin):
    list_display = ('uses_title','uses_des')

admin.site.register(Uses, Useradmin)