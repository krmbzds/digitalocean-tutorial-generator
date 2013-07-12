''' How to Install Linux, nginx, MySQL, PHP (LEMP) stack on Ubuntu 12.04 '''

domain = input("domain: ")

output = """
sudo apt-get update

#sudo apt-get install mysql-server

    # Deprecated
    # sudo apt-get install libmysqlclient18=5.5.30-mariadb1~precise mysql-common=5.5.30-mariadb1~precise
    # sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
    # sudo add-apt-repository 'deb http://mirrors.supportex.net/mariadb/repo/5.5/ubuntu precise main'
    # sudo vi /etc/apt/preferences.d/MariaDB

sudo apt-get install python-software-properties
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
sudo add-apt-repository 'deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntu precise main'
sudo apt-get update
sudo apt-get install mariadb-server

    # (Deprecated --Append:
    # Package: *
    # Pin: origin mirrors.supportex.net
    # Pin-Priority: 1000

sudo vi /etc/apt/preferences.d/MariaDB

#  --Append:
# Package: *
# Pin: origin ftp.osuosl.org
# Pin-Priority: 1000


sudo apt-get install nginx

sudo service nginx start

ifconfig eth0 | grep inet | awk '{{ print $2 }}'

sudo apt-get install php5-fpm

sudo nano /etc/php5/fpm/php.ini

# Find the line, cgi.fix_pathinfo=1, and change the 1 to 0.
# cgi.fix_pathinfo=0

sudo service php5-fpm restart

sudo nano /etc/nginx/sites-available/default

#  [...]
# server {{
#         listen   80;
#
#
#         root /usr/share/nginx/www;
#         index index.php index.html index.htm;
#
#         server_name {domain};
#
#         location / {{
#                 try_files $uri $uri/ /index.html;
#         }}
#
#         error_page 404 /404.html;
#
#         error_page 500 502 503 504 /50x.html;
#         location = /50x.html {{
#               root /usr/share/nginx/www;
#         }}
#
#         # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#         location ~ \.php$ {{
#                 #fastcgi_pass 127.0.0.1:9000;
#                 # With php5-fpm:
#                 fastcgi_pass unix:/var/run/php5-fpm.sock;
#                 fastcgi_index index.php;
#                 include fastcgi_params;
#
#         }}
#
# }}
# [...]

# - Add index.php to the index line.
# - Change the server_name from local host to your domain name or IP address (replace the example.com in the configuration)
# - Change the correct lines in “location ~ \.php$ {{“ section

echo '<?php phpinfo(); ?>' > /usr/share/nginx/www/info.php

sudo service nginx restart
"""

print(output.format(domain=domain))
