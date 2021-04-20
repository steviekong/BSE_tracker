# 1dha

Simple app to display latest BSE Bhavcopy (Equity) data. Allows you to search data by company name and download the search results as a CSV.

Built with Django, VueJs and Redis.

Hosted at http://1dha.srejikumar.com

![Screenshot](https://i.ibb.co/4ptWzHp/Screen-Shot-2021-04-18-at-12-28-57-AM.png)

## Getting started

This development setup has only been tested on OSX 11.2.3

### Prerequisites

- node v14.\*
- npm v6.14.\*
- python 3.9 \*
- pip 21.0.1 \*
- Redis server 6.2.1

### Directory structure

`backend` directory contains the django backend application.

`frontend` directory contains the vue frontend application.

### Setup for Local deployment

1. Clone this repository

2. cd into frontend directory
   `cd BSE_tracker/frontend`

3. Install npm packages
   `npm install`

4. Build static files
   `npm run build`

5. cd to backend directory
   `cd ../backend`

6. Create virtual env
   `python3 -m venv env`

7. Activate virtual env
   `source env/bin/activate`

8. Install pip packages
   `pip3 install -r requirements.txt`

9. Add cron tab
   `python3 manage.py crontab add`

You should see something like this as the output

`adding cronjob: (dd0a834c2648e926c551c5c97caa4ff4) -> ('00 18 * * *', 'backend.cron.get_bahv_add_to_redis')`

This cronjob will run at 18:00 IST daily assuming system time is set to accurate IST time.

10. Make sure you have redis server running locally on port 6379.

11. Start django server
    `python3 manage.py runserver`

If the server starts successfully you should see the following

```
Django version 3.2, using settings 'backend.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The app should be running on http://localhost:8000 .

### Populating data

If the redis is empty (should only occur the first time) the search function automatically runs a routine to populate redis with the latest bahv data.

After that the data with be refreshed by the cron job running at 18:00 daily.

#### File store

Temporary files like zip and csv files are stored on `/tmp` so windows users might have issues running this project.

**Have fun! 🙂 🎉**
