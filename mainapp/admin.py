from django.contrib import admin

# Register your models here.
from .models import Employee,MenuCategory
from .models import IndianRestaurantItem,Order
from .models import DailyMenu, MenuEmployeeAssignment

@admin.register(IndianRestaurantItem)
class IndianRestaurantItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'cuisine', 'dietary_preference', 'spice_level', 'price', 'is_available', 'updated_at')
    list_filter = ('cuisine', 'dietary_preference', 'spice_level', 'is_available')
    search_fields = ('name', 'description')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone_number', 'shift', 'salary', 'is_active')
    list_filter = ('role', 'shift', 'is_active')
    search_fields = ('name', 'email', 'phone_number')

admin.site.register(MenuCategory)    



@admin.register(DailyMenu)
class DailyMenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'created_at', 'updated_at')
    list_filter = ('date',)
    search_fields = ('date',)

@admin.register(MenuEmployeeAssignment)
class MenuEmployeeAssignmentAdmin(admin.ModelAdmin):
    list_display = ('menu', 'employee', 'role', 'assigned_at')
    list_filter = ('role', 'menu__date')
    search_fields = ('employee__name', 'menu__date', 'role')

admin.site.register(Order)



from django.contrib.admin.sites import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "Tip Prediction Admin Panel"
    site_title = "Admin Panel"
    index_title = "Welcome to the Admin Dashboard"

    class Media:
        css = {
            "all": ("admin/css/custom_admin.css",)  # Load custom CSS file
        }

custom_admin_site = CustomAdminSite(name="customadmin")

admin.site.site_header = "Tip Prediction Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to the Admin Dashboard"
