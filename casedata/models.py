from django.db import models
from django.utils import timezone

class Point(models.Model):
	id = models.AutoField(primary_key=True)
	latitude = models.CharField(max_length=50)
	human_address = models.CharField(max_length=200)
	needs_recoding = models.BooleanField(default=False)
	longitude = models.CharField(max_length=50)

class Case(models.Model):
	id = models.AutoField(primary_key=True)
	address = models.CharField(max_length=200, default='')
	request_type = models.CharField(max_length=200, default='')
	opened = models.DateTimeField(default=timezone.now)
	source = models.CharField(max_length=200, default='')
	status_notes = models.CharField(max_length=300, default='')
	request_details = models.CharField(max_length=200, default='')
	supervisor_district = models.PositiveIntegerField(default=0)
	point = models.ForeignKey(Point, null=True, blank=True)
	case_id = models.PositiveIntegerField(default=0)
	responsible_agency = models.CharField(max_length=200, default='')
	neighborhood = models.CharField(max_length=200, default='')
	category = models.CharField(max_length=200, default='')
	updated = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=200, default='')