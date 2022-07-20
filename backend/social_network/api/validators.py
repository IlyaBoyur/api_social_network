from rest_framework import serializers


class MaxSizeValidator:
    """Check max size."""
    message = 'The size is too big.'

    def __init__(self, many_field, subfield, max_size, message=None):
        self.many_field = many_field
        self.subfield = subfield
        self.max_size = max_size
        self.message = message or self.message

    def __call__(self, attrs):
        size_many_field = sum(
            attr[self.subfield].size for attr in attrs[self.many_field]
        )
        if size_many_field >= self.max_size:
            raise serializers.ValidationError({
                self.many_field: self.message.format(size=size_many_field,
                                                     max_size=self.max_size,)
            })
