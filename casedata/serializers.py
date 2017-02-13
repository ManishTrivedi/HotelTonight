from rest_framework import serializers
from casedata.models import Point, Case

class PointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Point
		fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):

	point=PointSerializer(required=False)
	class Meta:
		model = Case
		fields = ('address', 'request_type', 'opened', 'source', 'status_notes', 'request_details', 'supervisor_district', 'point', 'case_id', 'responsible_agency',
		 'neighborhood', 'category', 'updated', 'status')

	def create(self, validated_data):
		point_data = validated_data.pop('point', None)
		point=None
		if point_data:
			point = Point.objects.create(**point_data)
		case=Case.objects.create(point=point, **validated_data)
		return case	
