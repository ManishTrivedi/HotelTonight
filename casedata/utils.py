from enum import Enum
from datetime import datetime
from geopy.distance import vincenty

class Status(Enum):
	OPEN = 1
	CLOSED = 2

def format_status(status):
	if (status.upper() == Status.OPEN.name):
		return 'Open'
	elif (status.upper() == Status.CLOSED.name):	
		return 'Closed'

#Date time conversion from epoch to unix
#This is used filter jobs from date to current time
def format_datetime(since):
	datetime_from=datetime.fromtimestamp(float(since)).strftime('%Y-%m-%d %H:%M:%S.%f')
	datetime_to=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')
	return [datetime_from, datetime_to]

#Add filters according to the query string parameters
def get_filters_from_query_string(params):
	filters = {}
	status = params.get('status', None)
	category = params.get('category', None)
	since = params.get('since', None)

	if status:
		filters['status'] = format_status(status)
	if category:
		filters['category'] = category
	if since:
		filters['opened__range'] = format_datetime(since)
	return filters

#Using pythons geopy package to get distance based on latitude and longitude.
#If near filter present, get jobs within 5 mile radius, else return all jobs
def get_cases_within_radius(params, cases):

	location = params.get('near', None)
	if not location:
		return cases

	latitude=location.split(',')[0]	
	longitude = location.split(',')[1]

	nearby_cases=[]
	for case in cases:
		center = (float(latitude), float(longitude))
		if case.point:
			case_location = (float(case.point.latitude), float(case.point.longitude))
			if vincenty(center, case_location).miles <= 5:
				nearby_cases.append(case)
	return nearby_cases		



	
