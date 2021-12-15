from myproject import db
from myproject.models import Vehicle, Owner

print(Owner.query.all())

print(Vehicle.query.all())