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

    # ENDPOINT http://localhost:8000/cases/
    # Handles all the following 

    # GET /cases
	# Returns all cases

	# GET /cases?since=1398465719
	# Returns cases opened since UNIX timestamp 1398465719

	# GET /cases?status=open
	# Returns cases that are in open state.

	# GET /cases?category=General%20Requests
	# Returns cases that belong to "General Requests" category

	# GET /cases?near=37.77,-122.48
	# Returns cases that were created within 5 mile radius of lat=37.77 and lng=-122.48

	# GET /cases.json?near=37.77,-122.48&status=open&category=General%20Requests
    def list(self, request):

    	params = request.GET.dict()
    	filters = get_filters_from_query_string(params)
    	cases = Case.objects.filter(**filters).select_related('point')
    	cases=get_cases_within_radius(params, cases)
    	serializer = CaseSerializer(cases, many=True)
    	return Response(serializer.data)

