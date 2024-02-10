#!/usr/bin/python3

def init(self, city_id, user_id, name, description, number_rooms,
         number_bathrooms, max_guest, price_by_night, latitude,
         longitude, amenity_ids):

    self.city_id = str(city_id)
    self.user_id = str(user_id)
    self.name = str(name)
    self.description = str(description)
    self.number_rooms = int(number_rooms)
    self.number_bathrooms = int(number_bathrooms)
    self.max_guest = int(max_guest)
    self.price_by_night = int(price_by_night)
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.amenity_ids = float(amenity_ids)