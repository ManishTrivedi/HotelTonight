from apscheduler.scheduler import Scheduler
import requests
from casedata.serializers import CaseSerializer


def get_case_data():
	try:
		r=requests.get('http://data.sfgov.org/resource/vw6y-z8j6.json')
		serializer=CaseSerializer(data=r.json(), many=True)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
	except Exception as e:
			print(e)

def schedule():
	# Start the scheduler
	sched = Scheduler()
	sched.start()
	sched.add_cron_job(get_case_data, minute=38, hour=23)