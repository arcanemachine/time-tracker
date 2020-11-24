from rest_framework import serializers

from accounts.models import TimerUser
from tracker.models import Activity, Timer


class TimerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerUser
        fields = ['id', 'username', 'timezone']
        read_only_fields = ['username']

    def to_representation(self, instance):
        return {'id': instance.id,
                'username': instance.username,
                'timezone': instance.timezone.zone}


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name']


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ['id', 'activity', 'start_time', 'stop_time',
                  'last_update_time', 'run_seconds', 'pause_seconds',
                  'is_running']
        read_only_fields = [
            'activity', 'start_time', 'stop_time', 'last_update_time',
            'run_seconds', 'pause_seconds', 'is_running']

    def to_representation(self, instance):
        return {'id': instance.id,
                'activity': instance.activity.pk,
                'start_time': instance.start_time,
                'stop_time': instance.stop_time,
                'last_update_time': instance.last_update_time,
                'run_seconds': instance.run_seconds,
                'pause_seconds': instance.pause_seconds,
                'is_running': instance.is_running}
