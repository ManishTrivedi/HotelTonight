from apscheduler.scheduler import Scheduler
import requests
from casedata.serializers import CaseSerializer
from datetime import datetime, timedelta

#Function to get cases and save it in db
def get_case_data():
	try:
		r=requests.get('http://data.sfgov.org/resource/vw6y-z8j6.json')
		case_list = r.json()
		new_case_list = []
		for case in case_list:
			case_time = datetime.strptime(case['opened'],'%Y-%m-%dT%H:%M:%S')
			if case_time > (datetime.utcnow() - timedelta(days=3)):
				new_case_list.append(case)

		serializer = CaseSerializer(data=new_case_list, many=True)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
	except Exception as e:
			print(e)

def schedule():
	# Start the scheduler
	sched = Scheduler()
	sched.start()
	sched.add_cron_job(get_case_data, minute=0, hour=0)