import datetime
# Air Management

class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []


class Airplane:
    def __init__(self, id, current_location, company):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = []

    def fly(self, destination):
        pass

    def location_on_date(self, date):
        pass

    def available_on_date(self, date, location):
        pass


class Flight:
    def __init__(self, date, destination, origin