'''Install Wordpress on Ubuntu 12.04'''

from random_mysql_pass import password_generator

username = input("current_username: ")
domain = input("domain: ")
db_name = input("db_name: ")
wp_user = input("wp_user: ")
wp_user_password = password_generator()
wp_admin_password = password_generator()

virtual_host_dir = "/var/www/" + domain + "/public_html/blog/"

output = """

wget http://wordpress.org/latest.tar.gz

tar -xzvf latest.tar.gz


# start of mysql promt
mysql -u root -p

CREATE DATABASE {db_name};

CREATE USER {wp_user}@localhost;

SET PASSWORD FOR {wp_user}@localhost= PASSWORD("{wp_user_password}");

GRANT ALL PRIVILEGES ON {db_name}.* TO {wp_user}@localhost IDENTIFIED BY '{wp_user_password}';

FLUSH PRIVILEGES;

exit
# end of mysql prompt


cp ~/wordpress/wp-config-sample.php ~/wordpress/wp-config.php

sudo nano ~/wordpress/wp-config.php

# // ** MySQL settings - You can get this info from your web host ** //
# /** The name of the database for WordPress */
# define('DB_NAME', '{db_name}');
#
# /** MySQL database username */
# define('DB_USER', '{wp_user}');
#
# /** MySQL database password */
# define('DB_PASSWORD', '{wp_user_password}');


sudo cp -r ~/wordpress/* {virtual_host_dir}

cd {virtual_host_dir}

sudo chown www-data:www-data * -R

sudo usermod -a -G www-data {username}

sudo apt-get install php5-gd

"""
print(output.format(username=username, domain=domain, db_name=db_name, wp_user=wp_user, wp_user_password=wp_user_password, virtual_host_dir=virtual_host_dir))


record = """
|5|
#####
## username: {username}
## domain: {domain}
## db_name: {db_name}
## wp_user: {wp_user}
## wp_user_password: {wp_user_password}
#####
## wp_admin_password: {wp_admin_password}
#####
"""
print(record.format(username=username, domain=domain, db_name=db_name, wp_user=wp_user, wp_user_password=wp_user_password, wp_admin_password=wp_admin_password))
