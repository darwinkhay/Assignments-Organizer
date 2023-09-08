# Assignment Organizer (A-22)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h2 align="center">Assignment Organizer</h2>

  <p align="center">
    Organize your Assignments here!
    <br />
    <a href="https://assignment-organizer-cs3240.herokuapp.com/">View Live</a>
    ·
    <a href="https://github.com/uva-cs3240-f21/project-a-22/issues">Report Bug</a>
    ·
    <a href="https://github.com/uva-cs3240-f21/project-a-22/issues">Request Feature</a>
  </p>
</p>
<br />

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#local-development-setup">Local Dev Setup</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">How to Contribute</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
- Home page: http://localhost:8000 or http://127.0.0.1:8000 (The two are interchangable, but would affect login)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* [python](https://www.python.org/downloads/)
* [django](https://www.djangoproject.com/)
```shell
> python -m pip install Django
```

### Local Development Setup
1. Clone this repo 
```shell
> git clone https://github.com/uva-cs3240-f21/project-a-22.git assignment_organizer
```
2. `cd` into the repo and install all dependencies
```shell
> cd assignment_organizer
> pip install -r requirements.txt
```

3. Make sure your local postgresql service is running
4. change DATABASE configuration in myproject/settings.py to match your local
postgresql setting
```python
# local postgresql configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cs3240', # your local postgresql database
        'USER': 'swan', # your local postgresql user
        'PASSWORD': 'password', # your local posgresql password
        'HOST': '127.0.0.1', # localhost
        'PORT': '5432', # change this if your local postgresql runs in a different port
    }
}
```

5. Follow steps 4-5 in this [link](https://www.section.io/engineering-education/django-google-oauth/)
to create a new google api, and add social app on django admin

> Following steps 4-5 from the link above will allow you to use google login api
only when accessing via http://**127.0.0.1**:8000, but If you want to be able to
login with http://**localhost**:8000, need to add http://**localhost**:8000 to
the google credentials and admin page

> ! If you run into **Server Error 500** when trying to log in, try other numbers for
**SITE_ID** in **myproject/settings.py**

3. Start your own local server and go checkout the website in [localhost](http://localhost:8000) or [127.0.0.1](http://127.0.0.1:8000)
```shell
> python manage.py runserver
```

<!-- ROADMAP -->
## Roadmap
- [ ] Users login to the system using Google login. They then can in some way record their schedule in the system.
- [ ] Users can join classes with other students in the system, seeing who all is in each class.
- [ ] Users can upload PDFs of notes that are then associated with the class.
- [ ] Major tricky feature: Uploading and downloading PDF files
- [ ] Possible APIs you should consider: Google Calendar, other scheduling APIs, file sharing services

<!-- CONTRIBUTING -->
## Contributing

1. update your local main brach
```shell
> git pull origin/main
```
or if upstream is already set to origin/main,
```shell
> git pull 
```
2. create your *feature branch* 
```shell
> git checkout -b feature/[feature_name]
```
3. make changes
4. commit your *changes* 
```
> git commit -m '[commit message]'
```
3. push your changes
```
> git push origin main
```
or if upstream is already set to origin/main,
```shell
> git push 
```

4. Open a Pull Request on github or cli
