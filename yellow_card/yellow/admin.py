from django.contrib import admin

# Register your models here.
from .models import personal_details

admin.site.site_header = "Yellow Fever Track App"
admin.site.site_title = "Yellow Fever Track App"
admin.site.index_title = "Yellow Fever Track App"
# Register your models here.

@admin.register(personal_details)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','issue_date','end_date','immunised_for','passport_or_nin_number','photo','slug')
    prepopulated_fields = {'slug':('passport_or_nin_number',),}
    