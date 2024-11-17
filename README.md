# Bandon Dog Grooomers

![AmIResponsive](/documentation/Responsive/amiresponsive.PNG)

Welcome to Bandon Dog Groomers website,

This site was created with dog owners and their K-9 friends in mind. The purpose of the site  is to inform users of the site about the dog grooming service being provided. The users can visit the site to gain more insight into the services provided and allow potential customers to register, login and book appointments for their dogs for a variety of dog grooming services.

The deployed site can be accessed [here](https://django-dog-groomers-79f623645af8.herokuapp.com/) .

## UX
The design approach was to create a simple, user friendly site, allowing the user options to view  its content, register, login and make bookings in a seamless , simplistic way. 
Before any coding of the site took place, as a part of the planning stage, I created an initial wireframe to conceptually build a visual display of the aplication. 
 - Home Page
  - ![HomePage](/documentation/Wireframes/Home_Page.PNG)
 - Login Page
  - ![LoginPage](/documentation/Wireframes/Login_Page.PNG)
 - Sign Up Page
  - ![SignUpPage](/documentation/Wireframes/Register_Page.PNG)
 - Booking Page
  - ![BookingPage](/documentation/Wireframes/Booking_Page.PNG)
 - Booking Confirm
  - ![BookingConfirm](/documentation/Wireframes/BookingConfirm_Page.PNG)
 - Delete Booking
  - ![DeleteBooking](/documentation/Wireframes/DeleteBooking_Page.PNG)
 - Delete Confirm
  - ![DeleteConfirm](/documentation/Wireframes/DeleteBookingConfirmation_Page.PNG)

## Color Scheme
I used a combination of the following colours:
- Gold/Orange #f2b30d 
- White #fafafa 
- Navy #353354 

I felt these worked well visually to compliment the boostrap buttons which used a .warning class and the Leaflet JS colour scheme for maps zoom control and also to compiment the colour schemes within the gallery photos,  to present an overall colour theme that looked consistent, as a user experience.


## User Stories
My user stories can be viewed on my GitbHub project [here](https://github.com/users/petermcloughlin/projects/7)

## Features
- Navbar 
    -   The navbar is a responsive one utilising a responsive burgar icon on mobile and extended display on larger devices.
    ![Navbar](/documentation/Features/Navbar.PNG)
- About
    - The About Us section gives some basic information about Bandon Dog Groomers its servcices and contact details for the site visitor.
    ![AboutUs](/documentation/Features/AboutUs.PNG)
- Services
    -   The Services section uses a simplistic display combining fontawesome icons, bootstrap cards and short descriptions and prices.
    ![Services](/documentation/Features/Services.PNG)
- Gallery
    -   The gallery displays six .wepb images as a part of the user experience to give a visual understanding of the kind of services and treatments on offer, complimenting the services section above it.
    ![Gallery](/documentation/Features/Gallery.PNG)
- Footer
    -   The footer is split into three sections displaying the opening times, interactive LeafletJS map with responsive pin and contact details, which include the business address, telephone number, email address and social media icons.
    ![Footer](/documentation/Features/Footer.PNG)

## Site Pages
- HomePage
- Login Page
- Register Page
- Profile Page
- Booking Page

## Tools and Technologies
The tools used to develop the project included the following:
### GitPod
This was the IDE used to write the code for the project with access was supplied by Code Institute.

### GitHub
I used my GitHub account as a repository to save the source code for the project and to link to my GitPod wrokspace when developing the code. GitHub was used to create user stories as a part of the planning stage of the project.

### Heroku
Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.
    
DATABASE_URL - user's own value 
DISABLE_COLLECTSTATIC - value of 1 (*this is temporary, and can be removed for the final deployment*)
SECRET_KEY - user's own value

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
### Django Framework
Django version 4.2.16 was installed and used to scaffold the files and project structure.
### Python
Python was used to code the urls.py files in both the project and app folders, the views.py, forms.py and models.py files within the booking app folder.
### Bootstrap 5
Bootstrap 5 was used to style the base.html, with the following html files inheritng from this.
- index.html
- booking.html
- edit.html
- delete.html
- profile.html
- profile-no-booking.html
- login.html
- signup.html
- logout.html

### LeafletJS
I used LeafletJS to connect to its map's api. This map is used in the site footer to display an interactive map, displaying the business location with a responsive, clickable location pin.

### CSS
For the most part, the site's css is governed by Bootstrap 5 , however I did create my own custom style.css file for layout and component positioning and site colour.

### HTML
The site's html parent layout was taken care of with the base.html in the templates folder. All other pages wihtin the site inherited from this.

## Deployment
I used [GitHub](https://github.com/) as my source control for connection to my project's workspace on GitPod. The application was successfully deployed to [Heroku](https://dashboard.heroku.com/), by following the Code Institute's instructions for app deployment to Heroku. A range of commit's to my GitHub account and deployments to Heroku were completed throughout various stages of the project implementation and coding stages.

## Testing
I completed a series of manual tests on the application from accessing the site manually on desktop, tablet and mobile.
I also ran some tests on the HTML, Lighthouse, CSS and Python to check for any errors in the code.

###  HTML
I used [W3C HTML Validator](https://validator.w3.org/) to validate the site's html.

#### Results
 - [HomePageValidation](/documentation/HTML/HomePage.PNG)
 - [LoginPage](/documentation/HTML/LoginPage.PNG)
 - [LogoutPage](/documentation/HTML/LogoutPage.PNG)
 - [BookingPage](/documentation/HTML/BookingPage.PNG)
 - [BookingForm](/documentation/HTML/BookingFormPage.PNG)
 - [BookingUpdatePage](/documentation/HTML/BookingUpdatePage.PNG)
 - [BookingDeletePage](/documentation/HTML/BookingDeletePage.PNG)


###  Lighthouse
I used Google chromes Lighthouse reporting to assess the site for SEO, accessibility and performance on both mobile and desktop.

#### Mobile Results
 - [Home Page](/documentation/Lighthouse/Mobile_HomePage.PNG)
 - [Gallery](/documentation/Lighthouse/Mobile_HomePageGallery.PNG)
 - [Login Page](/documentation/Lighthouse/Mobile_LoginPage.PNG)
 - [Profile Page](/documentation/Lighthouse/Mobile_ProfilePage.PNG)
 - [SignUp Page](/documentation/Lighthouse/Mobile_SignUpPage.PNG)
 - [Booking Update](/documentation/Lighthouse/Mobile_BookingUpdate.PNG)
 - [Booking Delete](/documentation/Lighthouse/Mobile_BookingDelete.PNG)
 - [Booking Button](/documentation/Lighthouse/Mobile_BookButton.PNG)
 - [SignOut Page](/documentation/Lighthouse/Mobile_SignOut.PNG)
#### Desktop Results
 - [Home Page](/documentation/Lighthouse/Desktop_HomePage.PNG)
 - [Gallery](/documentation/Lighthouse/Desktop_HomePageGallery.PNG)
 - [Login Page](/documentation/Lighthouse/Desktop_LoginPage.PNG)
 - [Profile Page](/documentation/Lighthouse/Desktop_ProfilePage.PNG)
 - [Booking Page](/documentation/Lighthouse/Desktop_BookingPage.PNG)
 - [Booking Update](/documentation/Lighthouse/Desktop_BookingUpdate.PNG)
 - [Booking Delete](/documentation/Lighthouse/Desktop_BookingDelete.PNG)
 - [Booking Button](/documentation/Lighthouse/Desktop_BookButton.PNG)
 - [SignOut Page](/documentation/Lighthouse/Desktop_SignOut.PNG)
 
 
###  CSS
I used [JigSaw's CSS validator](https://jigsaw.w3.org/css-validator/) to validate my custom css style.css file.
You can view the results below;
![CSSValidationResults](/documentation/CSS/JigsawCSSValidation.PNG)

###  Python
I used Python's [CI Python Linter](https://pep8ci.herokuapp.com/) to test my .py files for PEP8 validation.

#### Results:
- Forms
![Forms](/documentation/Python/FormsTest.PNG)
- Models
![Models](/documentation/Python/ModelTest.PNG)
- Views
![Views](/documentation/Python/ViewsTest.PNG)

## Bugs
A notable bug I encountered during the development of the application involved the implementation of the DateTimePicker. Initially, I encountered some issues when trying to display the DateTimePicker correctly on the Booking web page for making and updating bookings. I used some web searches such as [StackOverFlow](https://stackoverflow.com/), [Django-Docs](https://docs.djangoproject.com/en/5.1/) and Tutor support with the Code Institute to assist with its display. 
Howver, I do have another ongoing bug which I will attempt to resolve. It involves restricting the display of the Dates to weekdays and the times ranges within the 09:00 to 19:00 hours. Some solutions I found online were a little daunting for me to amend and implement so I have decided for now to list this as a known bug in my application. I hope by project 5 and beyond to have this resolved and working seamlessly for the purposes of a positive user experience and seamless integration with the data model and database.

## Summary / Reflection


