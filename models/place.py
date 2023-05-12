#!/usr/bin/python3
'''This module will create a Place class'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''This Class is for managing place objects'''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        '''This Initializes attributes for the place class'''
        super().__init__(*args, **kwargs)
