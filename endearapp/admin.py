from django.contrib import admin
from endearapp.models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('email_address', 'username', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email_address', 'username')
    readonly_fields = ('email_address', 'date_joined')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
