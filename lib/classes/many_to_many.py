class NationalPark:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<NationalPark: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            if type(new_name) == str and 3 <= len(new_name):
                self._name = new_name
            else:
                raise Exception("Name must be a string with at least 1 and up to 15 characters.")
        else:
            raise Exception("Cannot rename National Park.")

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass




class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def __repr__(self):
        return f"<Trip: {self.visitor.name} visited {self.national_park.name} from {self.start_date} to {self.end_date}>"

    @classmethod
    def date_checker(cls, date):
        month_and_day = date.split(" ")
        if len(month_and_day) != 2:
            return False
        day = month_and_day[1]
        if int(day[0]) == int:
            return False
        else:
            return True

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_start_date):
        if (type(new_start_date) == str) and (len(new_start_date) >= 7) and Trip.date_checker(new_start_date):
            self._start_date = new_start_date
        else:
            raise Exception("Start date must be in the form of: 'September 1st'.")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, new_end_date):
        if (type(new_end_date) == str) and (len(new_end_date) >= 7) and Trip.date_checker(new_end_date):
            self._end_date = new_end_date
        else:
            raise Exception("End date must be in the form of: 'September 1st'.")

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, new_visitor):
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            raise Exception("Visotor must be an instance of Visitor class.")

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, new_national_park):
        if isinstance(new_national_park, NationalPark):
            self._national_park = new_national_park
        else:
            raise Exception("National Park must be an instance of NationalPark class.")




class Visitor:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Visitor: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) == str and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception("Name must be a string with at least 1 and up to 15 characters.")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        pass