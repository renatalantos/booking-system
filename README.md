
# Milestone Project 4 - Restaurant Booking System for Renata's Restaurant
![All devices](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/site%20features/Intro%20to%20site%20readme.JPG)

[View the live project here.](https://restaurant-reservation-sytem.herokuapp.com)

This is the main marketing website for the fictitious website, Renata's Restaurant. It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential visitors and users.

## Table of Contents

* Introduction
* UX
    - User Stories
        -  First Time Visitor Goals
        -  Returning Visitor Goals 
* Layout

    - Design
        -  Colour scheme
        -  Typography
        -  Images
    - Wireframes
        - Discrepancy with original ideas
        - Links to Wireframes

++++++ Correct table content ++++++++++

 * Features

* Structure
  * Wireframes
  * Discrepancies with original ideas
  * Colours
  * Typography

* Technologies

* Testing

* Bugs, Issues

* Deployment

* Acknowledgements
## Introduction

The product Restaurant Booking System is a fictitious restaurant website. 
Beside being able to view pages like the home page, menu and the contact page, users are also able to create an account, sign in and avail of the table booking feature, which unregistered users don't have access to. Through the booking, users can access all their previous bookings, edit and delete them. Site user administrators have access to all bookings and all create, edit and delete functionalities.
The site has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.

## User Experience (UX)

-   ### User stories 

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the business.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to sign up for a user account to access restricted content.
        4. As a First Time Visitor, I want to create a table booking, view booking details, and learn what changes I can make on created bookings.
        5. As a First Time Visitor, I want to sign out of my user account at the end of the session to keep my account related details safe.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to sign into my user account.
        2. As a Returning Visitor, I want to create a table booking, view my current and previous booking details, and alternatively edit them or delete them.
        3. As a Returning Visitor, I want to sign out of my account at the end of the session to keep my account safe.
        4. As a Returning visitor I want to like on the restaurant services.
        5. As a Returning visitor I want to send messages and queries to the site owner.

## Layout
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


## Features
-   ### Responsivity

The application is responsive on all device sizes, thanks to the Boostrap theme. In mobile view there is a collapsible menu icon. All images, text labels, forms get appropriately resized. There is an exception, however: when bookings are displayed in the database table in the view_booking.html, on mobile phone screens in portrait mode there is not enough room for all columns to be shown. However, Bootstrap adds a slide bar so that user can slide the page content from left to right. 

[View database table in portrait mode on smallest mobile device](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/site%20features/Booking%20table%20with%20slide%20bar.JPG)

In mobile phone landscape mode all columns show beside one another, however, the nav header and footer don't reach from one end of the page to the other.

[View database table in landscape mode on smallest mobile device](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/site%20features/Booking%20table%20landscape.JPG)

-   ### Interactive elements
    -   #### Nav links for Home, Menu, Book a Table, Contact Us, Register, Login and Logout pages
    -   #### Form input fields on signup, register, signout, table booking, edit booking and delete booking forms
    -   #### Buttons - including form buttons (signup, register, signout, table booking, edit booking and delete booking form buttons) and page buttons (Visit Us button on Home page)

## Technologies Used

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
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript. It is also used for the Bootstrap Tempus Dominus datetime picker and to define visibility duration for popup messages that signal successful completion of different form related activities.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process. [Wireframes](https://github.com/renatalantos/booking-system/tree/main/restaurant/documents/screenshots/wireframes)
1. [Lucidchart:](https://www.lucidchart.com/)
    - Lucidchart was used to create the data model of the project . [View Booking data model](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/wireframes/1%20model%20only%20with%20Booking.JPG)   
1. [SQLite3 database:](https://en.wikipedia.org/wiki/SQLite)
    - SQLite3 is Django's default database system
1. [Cloudinary:](https://cloudinary.com/)
    - I used cloudinary for cloud-based storage and partly for linking of my website images.
1. [Heroku:](https://www.heroku.com/)
    -  Heroku is used for the deployment and ultimate cloud-based storage of my application.

## Testing

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
        2. The login page sign in form contains a link where user can create an account from: "If you have not created an account yet, then please sign up to make reservations."
        3. Alternatively, the user might want to create an account from the navbar link "Register", which will take them straight to the signup form. 
        4. Once the user signs up by creating a username, optionally adding an email address, creating and repeating the password, they are redirected to the home page. 
        5. In the navbar now, the Login and Register navbar links have disappeared, Logout and Logged in as (Created username) appear instead.
    
    4. As a First Time Visitor, I want to create a table booking, view booking details, and learn what changes I can make on created bookings.


        1. Once the first-time user has created an account and been redirected to the home page, they can click on the Book a Table nav link again. This time they will see a hero image with tables and a booking form with the  following form elements:
            - ### Form title "Table Booking Form"
            - ### A request to the user asking them not to put in a past date
            - ### The following input fields:
                *   Customer name - takes alphanumerical characters
                *   Phone number - takes alphanumerical characters
                *   Reservation date and time - has a calendar popping up with date and time picker
                *   Number of customers - takes only positive whole numbers (not 0)
            - ### Submit booking button


        2.  User enters in Customer name, phone number, reservation date and time and number of customers on the form.
        Although only two fields are marked with an asterisk, customer cannot submit without filling in all fields. 
        
        
        [Please click on this link for more detail on validation issues and successful validation on the booking form: ]()
        
        
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
        - ### Form title "Edit Your Booking"
        - ### Link "Changed my mind, back to my booking" in case customer has changed their mind
        - ### The following input fields:
                *   Customer name - as per user input when creating a booking
                *   Phone number - as per user input when creating a booking
                *   Reservation date and time - as per user input when creating a booking
                *   Number of customers - as per user input when creating a booking
        - ### Submit edited booking button

        If user clicks on "Changed my mind, back to my booking" link, they are taken back to the previous page, to the table with all booking details.
        Whether user edits their booking details on the form or leave them unedited on the form and click on the "Submit edited booking" button, they are taken back to the previous page, to the table with all booking details. Additionally, user sees the following popup message "Your booking has been updated". If user enters a date in the past, the form won't update and the success message won't appear. (See validation details) Customer can then go onto any page after as per navbar links, which are displayed straight above the bookings table.
        
        5. If user decides, that they wish to delete their booking, they must click on the Delete Booking button. The booking will appear on a separate page, with a waste paper basket image, on a form like the table booking form. The form has the following elements:
        - ### Form title "Are You Sure You Wnt to Delete this Booking?"
        - ### Link "No, back to my booking" in case customer has changed their mind
        - ### The following input fields:
                *   Customer name - as per user input when creating a booking
                *   Phone number - as per user input when creating a booking
                *   Reservation date and time - as per user input when creating a booking
                *   Number of customers - as per user input when creating a booking
        - ### Delete booking button

        If user clicks on "No, back to my booking" link, they are taken back to the previous page, to the table with all booking details.
        When user clicks on the "Delete booking" button, they are taken back to the previous page, to the table with all booking details, without the deleted booking details. Additionally, user sees the following popup message "Your booking has been deleted". If customer deletes a booking where a date in the past now, the success message won't appear. (See validation details) Customer can then go onto any page after as per navbar links, which are displayed straight above the bookings table.

        
    5. As a First Time Visitor, I want to sign out of my user account at the end of the session to keep my account related details safe. 
        1. To accomplish this, user clicks on the Logout navbar link.
        2. A logout form with matching image as a background and with the following elements:
        - ### Form title "Sign Out"
        - ### Text "Are you sure you want to sign out?"
        - ### Sign Out button
        3. User is taken to the home page, at the same time the message "You have signed out" appears.



-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the new programming challenges or hackathons.

        1. These are clearly shown in the banner message.
        2. They will be directed to a page with another hero image and call to action.

    2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

        1. The navigation bar clearly highlights the "Contact Us" Page.
        2. Here they can fill out the form on the page or are told that alternatively they can message the organisation on social media.
        3. The footer contains links to the organisations Facebook, Twitter and Instagram page as well as the organization's email.
        4. Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
        5. The email button is set up to automatically open up your email app and autofill there email address in the "To" section.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
        2. Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
        3. If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.

        1. The user would already be comfortable with the website layout and can easily click the banner message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
        1. At the bottom of every page their is a footer which content is consistent throughout all pages.
        2. To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
        3. There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   On some mobile devices the Hero Image pushes the size of screen out more than any of the other content on the page.
    -   A white gap can be seen to the right of the footer and navigation bar as a result.
-   On Microsoft Edge and Internet Explorer Browsers, all links in Navbar are pushed upwards when hovering over them.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   The full-screen hero image code came from this [StackOverflow post](https://stackoverflow.com)

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.