from django.contrib import admin

# Register your models here.
from .models import Employee,MenuCategory
from .models import IndianRestaurantItem
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