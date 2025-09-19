from django.db import models
from borrower.models import Borrower


# Create your models here.

DOCUMENT_CATEGORY_CHOICES = [
    ('identity', 'Proof of Identity'),
    ('address', 'Proof of Address'),
]

DOCUMENT_CHOICES = [
    # Identity
    ("NIN", "National ID Card / NIN Slip"),
    ("PASSPORT", "International Passport"),
    ("PHOTO", "Passport Photograph"),
    ("DL", "Driver's License"),

    # Address
    ("PVC", "Permanent Voter's Card"),
    ("UTILITY", "Utility Bill"),

]

# Document Model
class Document(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name='document_details', default=1)
    document_category = models.CharField(max_length=50, choices=DOCUMENT_CATEGORY_CHOICES, default='identity')
    document_type = models.CharField(max_length=150, choices=DOCUMENT_CHOICES, default='NIN')
    document_image = models.ImageField(blank=True, null=True, upload_to='business_files/')
    created_at = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_document_type_display()}-{self.get_document_category_display()}->({self.borrower})"