from django.contrib import admin

# Register your models here.
from django.contrib import admin
from user.models import CustomUser,UserSocialNetworks


# Register your models here.
@admin.register(CustomUser)
class CustomUserdAdmin(admin.ModelAdmin):
    list_display= ('ci','email', 'first_name', 'last_name', 'role',)
    list_filter = ('ci','email', 'role',)
    search_fields = ('email',)




@admin.register(UserSocialNetworks)
class UserSocialNetworksAdmin(admin.ModelAdmin):
    list_display = ('get_user_name','get_user_lastname')
    
    def get_user_name(self, obj):
        return obj.user.first_name
    def get_user_lastname(self, obj):
        return obj.user.last_name
        


