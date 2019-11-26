# Log Analysis

## Requirements:

### Virtual Environment

* Download the `VirtualBox` via [VirtualBox official download page](https://www.virtualbox.org/wiki/Downloads)
    * This step may not be necessary
* Download `vagrant` via [Vagrant official download page](https://www.vagrantup.com/downloads.html)
* Unzip the downloaded file
* Move the executable binary file into the environment folder via `sudo mv vagrant /usr/bin`
* In the terminal, run `sudo vagrant up` to install or (re-)start the virtual environment
* In the terminal, run `sudo vagrant ssh` to connect to the virtual environment
* type `cd /vagrant` into the working folder
* type `<ctrl>` + `D`  or `exit` to disconnect
* type `sudo vagrant halt` to shutdown the virtual machine
* `sudo vagrant destroy` to remove all the resources of this virtual machine

---

* Ref: [Udacity FullStackND VM](https://github.com/udacity/fullstack-nanodegree-vm)

###  Install libraries in the virtual machine

* python 3 interpreter
* postgreSQL `sudo apt-get install postgresql`
* psycopg2 library `sudo apt-get install psycopg2`
* file [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### How to run this code

1. Load the data `psql -d news -f newsdata.sql`
2. Run the python file `log_analysis.py` or `python3 log_analysis.py`

## Design of the logic
### What are the most popular three articles of all time?

* `join` the two tables `articles` and `log`
* `count` the columne `log.path` with restriction `log.path like ('%' + articles.slug)`
* `group by` the columne `articles.title` 

### Who are the most popular article authors of all time?

* `join` the three tables `articles`, `log` and `authors`
* `count` the columne `log.path` with restrictions `log.path like concat('%', articles.slug)` and `authors.id = articles.author`
* `group by` the column `authors.name`

### On which days did more than 1% of requests lead to errors? 

* `select` the time as `day` from the table `log`
* calculate the percentage of the errors
* `group by` the column `day` 
* `select` the row from the newly generated table with condition `percentage of the errors is bigger than 1%`
