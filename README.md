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

    - The main homepage for the site, hero image is large and striking. Large heading tells users they are in the right place. Call to action button to invite users to enter and explore the site.

![screenshot](documentation/features/sitepages/home.png)

- **About Page**

    - About page. Gives users essential information about the tennis club. Text content interspersed with pictures helps to break up the page and keep the user engaged with the presented information. 

![screenshot](documentation/features/sitepages/about.png)

- **News Page**

    - News Page. Displays news posts made by site staff. User can see the most up-to-date information about events and other things happening at the club. Posts are paginated and displayed in a pleasing layout, utilising images to draw the user in.

![screenshot](documentation/features/sitepages/news.png)

- **Contact Page**

    - Contact Page. Users can see contact information for the tennis club, including 
    a contact email address and location information. An embedded Google Maps widget allows users to see the club's exact location.

![screenshot](documentation/features/sitepages/contact.png)

- **Register Page**

    - Register Page. Displays a form that new users of the site can fill in and make an account. The form is short, simple, and clean to encourage users to use it.

![screenshot](documentation/features/sitepages/register.png)

- **Login Page**

    - Login Page. Displays a login form that existing users can use to log in to the site. Two simple input fields for username and password make it easy for users to log in tto their account. A Forgot Password link takes users to another page where they can recover their password. A sign up button at the bottom of the page lets users who do not yet have an account easily find the register page

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

    - Users can use a front-end form to reserve a court to play tennis on at the tennis club. Users are presented with a very simple form, which is easy to fill out, and allows them to quickly 
      make reservations.

      The reservation form contains two steps. First, the user is prompted to select the date on which they would like to play, dates in the past are automatically disabled. Next the user is prompted to choose the timeslot on which they would like to play. Timeslots are automatically presented according to the club's opening hours.

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

- **Title for feature #**

    - Details

![screenshot](documentation/feature/admin/.png)

- **Title for feature #**

    - Details

![screenshot](documentation/feature/admin/.png)


**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
