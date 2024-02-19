from rest_framework import viewsets
from rest_framework.response import Response
from .models import FileUpload
from .serializer import FileUploadSerializer

# Create your views here.
class FileUploadViewSet(viewsets.ModelViewSet):
    serializer_class = FileUploadSerializer

    queryset = FileUpload.objects.all()

    # without manual POST request handling, it seems you can't submit the request as JSON
    def create(self, request, *args, **kwargs):
        data = request.data

        # print(data)

        new_file = FileUpload.objects.create(
            doc=data["document"],
        )
        new_file.save()


        serializer = FileUploadSerializer(new_file)
        return Response(serializer.data)