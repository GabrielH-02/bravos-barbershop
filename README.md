# Bravo's Bold Barbershop

![responsive-image](documentation/responsive-design.png)

The live link can be found [Bravo's Bold Barbershop!](https://bravos-bold-barbershop-c6f1277863c4.herokuapp.com/)

## Introduction
Bravo's Bold Barbershop is a data-driven website for the 'Bravo's Bold Barbershop'. The site has multiple purposes, as a site it provides insight to the barbershop itself and those who work there. It also takes on the responsibility of booking online appointments. The site is targeted towards users who like to know more information about the establishment and to become a member of ‘Bravo’s Bold Barbershop’ to book one of the many services the barbershop provides. Bravo himself wishes to advertise his barbershop freely with up-to-date information and staff as well as to have the ability to take online appointments to a particular work schedule.


## Planning

In this section, you will find resources which help with the creation of the project. As a note, some aspects of the planning have been altered to the current version of the site. As there have been changes in the scope of the project as well as the look of the project. 

### User Stories

Within this project, there were three main types of users to consider; a non-logged-in user, a logged-in site user, and the site admin/owner of the site.

#### Main User Goals

Non-logged-in User: The main goal for non-logged-in users is to navigate through an attractive and interactive website. With key and relevant information about the establishment. Such as, about the barbershop, about the team they have, and even creating personalized requests to the site owner. Another aspect is being able to become a logged-in user, simply and easily.

Logged-in User: The main goal for a logged-in user is to able to have the same access as the non-logged-in users but more. As a logged-in user, the goal is to able to have access to the the services the barber provides at what prices. As well as being able to create an appointment to my needs. In addition to this being able to delete and update my appointments.

Site Admin / Site Owner: The main goal for the site owner is accessible and able to have control over every aspect of the site. A site would like to add personnel to the site to provide a clear representation of the staff working there. As well as being able to write an about section which can be updated at any time. Another key aspect is the ability to receive hair requests as well. Another aspect which an owner can update is the services they provide and the price at which they are. And finally, the main goal is to view users and the appointments they make.

From those main points of information from those three main users the following stories were made to follow a clear representation of an agile workspace, each story with its acceptance criteria. These user stories dive deeper into every aspect of the requirements this site needs! (Note: Some user stories have not been completed due to a change in the scope of the project.)

For the full list of all 16 User Stories, this link will redirect you to the board of all the [User Stories](https://github.com/users/GabrielH-02/projects/5)


### Wireframe

After each user story was made, the wireframe was created to have a visual representation of what features were needed for the site, it also provided clarity for what data was required for the site. As a note, the style of the site was designed around the look of the ‘Start Bootstrap’ theme bootstrap template, which was titled; [‘Grayscale’](https://startbootstrap.com/theme/grayscale).

This wireframe has no responsive styles, however, when designing the wireframe this was heavily considered.  

#### ‘Home’ page

![wireframe-homepage-image](documentation/bbb-wireframe-01.png)

This is the wireframe that was designed for the ‘home’ page, the look of the page is consistent throughout the project every page has the ‘masthead’ with the title of that particular page. Followed by the ‘make an appointment’ button, to force the user to make an appointment. Then underneath are titled sections of the page. On this particular page, it is ‘our services’ which is a simple teaser of the services the barbershop provides, with links to view the ‘more’ about the services. Underneath this is ‘Opening times’ which clearly shows the user the times at which the barbershop is open. Then finally the is footer which has social media anchors, and more contact information. Such as the email address, phone number and addresses. The footer is consistent throughout the wireframe and project.

Note the page was designed twice one for a non-logged-in user and one for a logged-in user. The changes are the navigation bar and the links, once logged in the links redirect to the relevant pages. Whereas when not logged in the links will redirect to the ‘Sign-Up page. As well as this when I user finally logs in they are redirected to the ‘home’ page with a message. The same goes for logging out.   



#### ‘About’ page

![wireframe-aboutpage-image](documentation/bbb-wireframe-02.png)

The design is consistent with the ‘home’ page. As well as this the sections of ‘Our story’, ‘Our team’ and ‘Contact Us’ are included on this page. Each of these aspects is data that the site admin can control. The ‘Our Story’ section contains an image, a body of text and an updated date. This can be updated by the admin whenever they want to update their story of the barbershop. ‘Our team’ section is a display of all the stylists that currently work at the barbershop. Each with their name, a profile image and job title. The number of stylists then can be paginated. The ‘Contact Us’ section is a form for the user to make a personalized request to the site owner.  

#### ‘Sign-In’, ‘Sign-up’ and ‘Sign-out’ pages

![wireframe-signinpage-image](documentation/bbb-wireframe-03.png)

![wireframe-signuppage-image](documentation/bbb-wireframe-04.png)

![wireframe-signoutpage-image](documentation/bbb-wireframe-05.png)

These three pages were designed to stay consistent with the style of the site, but also allow the user to make an account. This was designed with Django All-Auth in mind. 

#### ‘Our Services’ page

![wireframe-ourservicespage-image](documentation/bbb-wireframe-06.png)

This page was designed exclusively for logged-in users and stays consistent with the look of the whole site. It displays a list of all the services the barbershop provides and the price of them. 

#### ‘My Appointments’ page

![wireframe-myappointmentspage-image](documentation/bbb-wireframe-07.png)

The final key aspect of the site is the ‘My Appointments’ page. It was designed to give the user full access to creating, reading, updating and deleting appointments. With the user of forms and modal. As well as messages indicating changes. Whilst also staying true to the site’s style.

For full access to the wireframe, this link will redirect to the Balsamiq workspace for [Bravo’s Bold Barbershop…](https://balsamiq.cloud/scq8ivf/pd49j2m/r2278)



### Entity Relationship diagrams

After the creation of the wireframe, it was time to map out the data of the site and how everything would connect. So the following ERD was created. Note; Changes were made to the models as the scope and complexity of the project changed.

![erd-image](documentation/erd-design.png)

## Features

### Existing Features

#### General Features

#### ‘Home’ page

#### ‘About’ page

#### ‘Sign-in’, ‘Sign-up’ and ‘Sign-out’ pages

#### ‘Our Services’ page

#### ‘My Appointments’ page

### Features Left to implement

## Technologies Used

### Languages

* [HTML5](https://html.spec.whatwg.org/multipage/)  - Used to write the content of the site
* [CSS3](https://www.w3.org/TR/css-2022/)   - Used to style the site.
* [JavaScript](https://www.w3.org/TR/css-2022/)   - Used to create functionality for the site.
* [Python](https://www.python.org/) - Used to create and navigate the project.

### Frameworks
* [Django](https://www.djangoproject.com/) - Used to create project structure and utilities.
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Used to have built-in stylisation and functionality.   

### Django Add-on Packages
* [Allauth](https://docs.allauth.org/en/latest/) - Used for account management
* [Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html) - Used functionality and stylisation of the forms
* [Gunicorn](https://gunicorn.org/) - Used to deploy to Heroku
* [Sumernote](https://pypi.org/project/django-summernote/) - Used for stylisation to admin panel
* [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) - Used for collecting static files

### Databases
* [Cloudinary](https://cloudinary.com/) - Used for storing uploaded images by admin
* [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) - Used for the application database
* [ElephantSQL](https://www.elephantsql.com/) - Used as PostgreSQL database service

### Development
* [Git](https://git-scm.com/) - Used for version control
* [Gitpod Template](https://github.com/Code-Institute-Org/gitpod-full-p3) - Used to create a workspace, provided by Code Institute!
* [Gitpod](https://www.gitpod.io/) - Used IDE to create a project
* [Github](https://github.com/) - Used for hosting repository 
* [Heroku](https://www.heroku.com/home) - Used to deploy the site.

### Planning
* [Balsamiq](https://balsamiq.com/) - Used to create a wireframe to design a project
* [LucidChart](https://www.lucidchart.com/) - Used to create ERD 

### Testing
* [HTML Validator](https://validator.w3.org/)   -Used to check and validate the HTML code used in the site.
* [CSS Validator](https://jigsaw.w3.org/css-validator/) -Used to check and validate the CSS code used in the site.
* [JavaScript Validator](https://jshint.com//) - Used to check and validate the JavaScript code used in the site.
* [Python Validator](https://pep8ci.herokuapp.com/) - Used to check and validate the Python code used in the site.
* [Google Lighthouse](https://chromewebstore.google.com/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=de) - Used to check and the performance and accessibility of the site.

### Others
* [Grayscale](https://startbootstrap.com/theme/grayscale) - Used as a template theme.
* [Am I Responsive](https://ui.dev/amiresponsive) - A site used to test the responsiveness of the page.
* [FontAwesome](https://fontawesome.com/)   - Linked for all icons used on the site
* [Google Fonts](https://fonts.google.com/) - Source of the site’s fonts.
* [Favicon Generator](https://realfavicongenerator.net/) - Used to generate favicon files.
* [Pexels](https://www.pexels.com/) - Used for stocked images.


## Testing

### Automated Testing

### Manual Testing

### Validator Testing

### Accessibility 

### Bugs

#### Fixed Bugs

#### Unfixed Bugs

## Deployment

## Credits

### Content

### Media


