# Now that the table has been created by running
# flaskdb_model and flaskdb_setup we can run CRUD commands
from flaskdb_model import db, Users

###### CREATE ############
shas = Users('Harry',3, 'M')
gans = Users('Glauss', 80, 'M')
db.session.add(gans)
db.session.add(shas)
db.session.commit()

###### READ ##############
# Note lots of ORM filter options here.
# filter(), filter_by(), limit(), order_by(), group_by()
# Also lots of executor options
# all(), first(), get(), count(), paginate()
all_users = Users.query.all() # list of all users in table
print(all_users)
print('\n')

# Grab by id
user_one = Users.query.get(1)
print(user_one)
print(user_one.age)
print('\n')

# Filters
user_shas = Users.query.filter_by(name='Harry') # Returns list
print(user_shas.first())
print('\n')

###### UPDATE ############
# Grab your data, then modify it, then save the changes.
user_saus = Users.query.get(1)
user_saus.age = 36
db.session.add(user_saus)
db.session.commit()

###### DELETE ############
user_gans = Users.query.get(3)
db.session.delete(user_gans)
db.session.commit()

# Check for changes:
all_users = Users.query.all() # list of all users in table
print(all_users)
