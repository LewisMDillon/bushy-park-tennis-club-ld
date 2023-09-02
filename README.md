# BUSHY PARK TENNIS CLUB

![screenshot](documentation/mockup.png)


Bushy Park Tennis Club is a fully functioning web application for a tennis club. The site provides users with all important information about the tennis club, and allows users to easily create personal accounts and profiles, and utilises a fully fleshed-out court reservation system. The site also enables administrators to post news articles to the site, as well as view and make changes to reservations on behalf of users.

## UX

The design philosophy was to create a simple, minimalistic look, which would be in stark contrast to the many cluttered and confusing sports club websites that the user will have undoubtedly come across. Relevant information is presented in a salient and refreshingly clean manner, allowing the user to easily and pleasingly navigate through the site.

### Colour Scheme


The color scheme uses soft white and grey colors, with a strong "tennis style" dark-green accent which is present throughout the site.


I used [coolors.co](https://coolors.co/000000-333333-a1a1a1-f5f5f5-ffffff-507e50-507948-304f2a-263e21) to generate my colour palette.

![screenshot](documentation/coolors.png)


### Typography

- [Raleway](https://fonts.google.com/specimen/Raleway) was used for the primary headers, titles, and text content.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

All user stories can be found in a linked GitHub project [here](https://github.com/users/LewisMDillon/projects/4)


## Features

## Existing Features

### Site Pages

- **Homepage**

    - The main homepage for the site. Hero image is large and striking. Large heading tells users they are in the right place. Call to action button to invite users to enter and explore the site.

![screenshot](documentation/features/sitepages/home.png)

- **About Page**

    - About page. Gives users essential information about the tennis club. Text content interspersed with pictures helps to break up the page and keep the user engaged with the presented information. 

![screenshot](documentation/features/sitepages/about.png)

- **News Page**

    - News Page. Displays news posts made by site staff. Users can see the most up-to-date information about events and other things happening at the club. Posts are paginated and displayed in a pleasing layout, utilising images to draw the user in.

![screenshot](documentation/features/sitepages/news.png)
![screenshot](documentation/features/sitepages/pagination.png)

- **Contact Page**

    - Contact Page. Users can see contact information for the tennis club, including 
    a contact email address and location information. An embedded Google Maps widget allows users to see the club's exact location.

![screenshot](documentation/features/sitepages/contact.png)

- **Register Page**

    - Register Page. Displays a form that new users of the site can fill in and make an account. The form is short, simple, and clean to encourage users to use it.

![screenshot](documentation/features/sitepages/register.png)

- **Login Page**

    - Login Page. Displays a login form that existing users can use to log in to the site. Two simple input fields for username and password make it easy for users to log in to their account. A Forgot Password link takes users to another page where they can recover their password. A sign up button at the bottom of the page lets users who do not yet have an account easily find the register page

![screenshot](documentation/features/sitepages/login.png)

- **Profile Page**

    - Profile page. Displays a user's profile information. Lets a user see their relevant profile information in a clean and simple way, and contains an update form that users can use to update their profile information.

![screenshot](documentation/features/sitepages/profile.png)

- **My Reservations Page**

    - My reservations page. Displays a formatted table populated with the user's upcoming court reservations. Users can easily see details of their reservations as well as links to a detail page of each reservation where it can be deleted if the user wishes.

![screenshot](documentation/features/sitepages/my-reservations.png)

- **Logout Page**

    - Logout Page. A simple page confirming that the user has logged out of their account. Displays a log in again button in case the user wishes to log back in.

![screenshot](documentation/features/sitepages/logout.png)

- **Reservation Page**

    - Court reservation page. Displays a form for users to reserve a court at the tennis club. The form is simple and easy to use, with only two steps, letting the user quickly and easily make bookings. 

![screenshot](documentation/features/sitepages/reservation-page.png)

- **Custom Error Pages**

    - Custom error handler pages. These pages display when a user encounters one of the following common errors: 400, 403, 404, 500. These provide a more user-friendly error page than the user would see otherwise and includes an informative message and button to return home to the site. 

![screenshot](documentation/features/sitepages/400.png)
![screenshot](documentation/features/sitepages/403.png)
![screenshot](documentation/features/sitepages/404.png)
![screenshot](documentation/features/sitepages/500.png)

### User Features

- **User Registration**

    - Users can register for an account using a front-end form. This creates a user object in the database and automatically secures the user's sensitive information.

![screenshot](documentation/features/user/register.png)

- **User Login**

    - Users who have made an account can quickly and easily log in to their account in order to access the login-required functionality of the site.

![screenshot](documentation/features/user/login.png)

- **User Logout**

    - Users who are logged in can easily log out in order to stop access to their account-based information and functionality.

![screenshot](documentation/features/user/logout.png)

- **User Password Recovery**

    - Users who have forgotten their password can recover their password via the forgot password link on the login page. Users will enter their email and get a password reset link sent to their account email which they can use to set a new password.

![screenshot](documentation/features/user/password-recover.png)

- **Login Dependant Navbar Links**

    - Users who are logged in see new links in the navbar. 'Register' and 'Login' links are replaced with 'My Account' and 'Reserve A Court' links. This provides the user with visual feedback upon logging in, as well as removing links that they will not need.

![screenshot](documentation/features/user/login-navbar-links.png)

- **Login Redirect**

    - Users who are not logged in who attempt to access an area of the site which requires login are redirected to the login page. After logging in, they are sent to the page they first intended to visit.

![screenshot](documentation/features/user/login-redirect.png)

- **User Profile Creation**

    - User profiles are automatically created upon user registration. This assigns each user a profile which they can use to see/update their user information.

![screenshot](documentation/features/user/profile-creation.png)

- **User Profile Update**

    - Users can update their profile information using a front-end form located on their user profile page. This allows users to update profile information or correct possible mistakes made at registration.

![screenshot](documentation/features/user/profile-update.png)

- **User Court Reservations**

    - Users can use a front-end form to reserve a court to play tennis at the tennis club. Users are presented with a very simple form, which is easy to fill out, and allows them to quickly 
      make reservations.

      The reservation form contains two steps. First, the user is prompted to select the date on which they would like to play, dates in the past are automatically disabled. Next,the user is prompted to choose the timeslot at which they would like to play. Timeslots are automatically presented according to the club's opening hours.

![screenshot](documentation/features/user/court-reservation.png)

- **Automatic Timeslot Availability Checking**

    - In the court reservation form, when selecting a timeslot, users can see which timeslots are fully booked, as well as timeslots which have limited availability on their chosen date. Timeslots which are fully booked (all 9 courts already booked at that time) are automatically disabled and unselectable by the user. Timeslots which have limited availability (courts with 6 to 8 bookings) are automatically colored orange and the user can see a 'limited availaility' message beside the timeslot.

![screenshot](documentation/features/user/timeslot-availability.png)

- **Automatic Court Assignment**

    - In the court reservation form, users do not need to select a court on which to play. Instead, the backend functionality of the form automatically assigns the user an available court based on the amount of bookings that have already been placed on the selected date and timeslot.

![screenshot](documentation/features/user/court-assignment.png)

- **User Email Confirmations**

    - After making a reservation, the site automatically sends the user a confirmation email which contains their reservation details, as well as instructions on how to cancel the reservation.

![screenshot](documentation/features/user/email-confirmation1.png)
![screenshot](documentation/features/user/email-confirmation2.png)

- **User Reservation Cancellation**

    - Users can cancel their existing reservations using front-end functionality on the site, without having to call or visit the tennis club. On the reservation details page, users can see a clear and obvious 'cancel reservation' button which will take them to a confirmation page, before deleting their reservation. 

![screenshot](documentation/features/user/cancel-reservation.png)

### Admin/Staff Features

- **Create News Posts**

    - Administrators can use a front-end form to create new site news posts. The form is simple and clean and automatically formats and displays the created post in the same manner as existing posts.

![screenshot](documentation/features/admin/create-post.png)

- **Update News Posts**

    - Administrators can use a front-end form to update existing posts. If the current logged-in user has staff privileges, an update button will appear over posts which allows that user to edit the information in posts.

![screenshot](documentation/features/admin/update-post.png)

- **Delete News Posts**

    - Administrators can use a front-end form to delete existing posts. If the current logged-in user has staff privileges, an delete button will appear over posts which allows that user to delete that post.

![screenshot](documentation/features/admin/delete-post.png)

- **Latest News Posts On Homepage**

    - The most recent post, along with the two next-most recent posts are automatically displayed on the homepage. This allows users of the site to see the most up-to-date site news at a glance.

![screenshot](documentation/features/admin/homepage-news.png)

- **Master Reservation List**

    - Administrators have access to a master list of all the club reservations. The list is ordered by reverse date by default, which helps to show administrators the most relevant reservations first. There are two search boxes at the top of the list page, which can be used to find reservations on certain dates, or to find reservations made by a specific user.

![screenshot](documentation/features/admin/reservation-list.png)

- **Delete Reservations For Users**

    - Administrators, using the master reservation list, can view the details of another user's reservation, as well as delete that reservation on behalf of that user.

![screenshot](documentation/features/admin/reservation-delete.png)


### Future Features


- Update Reservations
    - A user can edit their reservation, without deleting it and creating a new one. 
         - Not in this deployment due to it breaking the automatic availability checks and automatic court assignment. Needs a restructure of reservation system to be implemented. 
- Advanced reservation actions for admins
    - An admin can make more advanced reservation actions, such as:
        - block booking timeslots
        - recurring reservations
        - changing of available reservation dates
        - changing of available timeslots and courts
        - mass deletion/creation of reservations
- Online Payment System
    - Users can pay the cost of their court reservation online

## Tools & Technologies Used


- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Pillow](https://pypi.org/project/Pillow/) used for image processing
- [Gunicorn](https://gunicorn.org/) used for WSGI server
- [sycopg2](https://pypi.org/project/psycopg2/) used as a PostgreSQL database adapter

## Database Design

While planning this project, I drew up an Entity Relationship Diagram to help me to visualise the database models and their relationships. 

![screenshot](documentation/erd.png)


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/LewisMDillon/bushy-park-tennis-club-ld/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and tasks were planned, then tracked on a weekly basis using the basic Kanban board.

The [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method) method was used with accompanying custom Github project labels to help me to prioritise the important tasks in the time I had available.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://github.com/LewisMDillon/bushy-park-tennis-club-ld/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.


- [Open Issues](https://github.com/LewisMDillon/bushy-park-tennis-club-ld/issues)

    ![screenshot](documentation/gh-issues-open.png)

- [Closed Issues](https://github.com/LewisMDillon/bushy-park-tennis-club-ld/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-issues-closed.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://bushy-park-tennis-club-896947b1504e.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: bushy-park-tennis-club-ld).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/LewisMDillon/bushy-park-tennis-club-ld) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/LewisMDillon/bushy-park-tennis-club-ld.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/LewisMDillon/bushy-park-tennis-club-ld)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LewisMDillon/bushy-park-tennis-club-ld)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

The local version, created on Gitpod, does not have the functionality to send confirmation emails. This is due to the fact that Gitpod blocks the necessary email port required to carry out this operation. Gitpod blocks this port by default due to concerns about email spam and it cannot be changed.

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/questions/3005080/how-to-send-html-email-with-django-with-dynamic-content-in-it) | reservations/views.py | Django sendmail function with dynamic content |
| [Stack Overflow](https://stackoverflow.com/questions/15795869/django-modelform-to-have-a-hidden-input) | Reservation Form | Hide inputs on a Django built-in model form
| [YouTube](https://www.youtube.com/watch?v=vmP1r6xiJog) | Reservation Form | passing data from one page to another in Django |
| [Youtube - Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) | entire site | how to set up a Django Project
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [Bootstrap Components](https://getbootstrap.com/docs/5.3/examples/) | Navbar, Hero, About, Jumbotron, Footer | pre-built bootstrap components
| [Date Picker date restriction](https://www.w3resource.com/javascript-exercises/javascript-date-exercise-2.php) | Reservation Form | tutorial on how to set date restrictions on the HTML date picker
| [Neverlost-Thrift](https://github.com/Ri-Dearg/neverlost-thrift/blob/master/config/urls.py) | tests.py | My mentor's repository used as a reference for creating tests & error handler pages
| [Codepen](https://codepen.io/uidesignhub/pen/vYmBKpj) | Error Handler pages | HTML & CSS template for error handler pages


### Media


| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Google Icon](https://fonts.google.com/icons?selected=Material+Symbols+Outlined:sports_tennis:FILL@0;wght@400;GRAD@0;opsz@24&icon.query=tennis) | entire site | image | favicon on all pages
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |
| [Unsplash](https://unsplash.com/photos/BlS47Eiu2iM) | homepage | image | hero image
| [Unsplash](https://unsplash.com/photos/wvDELsJ_E20) | homepage, news page| image | news article image 1
| [Unsplash](https://unsplash.com/photos/0wbYOLZwDPY) | homepage, news page| image | news article image 2
| [Unsplash](https://unsplash.com/photos/2FKTyJqfWX8) | homepage, news page| image | news article image 3
| [Freepik](https://www.freepik.com/free-photo/young-couple-playing-tennis-court_5507419.htm#from_view=detail_alsolike) | about page | image | 'open to all' image on about page
| [Unsplash](https://unsplash.com/photos/vRb10tlBHVQ) | about page | image | 'fairly priced' image on about page

The first image for 'Beautiful Facilities' on the about page is my own.
### Acknowledgements

- I would like to thank my Code Institute mentor, Rory Patrick Sheridan for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner Rachel, for believing in me, and allowing me to make this transition into software development, and also actually playing tennis with me while I was making this site to keep me sane.
