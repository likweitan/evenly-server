from rest_framework import serializers
from .models import Participant, Group, Expense, PaidFor, Attachment

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['key', 'name']

class GroupSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['key', 'group_name', 'currency', 'group_information', 'participants']

class PaidForSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidFor
        fields = ['key', 'participant', 'amount']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['key', 'document']

class ExpenseSerializer(serializers.ModelSerializer):
    paid_for = PaidForSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Expense
        fields = ['key', 'expense_title', 'date', 'category', 'amount', 'paid_by', 'notes', 'group', 'paid_for', 'attachments']