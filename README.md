# Bandon Dog Grooomers

![AmIResponsive](/documentation/Responsive/amiresponsive.PNG)

Welcome to Bandon Dog Groomers website,

This site was created with dog owners and their K-9 friends in mind. The purpose of the site  is to inform users of the site about the dog grooming service being provided. The users can visit the site to gain more insight into the services provided and allow potential customers to register, login and book appointments for their dogs for a variety of dog grooming services.

The deployed site can be accessed [here](https://django-dog-groomers-79f623645af8.herokuapp.com/) .

## UX
The design approach was to create a simple, user friendly site, allowing the user options to view  its content, register, login and make bookings in a seamless , simplistic way. 

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
- HomePage
- About
- Services
- Gallery
- Footer

## Site Pages
- HomePage
- Login Page
- Register Page
- Profile Page
- Booking Page

## Tools and Technologies

## Deployment
I used [GitHub](https://github.com/) as my source control for connection to my project's workspace on GitPod. The application was successfully deployed to [Heroku](https://dashboard.heroku.com/), by following the Code Institute's instructions for app deployment to Heroku. A range of commit's to my GitHub account and deployments to Heroku were completed throughout various stages of the project implementation and coding stages.

## Testing
I completed a series of manual tests on the application from accessing the site manually on desktop, tablet and mobile.
I also ran some tests on the HTML, Lighthouse, CSS and Python to check for any errors in the code.

###  HTML
I used [W3C HTML Validator](https://validator.w3.org/) to validate the base.html and index.html.

![HTMLValidation](/documentation/HTML/HomePage.PNG)

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
- [Forms](/documentation/Python/FormsTest.PNG)
- [Models](/documentation/Python/ModelTest.PNG)
- [Views](/documentation/Python/ViewsTest.PNG)

## Bugs
A notable bug I encountered during the development of the application involved the implementation of the DateTimePicker. Initially, I encountered some issues when trying to display the DateTimePicker correctly on the Booking web page for making and updating bookings. I used some web searches such as [StackOverFlow](https://stackoverflow.com/), [Django-Docs](https://docs.djangoproject.com/en/5.1/) and Tutor support with the Code Institute to assist with its display. 
Howver, I do have another ongoing bug which I will attempt to resolve. It involves restricting the display of the Dates to weekdays and the times ranges within the 09:00 to 19:00 hours. Some solutions I found online were a little daunting for me to amend and implement so I have decided for now to list this as a known bug in my application. I hope by project 5 and beyond to have this resolved and working seamlessly for the purposes of a positive user experience and seamless integration with the data model and database.

## Summary / Reflection


