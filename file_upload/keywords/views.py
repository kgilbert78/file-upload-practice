from rest_framework import viewsets
from rest_framework.response import Response
from .models import FileWithKeywords, Keyword
from .serializer import FileWithKeywordsSerializer, KeywordSerializer

# Create your views here.
class FileWithKeywordsViewSet(viewsets.ModelViewSet):
    serializer_class = FileWithKeywordsSerializer

    def get_queryset(self):
        files = FileWithKeywords.objects.all()
        return files

    def add_keywords(self, keyword_data):
        print(keyword_data)
        # handling postman input formatted as ["keyword1", "keyword2", "keyword3"]
        keyword_list = keyword_data.strip('"]["').split('", "')
        print(keyword_list, type(keyword_list))
        # add keywords in request that aren't already in the db keywords
        for each_keyword in keyword_list:
            inDB = Keyword.objects.filter(associated_keyword=each_keyword).exists()
            print(each_keyword, inDB)
            if inDB == False:
                new_keyword = Keyword.objects.create(associated_keyword=each_keyword)
                new_keyword.save()

    def create(self, request, *args, **kwargs):
        data = request.data

        # print(data)

        new_file = FileWithKeywords.objects.create(
            keyword_doc=data["document"],
            
        )
        new_file.save()


        self.add_keywords(data["keyword"])
        
        keyword_list = data["keyword"].strip('"]["').split('", "')
        # associate the keywords to the new file by keyword text
        for each_keyword in keyword_list:
            keyword_obj = Keyword.objects.get(associated_keyword=each_keyword)
            # if duplicate keywords are in the db, this line will error:
            # file_api.models.Keyword.MultipleObjectsReturned: get() returned more than one Keyword -- it returned 4!

            new_file.keyword.add(keyword_obj)

        serializer = FileWithKeywordsSerializer(new_file)
        return Response(serializer.data)