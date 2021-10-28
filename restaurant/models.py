from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Booking(models.Model):
    """
    Class to represent booking model
    in database and for booking form.
    """
    user = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=15, null=True)
    reservation_date_and_time = models.DateTimeField(null=True)

    def validate_date(reservation_date_and_time):
        """
        Function to validate date so that
        booking date is not in the past.
        """
        if reservation_date_and_time < timezone.now():
            raise ValidationError("Date cannot be in the past")
    reservation_date_and_time = models.DateTimeField(null=True, blank=True, validators=[validate_date])
    number_of_customers = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=15, null=True)

    class Meta:
        """
        Class container with metadata
        attached to the model.
        """
        unique_together = ('user', 'customer_name',
                           'reservation_date_and_time')
        ordering = ["-reservation_date_and_time"]

    def __str__(self):
        """
        Function to return object model
        items as string.
        """
        return f' Customer {self.customer_name} has made a booking\
                          for {self.number_of_customers} customers\
                          for {self.reservation_date_and_time}.'
