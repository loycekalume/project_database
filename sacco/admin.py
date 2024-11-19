from django.contrib import admin

from sacco.models import Customer, Deposit

admin.site.site_header = 'Umoja Sacco Administration'
admin.site.site_title = 'Sacco Admin'

# Register your models here.
# python manage.py --help
# python manage.py createsuperuser

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','gender','dob']
    search_fields = ['first_name','last_name','email']
    list_filter = ['gender']
    list_per_page = 25

class DepositAdmin(admin.ModelAdmin):
    list_display = ['customer','created_at','status','amount']
    search_fields = ['customer', 'status', 'amount']
    list_filter = ['status']
    list_per_page = 25

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)

# p@55word