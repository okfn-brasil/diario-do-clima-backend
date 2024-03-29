from rest_framework import serializers
from .models import PlanSubscription


class PlanSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanSubscription
        fields = (
            'plan',
            'pagseguro_code',
            'trial_end_at',
        )
