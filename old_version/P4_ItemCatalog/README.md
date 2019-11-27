# Item Catalog Web-App Project

## Requirements

### Virtual Environment

* Download the `VirtualBox` via [VirtualBox official download page](https://www.virtualbox.org/wiki/Downloads) and install `VirtualBox`
* Download `vagrant` via [Vagrant official download page](https://www.vagrantup.com/downloads.html)
    * Unzip the downloaded file
    * Move the executable binary file into the environment folder via `sudo mv vagrant /usr/bin`

#### Run the `Vagrant` virtual machine
* In the terminal, run `sudo vagrant up` to install or (re-)start the virtual environment
* In the terminal, run `sudo vagrant ssh` to connect to the virtual environment
* type `cd /vagrant` into the working folder
* type `<ctrl>` + `D`  or `exit` to disconnect
* type `sudo vagrant halt` to shutdown the virtual machine
* `sudo vagrant destroy` to remove all the resources of this virtual machine

---

* Ref: [Udacity FullStackND VM](https://github.com/udacity/fullstack-nanodegree-vm)

### Install the Python Packages

The packages are installed while setup the virtual machine

Refer to `Vagrantfile`, to see the packages installed.

* The python version is `python2`

## Steps to run this web app
* Type in the Client ID/Secret of Google into the file `client_secrets_temp.json` and change the file name to `client_secrets.json`.
* Type in the client id in the file `templates/login.html`.
* Navigate into the folder of this project in the terminal.
* Run `python database_setup.py` to initialize the database.
* Run `python lotsofcourses.py` to populate data into the db.
* Run `python finalproject.py` to start application.
* Open the browser, enter the web address `http://localhost:5000`