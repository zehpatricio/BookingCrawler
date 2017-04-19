# What is the BookingCrawler?
BookingCrawler is a WebCrawler made with framework Scrapy to get extract reviews from the website [Booking.com](https://www.booking.com). It was develop by Natural Language Processing Laboratory(LPLN) of Federal University of Piauí, Brazil.

## Getting Started
Download or clone the project to became work.

### Prerequisites
You will need:
* Python 3.5
* Scrapy 1.3.3
* VirtualEnviroment

### Installing
#### Python
To install Python follow the instructions in [Python Website](https://www.python.org/downloads/).
#### Virtual Enviroment
A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, and help you to avoid problems with other projects in your machine.
Install VirtualEnviroment using the command:
```
sudo pip install virtualenvwrapper
```
After this change your bash file adding the follow lines:
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
Create your Virtual Enviroment using the command:
```
mkvirtualenv -p <path_to_python> <your_virtual_enviroment_name>
```
#### Scrapy
Scrapy is an open source and collaborative framework for extracting the data you need from websites. You can read more about it in the [Scrapy docs page](https://docs.scrapy.org/en/latest/).
Install Scrapy package using the command:
```
pip install scrapy
```
## Adding the URL to be crawled
To add the URL open the file ```bookingcrawler/spiders/bookingspider.py``` and replace the line ```start_urls ...``` by ```start_urls = ["your_url_from_booking"]```.
## Running
Active the VirtualEnv using the command:
```
workon <your_virtual_enviroment_name>
```
Run using the command:
```
scrapy runspider BookingCrawler/bookingcrawler/spiders/bookingspider.py -o <output_file_name>.<csv|json>
```
Thanks, and GO TO WORK!
