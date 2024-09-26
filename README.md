### Table of Contents
Introduction
Features
Screenshots
Prerequisites
Installation
Usage


## Introduction
This project is a feedback collection application that allows users to submit feedback easily. The main goal is to gather valuable insights to improve our services.

## Features
Feature 1: Feedback form submission (data stored at admin panel)
Feature 2: Thankyou page with details of user and time of submission

## Screenshots

### Home Page
![homepage](https://github.com/Kee-rti/Feedback/blob/master/project/media/home.png?raw=true)
### Feedback Form
![form](https://github.com/Kee-rti/Feedback/blob/master/project/media/form.png?raw=tue)
### Thank You Page
![thankyou](https://github.com/Kee-rti/Feedback/blob/master/project/media/thankyou.png?raw=true)
### Admin Page
![admin](https://github.com/Kee-rti/Feedback/blob/master/project/media/feedback.png?raw=true)
![feedback](https://github.com/Kee-rti/Feedback/blob/master/project/media/admin.png?raw=true)


### Prerequisites
- Python
- Django


## Installation

bash
Copy code
# Clone the repository
git clone https://github.com/Kee-rti/Feedback.git

# Navigate to the project directory
cd project

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver

##Usage

Visit http://localhost:8000/ in your web browser.
Click on "Give feedback" to access the feedback form.
Fill out the form and submit it to see the thank you page.
