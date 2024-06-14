from django.contrib import admin
from features.models import Uses
from features.models import Formdata

# Register your models here.
class Useradmin(admin.ModelAdmin):
    list_display = ('uses_title','uses_des')
admin.site.register(Uses, Useradmin)

class Enquiryform(admin.ModelAdmin):
    list_display = ('name','email','password','pics')
admin.site.register(Formdata, Enquiryform)



