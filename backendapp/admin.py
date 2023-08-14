from django.contrib import admin

# Register your models here.


from .models import Mobile


from django.contrib import admin
from .models import Mobile

class MobileAdmin(admin.ModelAdmin):
    list_display = ('projectname', 'username', 'startdate', 'enddate' , 'workhours')
    

admin.site.register(Mobile, MobileAdmin)
 
