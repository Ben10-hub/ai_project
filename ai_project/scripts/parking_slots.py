def assign_parking_slot(license_plate, membership_type):
    if membership_type == 'Gold':
        return 'VIP-Slot-1'
    else:
        return 'Regular-Slot-1'
