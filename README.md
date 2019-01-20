#udacity_catalog_project
This is the project of a web application of Udacity Backend Nanodegree which is deployed in AWS LightSail.

So this project includes a build of a website for users to add, edit and delete items.

The IP is 13.236.121.205 with the port at 80.

So the whole link is 13.236.121.205:80. You can paste this into your browser for further review.

Here is the list of software installed in AWS LightSail for configuration.

1. sudo apt-get install apache2
2. sudo apt-get install libapache2-mod-wsgi-py3 python3-dev
3. sudo apt-get install python3-pip python3-flask python3-sqlalchemy python3-psycopg2
4. pip3 install mod_wsgi
5. sudo apt-get install git
6. sudo apt-get install postgresql
7. sudo pip3 install oauth2client requests httplib2

Configurations made:
1. Firewall configuration
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 2200/tcp
sudo ufw allow 80/tcp
sudo ufw allow 123/udp

2. Timezone for UTC
sudo dpkg-reconfigure tzdata

3. grader user with sudo access
a. sudo adduser grader
b. sudo visudo
c. after b, add 'grader  ALL=(ALL:ALL) ALL' under 'root    ALL=(ALL:ALL) ALL'

4. wsgi configuration
a. project.wsgi file
b. config file at /etc/apache2/sites-available/catalog.conf

5. database user setup
a. create user catalog with access to categoriesitem.db
b. in database_setup.py & project.py: 
    engine = create_engine('postgresql://catalog:catalog@localhost/catalog')


First, we run:
python database_setup.py
to build the database.

Second, we run:
python addallitems.py
to add all info into the database.

When running the whole application, we run
python project.py,
then open the browser in localhost:80 to the main page.

Click on login button to login via google.

Url: localhost:5000/catalog/<catalog_name>/items/
To see all items under one catalog

Url:  localhost:5000/catalog/<item_name>/
To see the description for one specific item

Url: localhost:5000/catalog.json
To obtain all data in json format
