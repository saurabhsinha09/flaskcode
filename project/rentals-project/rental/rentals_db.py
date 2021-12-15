#################
####Database#####
#################
from sqlalchemy.orm import load_only
from rentals import db, Owner, Vehicle, Price

print(Owner.query.all())

name = Owner.query.get(1)
print(name.name)

print(Vehicle.query.all())


#rental = Price.query.filter((vehicle_type == 'bike') and (duration == 'month')).first()
rental = Price.query(Price.amount).filter(Price.duration=="month").filter(Price.vehicle_type=="bike").all()
print(rental)

