#!/usr/bin/env python3
import ipdb

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


np1 = NationalPark("Grand Canyon")
np2 = NationalPark("Gettysburg")
np3 = NationalPark("Dry Tortugas")

v1 = Visitor("Sam")
v2 = Visitor("Arthur")
v3 = Visitor("Julie")

t1 = Trip(v1, np1, "July 1st", "July 3rd")
t2 = Trip(v1, np2, "September 18th", "September 19th")
t3 = Trip(v1, np1, "January 10th", "January 13th")
t4 = Trip(v2, np2, "March 25th", "March 25th")
t5 = Trip(v3, np1, "April 6th", "April 10th")
t6 = Trip(v1, np2, "April 6th", "April 10th")
t7 = Trip(v2, np2, "April 6th", "April 10th")


ipdb.set_trace()
