from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return f"category name${self.category}"



# Define choices for cuisine types
CUISINE_CHOICES = [
    ('north_indian', 'North Indian'),
    ('south_indian', 'South Indian'),
    ('east_indian', 'East Indian'),
    ('west_indian', 'West Indian'),
    ('street_food', 'Street Food'),
    ('dessert', 'Dessert'),
    ('beverage', 'Beverage'),
]

# Define choices for spice levels
SPICE_LEVEL_CHOICES = [
    ('mild', 'Mild'),
    ('medium', 'Medium'),
    ('spicy', 'Spicy'),
    ('very_spicy', 'Very Spicy'),
]

# Define choices for dietary preferences
DIETARY_CHOICES = [
    ('veg', 'Vegetarian'),
    ('non_veg', 'Non-Vegetarian'),
    ('vegan', 'Vegan'),
    ('jain', 'Jain Food'),
]

class IndianRestaurantItem(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the dish
    cuisine = models.CharField(max_length=20, choices=CUISINE_CHOICES)  # Indian cuisine type
    dietary_preference = models.CharField(max_length=10, choices=DIETARY_CHOICES)  # Dietary preference
    spice_level = models.CharField(max_length=10, choices=SPICE_LEVEL_CHOICES, default='medium')  # Spice level
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the dish
    is_available = models.BooleanField(default=True)  # Availability status
    description = models.TextField(blank=True, null=True)  # Description of the dish
    # Change FileField to ImageField for image validation
    photo = models.ImageField(upload_to="restaurant/items/", blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the dish was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return f"{self.name} ({self.cuisine}) - ₹{self.price}"

    class Meta:
        ordering = ['cuisine', 'name']



# Define choices for employee roles
ROLE_CHOICES = [
    ('manager', 'Manager'),
    ('chef', 'Chef'),
    ('waiter', 'Waiter'),
    ('cleaner', 'Cleaner'),
    ('cashier', 'Cashier'),
    ('delivery', 'Delivery Person'),
]

# Define choices for work shifts
SHIFT_CHOICES = [
    ('morning', 'Morning'),
    ('afternoon', 'Afternoon'),
    ('evening', 'Evening'),
    ('night', 'Night'),
]

class Employee(models.Model):
    name = models.CharField(max_length=100)  # Employee's full name
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)  # Job role
    email = models.EmailField(unique=True)  # Contact email
    phone_number = models.CharField(max_length=15, unique=True)  # Contact phone number
    salary = models.DecimalField(max_digits=8, decimal_places=2,default='20000')  # Monthly salary
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES,default='morning')  # Assigned work shift
    date_of_joining = models.DateField(auto_now=True)  # Joining date
    address = models.TextField(blank=True, null=True)  # Employee's address
    is_active = models.BooleanField(default=False)  # Employment status
    photo = models.ImageField(upload_to="restaurant/items/", blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Record update timestamp
    password=models.CharField(max_length=100,default='password')
    

    def __str__(self):
        return f"{self.name} - {self.role.capitalize()}"

    class Meta:
        ordering = ['role', 'name']

from django.db import models

# Reuse Employee and IndianRestaurantItem models
class DailyMenu(models.Model):
    date = models.DateField(unique=True)  # The date for the menu
    items = models.ManyToManyField('IndianRestaurantItem')  # Menu items available for the day
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the menu was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update

    def __str__(self):
        return f"Menu for {self.date}"

    class Meta:
        ordering = ['-date']  # Latest menus appear first


class MenuEmployeeAssignment(models.Model):
    menu = models.ForeignKey(DailyMenu, on_delete=models.CASCADE)  # Reference to the daily menu
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)  # Reference to the assigned employee
    role = models.CharField(
        max_length=20,
        choices=[
            ('chef', 'Chef'),
            ('waiter', 'Waiter'),
            ('manager', 'Manager'),
            ('delivery', 'Delivery Person'),
        ]
    )  # Role of the assigned employee for the menu
    assigned_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the employee was assigned

    def __str__(self):
        return f"{self.employee.name} - {self.role.capitalize()} for {self.menu.date}"

    class Meta:
        unique_together = ('menu', 'employee', 'role')  # Prevent duplicate assignments for the same role and menu

class Order(models.Model):
    item=models.ForeignKey(IndianRestaurantItem,on_delete=models.CASCADE)
    total_amount=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    adddress=models.TextField(max_length=100)
    status=models.CharField(max_length=100,default='pending')

    def __str__(self):
        return f'item name:${self.item.name}'