from rest_framework import serializers

VALIDATION_ERROR_PHONE_NUMBER = 'Номер телефона введен с ошибкой'
PHONE_NUMBER_LENGTH = 12
class PhoneNumberField(serializers.CharField):
    def to_representation(self, value):
        value = str(value)
        value = ('+' + value[0] + '(' + value[1:4] + ')'
                 + value[4:7] + '-' + value[7:9] + '-' + value[9:11])
        return super().to_representation(value)

    def to_internal_value(self, data):
        if PHONE_NUMBER_LENGTH != len(data):
            raise serializers.ValidationError(VALIDATION_ERROR_PHONE_NUMBER)
        try:
            data = int(data.lstrip('+'))
        except ValueError:
            raise serializers.ValidationError(VALIDATION_ERROR_PHONE_NUMBER)
        return super().to_internal_value(data)
