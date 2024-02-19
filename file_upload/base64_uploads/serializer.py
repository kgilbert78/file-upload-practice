from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
# for _ in: raise ValidationError(_(f"Invalid type. This is not an base64 string: {type(base64_data)}"))
from django.utils.translation import gettext as _
from rest_framework import serializers
from drf_extra_fields.fields import Base64FileField, Base64ImageField
import filetype
import base64
import binascii
import uuid
from .models import FileUpload

# attempt to impliment code from https://medium.com/@pykhaled/how-to-handle-files-in-django-rest-framework-20afbe234956

## definition
class Base64FileField(Base64FileField):
    """
    A custom serializer field to handle base64-encoded files.
    """
    ALLOWED_MIME_TYPES = {
        'image/jpeg': 'jpg',
        'image/png': 'png',
        'application/pdf': 'pdf',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': 'docx',
    }

    ALLOWED_TYPES = ['pdf', 'docx', 'jpg', 'jpeg', 'png']

    def get_file_extension(self, filename, decoded_file):
        extension = filetype.guess_extension(decoded_file)
        return extension

    def to_internal_value(self, data):
        if isinstance(data, str):
            return super().to_internal_value(data)
        return data
    
class Base64FieldMixin:
    EMPTY_VALUES = (None, "", [], (), {})
    @property
    def ALLOWED_TYPES(self):
        raise NotImplementedError
    @property
    def INVALID_FILE_MESSAGE(self):
        raise NotImplementedError
    @property
    def INVALID_TYPE_MESSAGE(self):
        raise NotImplementedError
    def __init__(self, *args, **kwargs):
        self.trust_provided_content_type = kwargs.pop("trust_provided_content_type", False)
        self.represent_in_base64 = kwargs.pop("represent_in_base64", False)
        super().__init__(*args, **kwargs)
    def to_internal_value(self, base64_data):
        # Check if this is a base64 string
        if base64_data in self.EMPTY_VALUES:
            return None
        if isinstance(base64_data, str):
            file_mime_type = None
            # Strip base64 header, get mime_type from base64 header.
            if ";base64," in base64_data:
                header, base64_data = base64_data.split(";base64,")
                if self.trust_provided_content_type:
                    file_mime_type = header.replace("data:", "")
            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(base64_data)
            except (TypeError, binascii.Error, ValueError):
                raise ValidationError(self.INVALID_FILE_MESSAGE)
            # Generate file name:
            file_name = self.get_file_name(decoded_file)
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)
            if file_extension not in self.ALLOWED_TYPES:
                raise ValidationError(self.INVALID_TYPE_MESSAGE)
            complete_file_name = file_name + "." + file_extension
            data = SimpleUploadedFile(
                name=complete_file_name,
                content=decoded_file,
                content_type=file_mime_type
            )
            return super().to_internal_value(data)
        raise ValidationError(_(f"Invalid type. This is not an base64 string: {type(base64_data)}"))
    def get_file_extension(self, filename, decoded_file):
        raise NotImplementedError
    def get_file_name(self, decoded_file):
        return str(uuid.uuid4())
    def to_representation(self, file):
        if self.represent_in_base64:
            # If the underlying ImageField is blank, a ValueError would be
            # raised on `open`. When representing as base64, simply return an
            # empty base64 str rather than let the exception propagate unhandled
            # up into serializers.
            if not file:
                return ""
            try:
                with file.open() as f:
                    return base64.b64encode(f.read()).decode()
            except Exception:
                raise OSError("Error encoding file")
        else:
            return super().to_representation(file)

## usage
class FileUploadSerializer(serializers.Serializer):
    file = Base64FileField(required=False)
    class Meta:
        model = FileUpload
        fields = "__all__" # ['id', 'doc']