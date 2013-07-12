'''Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu'''


from random_mysql_pass import password_generator

mysql_root_pass = password_generator()

output = """
# install Apache
sudo apt-get update
sudo apt-get install apache2

# verify the installation
ifconfig eth0 | grep inet | awk '{ print $2 }'

# install MySQL
sudo apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql

# activate MySQL
sudo mysql_install_db

# run setup script (enter root pass; [N]; [Y]*4)
sudo /usr/bin/mysql_secure_installation


# install PHP ([Y]*2)
sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt

#add php to the directory index, to serve the relevant php index files
sudo nano /etc/apache2/mods-enabled/dir.conf

    <IfModule mod_dir.c>

              DirectoryIndex index.php index.html index.cgi index.pl index.php index.xhtml index.htm

    </IfModule>

# test your PHP installation
sudo nano /var/www/info.php

    <?php
    phpinfo();
    ?>
"""

record = """
|3|
####
## mysql_root_pass: {mysql_root_pass}
####
"""

print(output)
print(record.format(mysql_root_pass=mysql_root_pass))
