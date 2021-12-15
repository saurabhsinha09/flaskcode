import configparser

parser = configparser.ConfigParser()
parser.add_section('pgsql')

hostname = input("Host Name: ")
parser.set('pgsql', 'host', hostname)

username = input("User Name: ")
parser.set('pgsql', 'user', username)

password = input("Password: ")
parser.set('pgsql', 'passwd', password)

dbname = input("Database: ")
parser.set('pgsql', 'db', dbname)

fp=open('./myproject/db.ini','w')
parser.write(fp)
fp.close()