# Project: Venue Booking Database

## Environment

* Download the `VirtualBox` via [VirtualBox official download page](https://www.virtualbox.org/wiki/Downloads) and install `VirtualBox`
* Download `vagrant` via [Vagrant official download page](https://www.vagrantup.com/downloads.html) and install `Vagrant`.
* Run `vagrant init` in the terminal
* In file `Vagrantfile`, change the line to 
    ```
    config.vm.box = "ubuntu/xenial64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000, host_ip: "127.0.0.1"
    ```
    refer to [Vagrant boxes](https://app.vagrantup.com/boxes/search)
    * When error `Call to WHvSetupPartition failed` occurs
        * try to open a `cmd` via `administration`
        * type `bcdedit /set hypervisorlaunchtype off`
        * refer to [WhvSetupPartition failed](https://github.com/kubernetes/minikube/issues/4587)
        * Reboot the OS
* Run `vagrant up` in the terminal
(Run `vagrant halt` to shut down the virtual machine)

---

* Run `vagrant ssh` to connect to the virtual machine
* Run `cd /vagrant` to the workspace and run:
    ```
    $ sudo apt-get update
    $ sudo apt-get -y install python3-pip
    $ sudo pip3 install Flask
    $ sudo pip3 install -r requirements.txt
    $ sudo pip3 install Flask-SQLAlchemy
    ```
---

* Run the app in the virtual machine:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```
* Navigate to Home page [http://localhost:5000](http://localhost:5000) or [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

