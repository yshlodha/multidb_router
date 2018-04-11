# multidb_router

*All the below instructions are done on Ubuntu Machine. If you are using different OS then please search the alterantive for performing below instructions.*

#####Configure Your machine with PostgresSQL and MySQL

- This is the link to install (Postgres)[https://www.postgresql.org/download/linux/ubuntu/]
- This is the link to install (MySQL)[https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/]

Don't forget to configure Postgres and MySQL with proper user permission.

#####Create Database on both Postgres and MySQL
*In Terminal*

* Postgres:
>sudo -i -u postgres
>psql
>CREATE DATABASE user_db
>CREATE DATABASE database1;
>CREATE DATABASE database2;

if you are going to use different user to access this databases then run this comman where <username> will be the user which will going to access these databases:

>grant all privileges on database database1 to <username>;
>grant all privileges on database database2 to <username>;

exits from postgres.

* MySQL
>mysql -u <user> -p

this will prompt for password enter the valid password for user.

mysql console will open:

>CREATE DATABASE database3;
>CREATE DATABASE database4;
>CREATE DATABASE database5;

exits from MySQL.


#####Virtualenv Configuration

Install virtualenv by following instructions if already not exists in your machine: (Virtualenv) [https://virtualenv.pypa.io/en/stable/installation/]


*In terminal*
>virtualenv -p python3.4 multidb_routerenv

>cd multidb_routerevn/

>source bin/activate


####Clone app from github

>git clone https://github.com/yshlodha/multidb_router.git

>cd multidb_router/

>pip install -r requirements.txt

#####Make Settings file according to Your Host Configuration

>cd multidb_router/

>open settings.py and prod_settings.py

Edit DATABASES settings For USER, PASSWORD, HOST, And PORT

>Modifiy this variable as per your database username and password and host and port your dbs running on.

NOW Edit following settings as per your email backends and smtp server:
 
>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
>EMAIL_USE_TLS = True
>EMAIL_HOST = 'smtp.sendgrid.net'
>EMAIL_PORT = 587
>EMAIL_HOST_USER = ''
>EMAIL_HOST_PASSWORD = ''

>DEFAULT_EMAIL_ADDRESS = ''

Now Modifiy DOMAIN:

for prod_settings.py:

> set it the the domain name and port production is pointed to.

for local environment i.e. settings.py:

>you can keep as it on localhost:8000 or may change if you want to run it on some ip or on some domain.


>cd ../
>ls
and see if mamange.py is in the directory if it is you are in correct directory.

#####Run Migrations
>python manage.py migrate
>python manage.py migrate --database=db_1
>python manage.py migrate --database=db_2
>python manage.py migrate --database=db_3
>python manage.py migrate --database=db_4
>python manage.py migrate --database=db_5

load some data fixtures:
>python manage.py loaddata mutlidb_router_app/fixtures/db_choices.json


#####Create Super user to perform the admin tasks.

>python manage.py createsuperuser

this will prompt some input for admin user.


#####Run server

For local Envirnonment:

>python manage.py runserver --settings=mutlidb_router.settings

for Production Environment:

>python manage.py runserver --settings=multidb_router.prod_settings


#####Perform User Creation by Admin

go to localhost:8000/admin or whatever domain you are running your server with "/admin"

-login page opens

-Enter your superuser credentials for login.

-You will See two options Groups and User.

-with User you will '+' Add button.

-click the add button a user creation page opens.

-fill the fields to create user in the bottom of this you will see the list of databases.

-Select the databases you want to give access to the user you are creating.

- After this click the Save button at the bottom.

-once the User is save a email will sent on its email as per the email backend you are using.

#####After User receives Email

- Email will contains the username and password with a link for login on site.

-this link will be "domain/app/login"

-User will go on this link and enter its credentials received on email.

-After successfully logged in user will see home page.

-On home page user will finds 2 links

>  1. See Your Product List HERE!!

>  2. Add New Product HERE!!

- First link is to see the product added by user

- Second link is to add new product in selected database.

####For Admin Page to see all User product.

Go to "domain/app/login/"

-Enter the Admin credentials i.e. credentials of superuser.

- you will see admin page which will contains the list of users and the databases which contains the products with product name.

- The data for each user is separated in tabular structure.

- Every User data table contains two link one is beside User Name  which says: "click Here to add New product!!"

- And beside every product in details column : "click Here!!"

-When admin clicks to add new product he will redirected to new page to add new product on that user.

-When admin click on details on "click Here" he will redirected to details page will contain product name, db in which product is kept and category where it belongs. After from this this page also contains a 'delete' button by click on delete button that product will get delted from the database it is kept. and redirect backs to the admin all user list page. 



#####TEST CASES.

I will Update it SOON...
