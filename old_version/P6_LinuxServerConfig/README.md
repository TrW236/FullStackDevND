# Linux Server Configuration

## First step
* Enable the public IP on Lightsail.
* Try to connect the Server through the ssh. `ssh ubuntu@<IP>`
    * `ubuntu@<IP>: Permission denied (publickey).`
    * This means that the server has responded
* Connect the server using key
    * Download the default key file from Lightsail
    * change the key permission to 700: `sudo chmod 700 <path_to_key>`
    * ssh login using the key: `ssh -i <path_to_key> ubuntu@<IP>`
        * ssh connection successfully

## change the default ssh port
* `sudo vi /etc/ssh/sshd_config`: fine the `Port` line and edit it to 2200
* Set the firewall configuration on Lightsail:
    
    |Application|Protocol|Port Range|
    |---|---|---|
    |ALL TCP+UDP|ALL|0-65535|

* `sudo service ssh restart`: restart the service
* try to connect the server `ssh -i <path_to_key> ubuntu@<IP> -p 2200`
    * successfully logged in
* try to connect the server `ssh -i <path_to_key> ubuntu@<IP> -p 22`
    * `ssh: connect to host <IP> port 22: Connection refused`

## Setup Firewall

This step is considered almost at the beginning, because a failure of the configuration of the firewall could cause that the ssh connection fails.

* `sudo ufw allow 2200`
* `sudo ufw allow 80`
* `sudo ufw allow 123`
* `sudo ufw enable`

Try to connect to the server:
* ssh connection port 2200 -> successfully connected
* ssh connection port 22 -> connection timed out
* Above means that the firewall is set correctly

## Create new user `grader` and grant this user `sudo` permission
Update and upgrade the packages
* `sudo apt-get update`
* `sudo apt-get upgrade`

Create the user
* `sudo adduser grader`
* `sudo touch /etc/sudoers.d/grader`
* `sudo vi /etc/sudoers.d/grader`
    * add `grader ALL=(ALL) ALL`

Test
* login as grader `su grader`
* try `sudo apt-get update`
    * success

## Configure the key-based authentication for `grader` user
* `ssh-keygen`
    * file name `<path_to_key_pair>`
* set the public key into the server
    * create a file in the server `/home/grader/.ssh/authorized_keys`
    * copy the content of the file `<key>.pub` into the this file in the server `authorized_keys`
    * set the permission of the foler `.ssh` to 700
    * set the permission of the file `authorized_keys` to 644
* try to login using the new key `ssh -i <new_private_key> grader@<IP> -p 2200`
    * after enter the passphrase -> successfully logged in

## Enforce key-based authentication and block root login
* `sudo vi /etc/ssh/sshd_config`
    * find the `PasswordAuthentication` line and edit it to `no`
    * find the `PermitRootLogin` line and edit it to `no`
* `sudo service ssh restart`

## Setup the web application in the server
### copy the python web files into the server
* `sudo scp -i <path_to_private_key> -P 2200 -r <path_to_local_dir> grader@<IP>:<path_to_server_dir>`

### install all necessary packages for the python web app
* ubuntu packages `python2.7`, `python-dev`, `python-pip`, `postgresql`, `postgresql-contrib`
* pip install `sqlalchemy`, `flask`, `psycopg2`, `psycopg2-binary`, `oauth2client`, `requests`
    * `locale.Error: unsupported locale setting`
    * solution: 
        * `export LC_ALL=C`
        * https://stackoverflow.com/questions/36394101/pip-install-locale-error-unsupported-locale-setting

### setup postgresql server based database
* `sudo su - postgres`
* `psql` enter the postgresql env
* `create user catalog with password '123';`
* `ALTER USER catalog CREATEDB;`
* `CREATE DATABASE catalog WITH OWNER catalog;`
* `\c catalog`
* `REVOKE ALL ON SCHEMA public FROM public;`
* `GRANT ALL ON SCHEMA public TO catalog;`
* `\q`
* `exit`

change the python files as follows:

```python
engine = create_engine('postgresql://catalog:123@localhost/catalog')
```

* Reference: https://github.com/iliketomatoes/linux_server_configuration

### check if the python files work well and initialize the database setting
Run the python files:
* `python data_base.py`
* `python lotsofcourses.py`
* `python finalproject.py`
    * check if everything works -> `ctrl+C` stop the program

### in google console add the URL for `Oauth`
* `http://<IP>`

## Setup the app container in the server
* install apache and mod_wsgi -> ubuntu packages `apache2`, `libapache2-mod-wsgi`
* create a wsgi file `/var/www/catalog/finalproject.wsgi`
* edit this wsgi file
    ```python
    import sys
    sys.path.insert(0, "<path_to_app_dir>")

    from finalproject import app as application
    ```
* edit file `/etc/apache2/sites-enables/000-default.conf`
    ```html
    <VirtualHost *:80>
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        WSGIScriptAlias / /var/www/catalog/finalproject.wsgi
    </VirtualHost>
    ```
* `sudo apache2ctl restart`
