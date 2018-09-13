from rest_framework import serializers

from . import models

class SleepSerializer(serializers.ModelSerializer):

	class Meta:
		#to make a field read only
		#extra_kwargs = {
		#	'email': {'write_only': True}
		#}
		fields = (
			'id',
			'bedtime',
			'wakeup_time',
			'quality',
			'description',
			'sleep_duration'
		)
		model = models.Sleep

class DisciplineSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id'
			'date',
			'discipline',
		)
		model = models.Discipline
