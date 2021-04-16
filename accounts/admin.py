from django.contrib import admin

from .models import Account, Profile
from .forms import UserAdminCreationForm, UserAdminChangeForm


class UserAdmin(admin.ModelAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_superuser',)
    list_filter = ('is_superuser', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'avatar',)}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'username',)
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ('email',)
    filter_horizontal = ()

    class Meta:
        model = Account


admin.site.register(Account, UserAdmin)
admin.site.register(Profile)
