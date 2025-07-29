from django.db import models

# Create your models here.
class Documents(models.Model):
    document_name = models.CharField(verbose_name='Document Name', max_length=150)
    document_folder = models.CharField(verbose_name='Document Folder', max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.document_name



    ...
class KYC(models.Model):
    # statuses and remarks this reflects the customer's
    #  verification progress.


    KYC_STATUS_CHOICES= [
        ('pending', 'Pending'),
        ('in_review', 'In Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('resubmission_required', 'Resubmission Required'),
        ]

    status = models.CharField(choices=KYC_STATUS_CHOICES, max_length=30, default='pending')
    # borrower = models.ForeignKey('Borrower', on_delete=models.CASCADE)
    aadhar_number = models.CharField(unique=True, max_length=30)
    pan_number = models.CharField(unique=True, max_length=30)
    documents = models.ManyToManyField(Documents)
    completion_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    remark = models.TextField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = 'KYC Document'
        verbose_name_plural = 'KYC Documents'
    
    def __str__(self):
        return f"KYC for Borrower {self.borrower_id} - {self.status}"