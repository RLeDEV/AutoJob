# AutoJob
## About the project 
The project was made by a student to help other students to find their first professional position in the high-tech industry, using this project, you will receive emails with the most updated student positions.


## How to get it work
### This script works only for:
1. Indeed
2. Glassdoor
### Install the requirements
To install the requirement packages please use the following command `pip install -r requirements.txt`
### Make a config.yml file and locate it inside of `Driver` folder
The configure file should look like this: <br/>
```
mongodb:
  username: mongo_user_name
  password: mongo_password
  database: mongo_db_name
  collection: mongo_collection_name

mail:
  username: gmail_username (sender)
  password: gmail_password (sender)
  destination: your_destination_gmail

selenium:
  geckodriver_path: geckdriver_path_in_your_computer
```
### Download geckodriver
You can find executable in the following link: https://github.com/mozilla/geckodriver/releases
### Edit main.py
You can add as many web links as you want, the script will send to you only the jobs that it didn't sent yet using MongoDB.<br/>
to add a new website please add the following line and replace with your link:<br/>
`manage.add_website(link_here)`

## License 
This is a free to use, please do not copy.
