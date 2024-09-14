from rest_framework import viewsets
from .models import Participant, Group, Expense, PaidFor, Attachment
from .serializers import ParticipantSerializer, GroupSerializer, ExpenseSerializer, PaidForSerializer, AttachmentSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class PaidForViewSet(viewsets.ModelViewSet):
    queryset = PaidFor.objects.all()
    serializer_class = PaidForSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer