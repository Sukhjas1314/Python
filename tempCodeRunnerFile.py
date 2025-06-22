def get_fare(self):
    vehicle_fare = super().get_fare()
    maintainence_fare = vehicle_fare * 0.1
    total_fare = maintainence_fare + vehicle_fare
    return total_fare