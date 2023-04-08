from django.contrib import admin
from.models import User, Vehicle, CurrentVehicle, Expedition, Ticket, OrderItem, Module, Question

# Register your models here.

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(CurrentVehicle)
admin.site.register(Expedition)

admin.site.register(Ticket)
admin.site.register(OrderItem)

admin.site.register(Module)
admin.site.register(Question)