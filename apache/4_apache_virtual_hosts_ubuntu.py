'''Apache Virtual Hosts on Ubuntu 12.04 LTS'''


domain = input("domain: ")

output = """
sudo mkdir -p /var/www/{domain}/public_html

sudo chown -R $USER:$USER /var/www/{domain}/public_html 

sudo chmod -R 755 /var/www

sudo nano /var/www/{domain}/public_html/index.html

    <html>
      <head>
        <title>www.{domain}</title>
      </head>
      <body>
        <h1>Success: You Have Set Up a Virtual Host</h1>
      </body>
    </html>


sudo cp /etc/apache2/sites-available/default /etc/apache2/sites-available/{domain}

sudo nano /etc/apache2/sites-available/{domain}

    ServerName {domain}

    <VirtualHost *:80>
            ServerAdmin webmaster@{domain}
            ServerName {domain}
            ServerAlias www.{domain}
      [...]

    DocumentRoot /var/www/{domain}/public_html

sudo a2ensite {domain}

sudo service apache2 restart
"""

print(output.format(domain=domain))

