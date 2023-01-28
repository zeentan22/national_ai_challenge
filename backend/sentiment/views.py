from rest_framework import generics
from .models import History
from .serializers import HistorySerializer
from .services import SenticGCNService 

class SentimentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()

    def create(self, request, *args, **kwargs):
        # call machine learning service here
        user_input = self.request.data.pop("user_input", None)
        if user_input != None:
            history_data = SenticGCNService().predict(user_input)
            self.request.data["history_data"] = history_data

        return super().create(request, *args, **kwargs)

class SentimentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    lookup_field = "pk"

class SentimentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    lookup_field = "pk"

class SentimentDeleteAPIView(generics.DestroyAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    lookup_field = "pk"