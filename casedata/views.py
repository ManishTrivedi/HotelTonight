from rest_framework import viewsets
from casedata.models import Case
from casedata.serializers import CaseSerializer
from rest_framework.response import Response
from rest_framework.decorators import list_route
import requests
from casedata.utils import *

class CaseViewSet(viewsets.ViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def list(self, request):
  
    	# try:
    	# 	r=requests.get('http://data.sfgov.org/resource/vw6y-z8j6.json')
    	# 	serializer=CaseSerializer(data=r.json(), many=True)
    	# 	if serializer.is_valid(raise_exception=True):
    	# 		serializer.save()
    	# except Exception as e:
    	#     	print(e)

    	params = request.GET.dict()
    	filters = get_filters_from_query_string(params)
    	#cases = Case.objects.all().select_related('point')
    	import pdb
    	#pdb.set_trace()
    	#status=params.get('status', None)
    	#category=params.get('category', None)
    	#status=params.get('status', None)

    	cases = Case.objects.filter(**filters).select_related('point')
    	#cases = Case.objects.filter(status=status, category=category).select_related('point')
    	cases=get_cases_within_radius(params, cases)
    	serializer = CaseSerializer(cases, many=True)
    	return Response(serializer.data)

    #@list_route(methods=['get'])


