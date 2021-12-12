#############################################################################
### NOTE!! If you run this script multiple times you will add ##############
### multiple puppies to the database. That is okay, just the ##############
### ids will be higher than 1, 2 on the subsequent runs ##################
#########################################################################

# Import database info
from flaskdb_model import db, Users

# Create the tables in the database
db.create_all()

# Create new entries in the database
saus = Users('Sammy',35, 'M')
sauk = Users('Kevin',32, 'F')

# Check ids
print(saus.id)
print(sauk.id)

# Ids will get created automatically once we add these entries to the DB
db.session.add_all([saus,sauk])

# Alternative for individual additions:
# db.session.add(saus)
# db.session.add(sauk)

# Now save it to the database
db.session.commit()

# Check the ids
print(saus.id)
print(sauk.id)

all_users = Users.query.all() # list of all users in table
print(all_users)