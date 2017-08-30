# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class ShipmentDetailInline(admin.TabularInline):
	model = ShipmentDetail
	extra = 0

class ShipStatInline(admin.TabularInline):
	model = ShipStat
	extra = 0	

class StatusDetailInline(admin.TabularInline):
	model = StatusDetail
	extra = 1	

class ShipmentAdmin(admin.ModelAdmin):
	list_display = ('track_id', 'sender', 'source', 'creation_date')
	inlines = [
		ShipmentDetailInline,
		ShipStatInline,
		StatusDetailInline
	]

class ShipmentDetailAdmin(admin.ModelAdmin):
	list_display = 	('ship_item', 'receiver', 'destination', 'arrival_date')
	list_filter = ('ship_item', 'receiver')
	readonly_fields = ('ship_item',)
	
class ShipStatAdmin(admin.ModelAdmin):
	list_display = ('ship_item', 'current_status', 'work_state')
	list_filter = ('ship_item', 'work_state', 'current_status')
	readonly_fields = ('ship_item',)

class StatusDetailAdmin(admin.ModelAdmin):
	list_display = ('det_id', 'ship_item', 'this_status', 'new_action_date', 'current_location', 'action')
	list_filter = ('ship_item', )
	readonly_fields = ('ship_item', 'this_status')
	

# Register your models here.
admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(ShipStat, ShipStatAdmin)
admin.site.register(ShipmentDetail, ShipmentDetailAdmin)
admin.site.register(StatusDetail, StatusDetailAdmin)