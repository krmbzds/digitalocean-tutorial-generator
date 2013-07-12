''' How to Set Up nginx Virtual Hosts (Server Blocks) on Ubuntu 12.04 LTS '''

domain = input("domain: ")

output = """
sudo apt-get install nginx

sudo mkdir -p /var/www/{domain}/public_html

sudo chown -R www-data:www-data /var/www/{domain}/public_html

sudo chmod 755 /var/www

echo '<html><head>
<title>www.{domain}</title></head><body><h1>Success: You Have Set Up a Virtual Host</h1></body></html>' > /var/www/{domain}/public_html/index.html

sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/{domain}

sudo nano /etc/nginx/sites-available/{domain}

#  server {{
#         listen   80; ## listen for ipv4; this line is default and implied
#         #listen   [::]:80 default ipv6only=on; ## listen for ipv6
#
#         root /var/www/{domain}/public_html;
#         index index.html index.htm;
#
#         # Make site accessible from http://localhost/
#         server_name {domain};
# }}

sudo ln -s /etc/nginx/sites-available/{domain} /etc/nginx/sites-enabled/{domain}

sudo rm /etc/nginx/sites-enabled/default

sudo service nginx restart

"""

print(output.format(domain=domain))

