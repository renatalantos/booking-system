import datetime
from restaurant.models import Table, Booking

def check_availability(table, start_date, end_date):
    avail_list = []
    reservation_list = Booking.objects.filter(table=table)
    for reservation in reservation_list:
        if reservation.start_date > start_date or reservation.end_date < end_date:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)     
