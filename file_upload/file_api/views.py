from rest_framework import viewsets
from rest_framework.response import Response
from .models import File
from .serializer import FileSerializer

# Create your views here.
class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer

    queryset = File.objects.all()

    # without manual POST request handling, it seems you can't submit the request as JSON
    def create(self, request, *args, **kwargs):
        data = request.data

        # print(data)

        new_file = File.objects.create(
            document=data["document"],
        )
        new_file.save()


        serializer = FileSerializer(new_file)
        return Response(serializer.data)