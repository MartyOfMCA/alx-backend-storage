# 0x00. MySQL advanced
This directory contains SQL scripts on some advanced MySQL concepts. This project was created as part of my course requirement at ALX.

## Concepts
* User-defined Functions
* Views
* Indexes
* Stored Procedures
* Triggers

## Prerequisites
To run scripts in this project you need to install:
* MySQL Server 5.7 [Download](https://docs.vultr.com/how-to-install-mysql-5-7-on-ubuntu-20-04)

## How To's
### Executing scripts
The script file can be given to the mysql command-line interface which in turn executes the script providing the results to the console.

`cat script.sql | mysql -h host -u database_user -p`  or `echo "SQL_QUERY" | mysql -h host -u database_user -p`
