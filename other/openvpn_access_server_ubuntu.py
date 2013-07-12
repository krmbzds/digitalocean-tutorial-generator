''' How to Install OpenVPN Access Server on Ubuntu 12.04 '''

from random_mysql_pass import password_generator
password = password_generator()

terminate = 0

# Constants;
version = '1.8.4'
fln_32bit = 'openvpn-as-' + version + '-Ubuntu10.i386.deb'
fln_64bit = 'openvpn-as-' + version + '-Ubuntu10.amd_64.deb'
url_32bit = 'http://swupdate.openvpn.org/as/' + fln_32bit
url_64bit = 'http://swupdate.openvpn.org/as/' + fln_64bit

# Input Architecture and IP Address
arch = input("Architecture [32bit/64bit]: ")
ip_address = input("IP Address of Cloud Server: ")

if ("32" in arch) and not ("64" in arch):
    arch = url_32bit
    dpkg = fln_32bit
elif "64" in arch and not ("32" in arch):
    arch = url_64bit
    dpkg = fln_64bit
else:
    terminate = 1


output = """

# Login as root
sudo su

# Fetch package
sudo wget {arch}

# Install
dpkg -i "{dpkg}"

# Change Pass of 'openvpn' User
sudo passwd openvpn

|OpenVPN|
#########
## username: openvpn
## password: {password}
#####
## Admin  UI: https://{ip_address}:943/admin
## Client UI: https://{ip_address}:943/
#########

"""

if terminate == 0:
    print(output.format(arch=arch, dpkg=dpkg, password=password, ip_address=ip_address))
elif terminate == 1:
    raise("Wrong Input")
else:
    raise("Unknown Error")

if password:
    del(password)
