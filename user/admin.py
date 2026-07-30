from django.contrib import admin
from user.models import *
# Register your models here.


admin.site.site_header = "Login System Administration"
admin.site.site_title = "Login System Admin"
admin.site.index_title = "Welcome to Login System Dashboard"
admin.site.register(registration)
admin.site.register(testtable)