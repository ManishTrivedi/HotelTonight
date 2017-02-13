from django.apps import AppConfig

class CasedataConfig(AppConfig):
    name = 'casedata'
    def ready(self):
    	from casedata.scheduler import schedule
    	schedule()

