# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

col = "Collecting"
pro = "Processing"
trn = "In Transit"
dln = "Delivering"
dld = "Delivered"

STATUS = (
			(col, 'Collecting'),
			(pro, 'Processing'),
			(trn, 'In Transit'),
			(dln, 'Delivering'),
			(dld, 'Delivered')
		)

class Shipment(models.Model):
	track_id = models.CharField(max_length=10, help_text="unique tracking number", unique=True)
	sender = models.CharField(max_length=100, help_text="sender's first and last name", null=True, blank=True)
	source = models.TextField(help_text="Address, State, Postal Code, County", max_length=150)
	creation_date = models.DateField()

	def __str__(self):
		return self.track_id
		

class ShipmentDetail(models.Model):
	ship_item = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="ship_info", null=True, blank=True)
	receiver = models.CharField(max_length=100, help_text="receiver's first and last name", null=True, blank=True)
	destination = models.TextField(help_text="Address, State, Postal Code, County", max_length=150)
	arrival_date = models.DateField()
	quantity = models.PositiveIntegerField(help_text="From 0-99")
	weight = models.DecimalField(max_digits=4, decimal_places=2, help_text="example: 0.35kg (kilograms)")
	dimensions = models.CharField(max_length=20, help_text="0.9m x 1.5m x 3.0m", null=True, blank=True)

	def __str__(self):
		return self.receiver
		

class ShipStat(models.Model):
	ship_item = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="status", null=True, blank=True)
	
	current_status = models.CharField(max_length=11, choices=STATUS, default=col)
	STATE = (
		('a', 'Active'),
		('h', 'Hold')
		)
	work_state = models.CharField(max_length=1, choices=STATE, default='a')

	def __str__(self):
		return self.current_status
	

class StatusDetail(models.Model):
	det_id = models.AutoField(primary_key=True)
	ship_item = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="status_info", null=True, blank=True)
	this_status = models.CharField(max_length=11, choices=STATUS, null=True, blank=True)

	new_action_date = models.DateField()
	current_location = models.CharField(max_length=30, help_text="State and Country")
	action = models.CharField(max_length=400, help_text="current state of shipment")

	def __str__(self):
		return self.current_location
		
		
		