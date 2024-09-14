from django.db import models

class Participant(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Group(models.Model):
    key = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=3)  # e.g., "USD", "EUR"
    group_information = models.TextField()
    participants = models.ManyToManyField(Participant, related_name='groups')

    def __str__(self):
        return self.group_name

class Expense(models.Model):
    key = models.AutoField(primary_key=True)
    expense_title = models.CharField(max_length=255)
    date = models.DateField()
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_by = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='expenses_paid')
    notes = models.TextField(blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='expenses')

    def __str__(self):
        return f"{self.expense_title} - {self.amount}"

class PaidFor(models.Model):
    key = models.AutoField(primary_key=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='paid_for')
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.participant.name} - {self.amount}"

class Attachment(models.Model):
    key = models.AutoField(primary_key=True)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='attachments')
    document = models.FileField(upload_to='expense_attachments/')

    def __str__(self):
        return f"Attachment for {self.expense.expense_title}"