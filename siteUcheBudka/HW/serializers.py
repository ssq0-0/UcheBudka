from rest_framework import serializers
from .models import HW
from django.utils import timezone


class HWSerializers(serializers.Serializer):
    # class Meta:
    #     model = HW
    #     fields = '__all__'
    school_subject = serializers.CharField(max_length=50)
    task_text = serializers.CharField()
    fact_answer = serializers.CharField()
    # publish_time = serializers.DateTimeField()

    def create(self, validated_data):
        return HW.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.school_subject = validated_data.get('school_subject')
        instance.task_text = validated_data.get('task_text')
        instance.fact_answer = validated_data.get('fact_answer')
        instance.publish_time = timezone.now()
        instance.save()
        return instance

