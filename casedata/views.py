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

    	params = request.GET.dict()
    	filters = get_filters_from_query_string(params)
    	cases = Case.objects.filter(**filters).select_related('point')
    	cases=get_cases_within_radius(params, cases)
    	serializer = CaseSerializer(cases, many=True)
    	return Response(serializer.data)

