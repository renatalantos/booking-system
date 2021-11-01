
# Milestone Project 4 - Restaurant Booking System for Renata's Restaurant
![All devices](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/site%20features/Intro%20to%20site%20readme.JPG)

[View the live project here.](https://restaurant-reservation-sytem.herokuapp.com)

This is the main marketing website for the fictitious website, Renata's Restaurant. It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential visitors and users.

## Table of Contents

* [Introduction](#introduction)

* [UX](#ux) 
    - User Stories
        -  First Time Visitor Goals
        -  Returning and Frequent Visitor Goals
        -  Site Administrator Goals  
* [Layout](#layout)

    - Design
        - Colour scheme
        - Typography
        - Images
    - Wireframes
        - Discrepancy with Original Ideas
        - Links to Wireframes
* [Features](#features)
    - Responsivity
    - Interactive Elements
    - Features to add in future

* [Technologies Used](#technologies-used) 
    - Languages Used
    - Frameworks, Libraries and Programs Used  

* [Testing](#testing)
    - Testing User Stories from User Experience (UX) Section
    - Further Testing
    - Unresolved Bugs 

* [Deployment](#deployment)

* [Credits](#credits)

# Introduction

The product Restaurant Booking System is a fictitious restaurant website. 
Beside being able to view pages like the home page, menu and the contact page, users are also able to create an account, sign in, avail of the table booking feature and view bookings, which unregistered users don't have access to. Through the booking and the view booking navbar link users can access all their previous bookings, edit and delete them. Site user administrators have access to all bookings and all create, edit and delete functionalities.
The site has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.


# UX

-   ### User stories 

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the business.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to sign up for a user account to access restricted content.
        4. As a First Time Visitor, I want to create a table booking, view booking details, and learn what changes I can make on created bookings.
        5. As a First Time Visitor, I want to sign out of my user account at the end of the session to keep my account related details safe.
        

    -   #### Returning and Frequent Visitor Goals

        1. As a Returning and Frequent Visitor, I want to sign into my user account.
        2. As a Returning and Frequent Visitor, I want to create a table booking, view my current and previous booking details, and alternatively edit them or delete them.
        3. As a Returning and Frequent visitor I want to send messages and queries to the site owner.
        4. As a Returning and Frequent visitor I want to like the restaurant services.
        5. As a Returning and Frequent Visitor, I want to sign out of my account at the end of the session to keep my account safe.

    -   #### Site Administrator Goals
        1. As a Site Administrator I would like to be able to create, view, edit and delete bookings.    
        
        
# Layout
-   ### Design
    -   #### Colour Scheme
        -   The main colours in the website theme for header, background, footer and text labels are brown, yellow, and beige.
    -   #### Typography
        -   I used a standard Bootstrap theme with all the components and styling. Raleway and Lora are the main fonts used, Raleway for label titles and Lora for body text.
    -   #### Imagery
        -   Imagery was chosen to go with the website's colour and content theme. I'm using dining and restaurant interior images with deep-toned, soothing colours and attractive graphics. For the edit, delete and logout page I'm using images with graphics that signal what will happen if user edits, deletes or signs out.

*   ### Wireframes
    -   #### Discrepancy with original ideas
        -   I originally intended to create my own HTML pages and CSS styling, however, I decided to use a standard Bootstrap theme instead, which saved me a huge amount of time. I simply followed the theme layout, customized text labels for various forms, so the original wireframes were not used at all. As the theme is fully responsive, I didn't create mobile device wireframes after deciding to use Bootstrap. By using a Boostrap theme, my theme is more unified, too. I also created a menu page for the site, which wasn't in my original plans.
    -   #### Links to Wireframes

        -   Home Page Wireframe - [View](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/Home%20Page%20Wireframe.pdf)

        -   Booking Page Wireframe - [View](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/Booking%20Page%20Wireframe.pdf)

        -   Contact Us Page Wireframe - [View](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/Contact%20Page%20Wireframe.pdf)

        -   Login Page Wireframe - [View](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/Login%20Page%20Wireframe.pdf)

        -   Register Page Wireframe -[View](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/Register%20Page%20Wireframe.pdf)



# Features

-   ### Responsivity

The application is responsive on all device sizes, thanks to the Boostrap theme. In mobile view there is a collapsible menu icon. All images, text labels, forms get appropriately resized. There is an exception, however: when bookings are displayed in the database table in the view_booking.html, on mobile phone screens in portrait mode there is not enough room for all columns to be shown. However, Bootstrap adds a slide bar so that user can slide the page content from left to right. 

[View database table in portrait mode on smallest mobile device](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/site%20features/Booking%20table%20with%20slide%20bar.JPG)

In mobile phone landscape mode all columns show beside one another, however, the nav header and footer don't reach from one end of the page to the other.

[View database table in landscape mode on smallest mobile device](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/site%20features/Booking%20table%20landscape.JPG)

-   ### Interactive elements
    -   #### Nav links for Home, Menu, Book a Table, Contact Us, My bookings, Register, Login and Logout pages
    -   #### Form input fields on signup, register, signout, table booking, edit booking and delete booking forms
    -   #### Buttons - including form buttons (signup, register, signout, table booking, edit booking and delete booking form buttons) and page buttons (Visit Us button on Home page)

-   ### Features to add in future   
    -   #### I would like to add a dropdown list for registered users to acess their account-related activites like view bookings, login and logout.

## Technologies Used
# Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
1. [Django:](https://www.djangoproject.com/)
    - The Python-based Django framework was used to set up the structure, functionalities,  data model and database of the website.
1. [Bootstrap 5.1.3:](https://startbootstrap.com/theme/business-casual)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    -    Raleway and Lora are the main fonts used, Raleway for label titles and Lora for body text.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript. It is also used for the Bootstrap Tempus Dominus datetime picker.
1. [Javascript:](https://en.wikipedia.org/wiki/JavaScript)  
    - Javascript was used to define visibility duration for popup messages that signal successful completion of different form related activities.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process. [Wireframes](https://github.com/renatalantos/booking-system/tree/main/restaurant/documents/screenshots/wireframes)
1. [Lucidchart:](https://www.lucidchart.com/)
    - Lucidchart was used to create the data model of the project . [View Booking data model](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/1%20model%20only%20with%20Booking.JPG)   
1. [SQLite3 database:](https://en.wikipedia.org/wiki/SQLite)
    - SQLite3 is Django's default database system.
1. [Cloudinary:](https://cloudinary.com/)
    - I used cloudinary for cloud-based storage and partly for linking of my website images.
1. [Heroku:](https://www.heroku.com/)
    -  Heroku is used for the deployment and ultimate cloud-based storage of my application.

# Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every pagefor HTML and CSS of the project to ensure there were no syntax errors in the project. I used the inbuilt pylint compiler to validate the Python files.

-   [W3C URI Validator](https://validator.w3.org/#validate_by_uri)
    - See the [URI Validator Results](https://github.com/renatalantos/booking-system/tree/main/restaurant/documents/screenshots/html%20validation)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - See the [CSS Validator Results](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/css%20validation/Jigsaw%20CSS%20Validator.JPG)
-   [Gitpod Pylint](https://pylint.org/)
    - See the [Gitpod Pylint Results](https://github.com/renatalantos/booking-system/tree/main/restaurant/documents/screenshots/pylint%20validation)    

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the business.
        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text and a "Visit Us Today!" Call to action button. The name a resturant is a banner above the navigation bar, with a bit of a fun fact above. (WINNER OF THE SURPRISE ENTREPRENEUR OF THE YEAR AWARD)
        2. The main points are made immediately with the hero image, which is a restaurant interior and the text label attached to it.
        3. The user has two options, click the call to action button "Visit Us Today!" or go to the "Contact Us" page, both of which will lead to the same place, to learn more about the restaurant.

    2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        1. The site has been designed to have minimum content per page so that the user is not entrapped. The content is limited to what it says in the navigation links. The navigation bar is more towards the middle of the page and each link clearly describes what the page where the user will end up does.

    3. As a First Time Visitor, I want to sign up for a user account to access restricted content.
        1. Once the new visitor has read the Home, Contact us and Menu pages, had a look at what the Login and Register pages do, they might decide to book a table at the restaurant. They will click on the Book a Table navigation link, which will take them to the login page sign in form (hero image with restaurant interior and sign in form).
        2. The login page sign in form contains a link where user can create an account from: "If you have not created an account yet, then please sign up to make reservations." This way users can understand that all booking functionalities are only accessed for registered users.
        3. Alternatively, the user might want to create an account from the navbar link "Register", which will take them straight to the signup form. 
        4. Once the user signs up by creating a username, optionally adding an email address, creating and repeating the password, they are redirected to the home page. 
        5. In the navbar now, the Login and Register navbar links have disappeared, My Bookings, Logout and Logged in as (Created username) appear instead.
    
    4. As a First Time Visitor, I want to create a table booking, view booking details, and learn what changes I can make on created bookings.


        1. Once the first-time user has created an account and been redirected to the home page, they can click on the Book a Table nav link again. This time they will see a hero image with tables and a booking form with the  following form elements:
            - #### Form title "Table Booking Form"
            - #### The following input fields:
                *   ##### Customer name - takes alphanumerical characters
                *   ##### Phone number - takes alphanumerical characters
                *   ##### Reservation date and time - has a calendar popping up with date and time picker
                *   ##### Number of customers - takes only positive whole numbers (not 0)
            - #### Submit booking button


        2.  User enters in Customer name, phone number, reservation date and time and number of customers on the form.
        Although only two fields are marked with an asterisk, customer cannot submit without filling in all fields. 
        
        
        [Go to booking form validation section from this link to see all issues](#booking-form-validation)
        
        
        Once customer clicks on Submit booking, they are redirected to a page where bookings are arranged in a table. At the same time a pop up message appears just under the navbar: "Booking successful".
        The table where the booking(s) is visible has the following headings and the row(s) and columns(s) underneath:
        * Logged in User - username as per what user is logged in as
        * Booking Id - booking id as generated by the foor loop in view_booking.html
        * Customer name - as per user input on booking form
        * Reservation date and time - as per user input on booking form
        * Phone number - as per user input on booking form
        * Number of guests - as per user input on booking form
        * Edit booking - button
        * Delete booking - button


        3. If user decides that they do not wish to perform any further action on their booking, they can easily go on any other site page from the navbar that is visible straight above the bookings table.
        4. If user decides, that they wish to edit their booking, they must click on the Edit Booking button. The booking will appear on a separate page, with a clean pad and pencil image, on a form like the table booking form. The form has the following elements:
        - #### Form title "Edit Your Booking"
        - #### Link "Changed my mind, back to my booking" in case customer has changed their mind
        - #### The following input fields:
            *  ##### Customer name - as per user input when creating a booking
            *  ##### Phone number - as per user input when creating a booking
            *  ##### Reservation date and time - as per user input when creating a booking
            *  ##### Number of customers - as per user input when creating a booking
        - #### Submit edited booking button

        If user clicks on "Changed my mind, back to my booking" link, they are taken back to the previous page, to the table with all booking details.
        Whether user edits their booking details on the form or leave them unedited on the form and click on the "Submit edited booking" button, they are taken back to the previous page, to the table with all booking details. Additionally, user sees the following popup message "Your booking has been updated". If user enters a date in the past, the form won't update and the error message "Booking date must be in the future" appears. 
        Customer can then go onto any page after as per navbar links, which are displayed straight above the bookings table.
        
        5. If user decides, that they wish to delete their booking, they must click on the Delete Booking button. The booking will appear on a separate page, with a waste paper basket image, on a form like the table booking form. The form has the following elements:
        - #### Form title "Are You Sure You Want to Delete this Booking?"
        - #### Link "No, back to my booking" in case customer has changed their mind
        - #### The following input fields:
            * ##### Customer name - as per user input when creating a booking
            * ##### Phone number - as per user input when creating a booking
            * ##### Reservation date and time - as per user input when creating a booking
            * ##### Number of customers - as per user input when creating a booking
        - #### Delete booking button

        If user clicks on "No, back to my booking" link, they are taken back to the previous page, to the table with all booking details.
        When user clicks on the "Delete booking" button, they are taken back to the previous page, to the table with all booking details, without the deleted booking details. Additionally, user sees the following popup message "Your booking has been deleted". If customer deletes a booking where a date in the past now, the success message won't appear. Customer can then go onto any page after as per navbar links, which are displayed straight above the bookings table.

        
    5. As a First Time Visitor, I want to sign out of my user account at the end of the session to keep my account related details safe. 
        1. To accomplish this, user clicks on the Logout navbar link.
        2. A logout form with matching image as a background and with the following elements appears:
            *   Form title "Sign Out"
            *   Text "Are you sure you want to sign out?"
            *   Sign Out button
        3. If user clicks on the SIgn Out button, they are taken to the home page, at the same time the message "You have signed out" appears.

     



-   #### Returning and Frequent Visitor Goals

     1. As a Returning and Frequent Visitor, I want to sign into my user account to access restricted content.

        1. User clicks on Login button.
        2. They will be directed to the sign in form.
        3. They enter username and password created at the signup.
        4. If username and password match, they are taken to the home page. At the same time a pop up message appears
        "Successfully signed in as 'username'".
        5. If username and/or password are incorrect, the following message appears on the signup form: "The username and/or password you specified are not correct." User need to enter correct details or re-register. They are directed to the home page then.
        6. If user signs in by clicking on the Book a Table link first, they are directed to the Book a Table page.


    2. As a Returning and Frequent Visitor, I want to create a new table booking, view details of my newly made and previous bookings, and alternatively edit them or delete them.

        1. Users can create a new booking, as per the steps described above, by clicking on the booking form, from the Book a Table menu .
        2. After submitting the booking, users can view their newly added or older booking details. Editing and deleting can be done from there.
        3. Alternatively, if users do not wish to create a new booking, just would like to view their existing booking details or edit or delete them, they can click on the "My bookings" navbar link, which will be visible for authenticated users after login. This exposes the same page where users get after adding a booking.
        
    3. As a Returning and Frequent visitor I want to like the restaurant services on their website.
        1. Currently this feature is outside of this project's scope as was labelled as a non-immediate requirement in the Agile user stories (labelled as could have). I would like to add this feature in future.
        [Agile User Stories](https://github.com/renatalantos/booking-system/projects/1)
    4. As a Returning and Frequent visitor I want to send messages and queries to the site owner via a form.
        1. Currently this feature is outside of this project's scope as was labelled as a non-immediate requirement in the Agile user stories (labelled as should have). I would like to add this feature in future.
        [Agile User Stories](https://github.com/renatalantos/booking-system/projects/1)

    5. As a Returning and Frequent Visitor, I want to sign out of my account at the end of the session to keep my account safe.
        1. User should follow the steps described above for First Time Visitors.
    6. As a Returning and Frequent Visitor, I would like to see if there are any changes to the menu or opening hours.
        1. User goes on the Menu or Contact page to do this.

-   #### Site Administrator Goals

    1. As a Site Administrator I would like register as a site admin and then log into the admin page.
        1. In the Django framework, in the terminal window of the development environment the following command needs to be run:
        python manage.py createsuperuser and then user needs to press enter 
        2. Next user is prompted to create a username and then user needs to press enter 
        3. Next user is prompted to enter an email address (optional) and then user needs to press enter 
        4. Next user is prompted to enter a password, press enter, repeat password and then user needs to press enter again. 
        1. In the Django framework, the site administrator can log into the site by adding /admin to the basic web address. 
        2. They can login here through the standard login form provided.

    2. As a Site Administrator I would like to be able to create, view, edit and delete bookings.
        1. Once the booking object is created in the admin database (after being created in models.py, registered in admins.py and connection to the database), a site administrator can avail of the inbuilt functionalities in the Django admin site, like adding bookings, viewing all bookings made, editing and deleting bookings. They can do this for themselves and all authenticated users. This is fairly straightforward. All booking related changes on the website on the front end that registered and authenticated users make like adding, editing and deleting are synchronized with the django admin database and vice versa.
        [Django Admin Database Functionalities](https://github.com/renatalantos/booking-system/tree/main/restaurant/documents/screenshots/admin%20page)

### Further Testing

-   The Website was tested on Google Chrome, Firefox, Microsoft Edge, Opera and Internet Explorer browsers. The site renders fine in all browsers. In IE the body fonts revert from Lora to Times New Roman.
-   The website was viewed on a variety of devices such as Desktop, Laptop, Samsung Galaxy A51 and Google Developer Tools. It is responsive on all devices and all features work as expected.
-   A large amount of testing was done to ensure that all pages were linking correctly. - See Testing User Stories
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Unresolved Bugs

-   #### In general
    1. In the Gitpod Development Environment the site works with full CSS styling by now when Debug is off in the settings.py file. However, the admin page (/admin) comes up without CSS styling.

    [No CSS for site admin page](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/admin%20page/Site%20admin%20no%20css.JPG)
    
    When Debug is on in the development environment, the admin site has full CSS styling.
    # Booking form validation
-   #### Booking form related validation issues
    1. Validations I could implement
        -   1. There is a validation in place where user cannot enter a past or immediate present date (Immediate present date is already the past when user submits the booking form.) There is a validation function in the models.py file, with a validation error raised. In the views.py file in the add_booking function then, when due to the validaton error form is not valid, and cannot be saved, an error pop up message is generated, saying "Booking date must be in the past".

        [Validation function in models.py](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/dilemmas/Booking%20cannot%20be%20in%20past.JPG)


        [Error message in views.py](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/dilemmas/Error%20message%20in%20views.JPG)

        -   2. User cannot enter a duplicate booking. This is due to the uniqe_together list with its items in the models.py Meta class. User, customer name and reservation date and time cannot be duplicated together, otherwise a 505 error will show, which I customized as a duplicate_booking.html page.

        [Must be unique](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/dilemmas/unique_together.JPG)


        [Customized 505 error](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/dilemmas/Duplicate%20booking%20customized%20page.JPG)

    2. Validations I could not implement
        -   1. I wanted phone number to be purely numerical. At the moment it's at the user's discretion whether they enter alphabetical or numerical characters. I tried to use PhoneNumberField and validate regular expressions (with from django.core.validators import RegexValidator). However, the former could be deprecated and when I tried to add a regular expression with a validator, my booking page froze. However, no error message appeared.
        Due to time restraints, I'm not pursuing a further solution at the moment. In future I would like to add this validation.

        -   2. I wanted to define an opening time and make sure that user cannot book a reservation outside the opening hours. My approach was to extract the hour and minute from the reservation date and time and compare this to a certain hour and minute combination of the opening and closing time. However, I didn't manage to find a date-time format for opening and closing time where I could have compared them to the reservation date. Due to time restraints, I'm not pursuing a further solution at the moment. In future I would like to add this problem.

        Please find a screenshot below for a validation attempt and the error I was getting:


        
        [Validation attempt for opening hours](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/errors/Validate%20opening%20time%20error.JPG)


        [Error after opening hours validation attempt](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/errors/Validate%20opening%20time.JPG)

    3.  On the booking form, all fields are required, user cannot submit the form without filling in all fields. However, only Customer name and number of customers have an asterisk behind them. I assume the formatting and styling of the form fields is done by the crispy form tags. I noticed that when I changed the model for the form field in models.py, the asterisks were taken away in some cases. In future I would like to correct this validation.

    [No asterisk on form beside import field yet field is required](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/dilemmas/Booking%20form%20no%20asterisk%20yet%20fied%20is%20required.JPG)



# Deployment

### Heroku

The project was created in Github first and then transferred to the Gitpod development environment by the use of the green Gitpod button.

## Initial Deployment  
- ### When creating a Django project, it is highly advisable to deploy early, due to the compexities of the development process and the actual application.

1. In the Gitpod environment a skeleton django project was created (project, app and relating files).
2. A Heroku app was created in Heroku.
3. In Heroku, under the Resources tab, in Add-ons, I searched for Postgres. When found I submitted a request to use it. 
This attached Heroku Postgres to my project in Heroku.
4. In the Heroku Settings tab I clicked on "Reveal Config Vars" and copied the automatically added postgres link from beside the DATABASE_URL variable. 
5. In Gitpod dev environment, I looked for the env.py file that was automatially generated from the CI template at the beginning. This file stores environment variables.
6. After importing the os into the env.py file, I added the database URL from Heroku into env.py.
7. I added a secret key in the env.py file after having it generated on the [Django Secret Key Generator - MiniWebtool](https://miniwebtool.com/django-secret-key-generator/) website.
8. I added the secret key into the Heroku Settings > config vars as well.
9. In the settings.py file in Gitpod I imported os and added an if statement saying that outside the development environment the environment variables must be used from env.py, including the secret key.
10. Still in the settings.py file, I commented out the present code for databases and added code to use the currently set up django database URL as set in the env.py file and also in the Heroku config vars.
11. I migrated these changes in Gitpod using python3 manage.py migrate
12. To get static and media sites stored on Cloudinary, I went to the dashboard of my previously created Cloudinary account and copied the API Environment Variable.
13. I added this to the Gitpod env.py file and into the Heroku Settings > config vars. 
14. I also added DISABLE_COLLECTATIC = 1 to the Heroku config vars. 
15. I added cloudinary and cloudinary_storage to the installed apps in settings.py. 
16. I set up the static file storage, static file directory, the static root, the media url, the default file storage and the templates directory in settings.py.
17. I added the Heroku name followed by herokuapp.com to the ALLOWED_HOSTS variable name in settings.py, followed by a comma and 'localhost' (to allow running in the development environment).
18. I created 3 directories at the top level: media, static, templates.
19. I created a Procfile at the top level directory. 
20. I did a git add, git commit and git push.
21. In the Deployment tab in Heroku, in Deployment method, I added Github, set up Enable Automated Deployment, looked for my Github repository, connected my Heroku app to it and clicked on Deploy Branch at the bottom of the page.
22. When I opened the app after the app was built and deployed, I saw the success message page with a rocket.
23. After  my application was built, as the first step of the final deployment I turned Debug to False in the settings.py file in Gitpod.
24. In Heroku I removed the DISABLE_COLLECTSTATIC variable.
25. I saved my changes on all my files and performed a git add, git commit and git push.
26. As automatic depoyment had been enabled in Heroku, I waited until my app was built, then I opened it and made sure that all functionalities work.

# Credits

### Code

-   The structure and the code of the project was mainly based on two project walkthroughs by Code Institute:
    * Hello Django - I created CRUD functionalities based on this walkthrough.
    * I think therefore I blog - I created authentication and messages functionalities based on this walkthrough and followed the deployment steps described here. 

-   [Bootstrap5 Template](https://startbootstrap.com/theme/business-casual): Bootstrap Theme used throughout the project  to style pages and make site responsive.

-   [Official Django Documentation](https://docs.djangoproject.com/en/3.2/) was researched for syntax, code expressions, code functionalities.

-   Stack Overflow was was researched for syntax, code expressions, code functionalities, problem solving. Validation function for reservation date and time is from there.

-   How to implement widgets for form fields was answered by tutor on FullStack Slack channel.


### Content

-   Content comes from the Bootstrap template, I made slight changes to the prewritten content there. Food descriptions in Menu page come partly from the Burger Joint web page and various recipe websites. 


### Media

-   Images are from pexels.com and from the Bootstrap template.
### Acknowledgements

-   My Mentor Rohit for continuous helpful feedback.
-   Kasia for supporting all of us in all circumstances and for being available for individual support.
-   My classmates for their ongoing support and solidarity.
-   My family for their patience. Thanks for putting up with me in these intense times.