
from restaurant.models import Booking


def check_availability(start_date, end_date):
    avail_list = []
    reservation_list = Booking.objects.filter()
    for reservation in reservation_list:            
        if reservation.start_date > start_date or reservation.end_date < end_date:
          
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list) 





         
    