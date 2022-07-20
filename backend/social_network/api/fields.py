import base64
import uuid

from django.core.files.base import ContentFile
from rest_framework import serializers

VALIDATION_ERROR_PHONE_NUMBER = 'Номер телефона введен с ошибкой'
PHONE_NUMBER_LENGTH = 12
IMAGE_FILE_NAME = '{user}_image_{unique_end}.{extention}'
VALIDATION_ERROR_BASE64 = 'Неверный формат изображения.'


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


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        """Parse input string, decode, save image."""
        try:
            format, image_string = data.split(';base64,')
            data = ContentFile(
                base64.b64decode(image_string),
                name=IMAGE_FILE_NAME.format(
                    user=self.context['request'].user.username,
                    unique_end=uuid.uuid4().hex[:12],
                    extention=format.split('/')[-1]
                )
            )
        except ValueError:
            raise serializers.ValidationError(VALIDATION_ERROR_BASE64)
        return super().to_internal_value(data)
