from rest_flex_fields.serializers import FlexFieldsSerializerMixin

from NEMO.apps.sensors.models import SensorData
from NEMO.serializers import ModelSerializer


class SensorDataSerializer(FlexFieldsSerializerMixin, ModelSerializer):
    class Meta:
        model = SensorData
        fields = "__all__"
        expandable_fields = {}
