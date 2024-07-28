from scripts.detect_plate import recognize_license_plate
from scripts.detect_green_plate import detect_green_plate
from scripts.log_times import log_entry, log_exit
from scripts.subscriptions import check_membership, add_membership
from scripts.parking_slots import assign_parking_slot
from scripts.notifications import notify_entry, notify_exit

def main():
    image_path = 'images/captured_image.jpg'
    db_path = 'parking_log.db'
    membership_db_path = 'memberships.db'

    # Detect license plates in the image
    image, plates = recognize_license_plate(image_path)
    if not plates:
        print("No license plates detected.")
        return

    # Check for green plates
    green_plate = detect_green_plate(image, plates)
