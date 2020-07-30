from django.contrib import admin

#------Django Internal Packages-----
from django.contrib import admin
#/------Django Internal Packages-----
 
#------Django Importing Models-----
from my_project_data.models import ContactForm
#/------Django Importing Models-----
 
#Register your models here.
 
#-----Django Admin View for ----
 
#Django Admin View for Contact Form Model
class ContactFormkAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        'submitted_at',
        "full_name",
        "pid",
        "project_title",
        "project_description",
    ]
    list_editable = ["full_name"]
 
#Register ContactForm in Admin view 
admin.site.register(ContactForm,ContactFormkAdmin)
