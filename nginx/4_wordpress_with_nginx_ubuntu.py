''' How to Install Wordpress with nginx on Ubuntu 12.04 '''

from random_mysql_pass import password_generator

username = input("current_username: ")
domain = input("domain: ")
db_name = input("db_name: ")
wp_user = input("wp_user: ")
wp_user_password = password_generator()

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

sudo mkdir -p /var/www

sudo cp -r ~/wordpress/* /var/www

cd /var/www/

sudo chown www-data:www-data * -R

sudo usermod -a -G www-data {username}

sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/{domain}

sudo nano /etc/nginx/sites-available/{domain}

# server {{
#         listen   80;
#
#
#         root /var/www;
#         index index.php index.html index.htm;
#
#         server_name {domain};
#
#         location / {{
#                 try_files $uri $uri/ /index.php?q=$uri&$args;
#         }}
#
#         error_page 404 /404.html;
#
#         error_page 500 502 503 504 /50x.html;
#         location = /50x.html {{
#               root /usr/share/nginx/www;
#         }}
#
#         # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9$
#         location ~ \.php$ {{
#                 #fastcgi_pass 127.0.0.1:9000;
#                 # With php5-fpm:
#                 fastcgi_pass unix:/var/run/php5-fpm.sock;
#                 fastcgi_index index.php;
#                 include fastcgi_params;
#                  }}
#
#
# }}

    # Change the root to /var/www/

    # Add index.php to the index line.

    # Change the server_name from local host to your domain name or IP address (replace the example.com in the configuration)

    # Change the "try_files $uri $uri/ /index.html;" line to "try_files $uri $uri/ /index.php?q=$uri&$args;" to enable Wordpress Permalinks with nginx

    # Uncomment the correct lines in “location ~ \.php$ {{“ section

sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/{domain}

sudo rm /etc/nginx/sites-enabled/default

sudo apt-get install php5-mysql

sudo service nginx restart

"""
print(output.format(username=username, domain=domain, db_name=db_name, wp_user=wp_user, wp_user_password=wp_user_password))


record = """
|4|
#####
## username: {username}
## domain: {domain}
## db_name: {db_name}
## wp_user: {wp_user}
## wp_user_password: {wp_user_password}
#####
"""
print(record.format(username=username, domain=domain, db_name=db_name, wp_user=wp_user, wp_user_password=wp_user_password))
