from django.db import models

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    zip_code = models.CharField(max_length=10, null=False)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"


class Donor(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    donation_date = models.DateTimeField(auto_now_add=True)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.donor.first_name + " " + self.donor.last_name} - {self.donation_amount}"


class Event(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    publish_time = models.DateTimeField()
    event_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title