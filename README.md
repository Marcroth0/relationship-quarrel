# relationship-quarrel

![amiresponsive](static/images/readme-images/quarrel-responsive-readme.png)

Live link:

## About:

Quarrel is a platform where arguments are come to an end. Two people face off in an attempt to solve their argument once and for all. Do you have a spouse who you claim never to do the dishes and when you bring it up they claim that you're the one never doing the dishes? Usually on the internet we just hear one-sided stories "my spouse/friend never does this and always does this, bla bla" - with Quarrel you get both sides of the story. Other users are able to like, to choose who's right, as well as offer advice/comment.

### Table of Contents

1. [Goals](#goals)
   1. [Organisational Goals](#organisation-goals)
   2. [User Stories](#user-stories)
2. [Design](#design)
   1. [Box Shadow](#box-shadow)
   2. [Color palette day](#color-palette-day)
   3. [Color palette night](#color-palette-night)
3. [Planning](#planning)
   1. [Fonts](#fonts)
4. [Testing](#testing)
   1. [Lighthouse](#lighthouse)
   2. [Validator](#validator-testing)
5. [Credits](#credits)

## Goals

### Organisation Goals

### User Stories

1. As a Site user I can view posts so that I can choose which i'd like to open

2. As a Site user I can Click on a post so that read the full post

3. As a Site User / Admin I can view comments on a post so that i can read the comments

4. As a Site user / Admin I can view the number of likes on each post so that I can see which argument is winning

5. As a Site User I can create an account so that I can comment, like, and post

6. As a Site User I can create a post so that I can view it on the site and receive comments from other users

7. As a Site user I can leave comments on a post so that I can be a part of the conversation

8. As a Site User I can create, read, update and delete posts so that I can manage my posts content

9. As a Site user I can go to next page so that I see more posts

10. As a User I can like which of the two posts i agree with so that I can be a part of deciding the winner of the argument

11. As a User I can update my post so that I can edit a post if something went wrong

12. As a user I can delete my post so that I, or anyone else, can see it anymore

13. As a user I can delete my account so that I don't have an account anymore

14. As a user I can have my own posts in a profile so that I can easily reach them

15. As a User I can delete my comment so that I can write a new one, or if I regret it

# UX

## Strategy

Target Audience:

- 18-40 year olds
- People who are looking to take arguments with a bit of comedy
- People who would like to improve their communication skills
- People who've seen too many one-sided-stories

The audience is looking for something where both sides are visible. With the ability to post both arguments and hash it out once and for all, with complete strangers on the internet, the site allows the user to read different points of views and thereafter see whose argument was the best.

## Design/Structure

Quarrel has been designed to be easily navigated, easily managed, and with few but important functions. Straight-forward argument-solving website. Through two apps and three models it acchieves its goal.

Apps:

1. Quarrelapp:
   Core functionality containing models(Post, Comments, CommentPost)
2. Websitemanage:
   Holds basic views-functions such as delete user, deactivate user, delete post, general views.

### Databases:

Quarrelapp holds all the databases, consisting of:

1. Post in combination with CommentPost allows for the ability of letting the user create a post, but through a OneToOneField with CommentPost, separate the likes and comments. Through the ability of calling different keys, connected to each argument, it allows for the possibility of cross-liking as well as future customization of the comment section(more on that in improvements) With each post, the model generates the users post but splits the content one and content two into separate keys which are then callable in views.
2. Comment allows for users to comment on posts with date-stamps, as well as Post, have a built-in CASCADE in order to delete all comments related to user if user decided to delete their account.

Below is a diagram of the correlation between the models:

### Planning

I wireframed it using Balsamiq:

Landing page:

![wireframe](static/images/readme-images/readme-landing-page-mobile.png)

Landing page - Mobile:

![wireframe](static/images/readme-images/readme-landing-page-mobile.png)

A post full screen:

![wireframe](static/images/readme-images/readme-post-detail-page.png)

### End Design Result:

Navbar:
![navbar](static/images/readme-images/quarrel-navbar-readme.png)

Navbar(Logged in):
![navbar](static/images/readme-images/quarrel-navbar-logged-readme.png)

Hero:
![hero](static/images/readme-images/quarrel-hero-readme.png)

Quarrels:
![quarrels](static/images/readme-images/quarrel-quarrels-readme.png)

Post Detail:
![postdetail](static/images/readme-images/quarrel-postdetail-readme.png)

About page:
![about](static/images/readme-images/quarrel-about-readme.png)

Footer:
![footer](static/images/readme-images/quarrel-footer-readme.png)

### Color Palette

Colors:
![palette](static/images/readme-images/quarrel-color-readme.png)

### Reasoning

The design of the website was crucial. It being a "argument-solver" it needed to be flimsical and not take the initial argument, or the definition of an argument, all that seriously. With the ability of seeing it, instead of an obstacle, as a "funny challenge" to post it to the internet. Hence the sarcastic comments spread around the website. With a comical twist, but on serious subjects, it will hopefully invoke a funny tone in the comments as well as an appearance of the "good side" of the internet which are there to actually help.

### Fonts

Font-family: "Mochiy Pop P One", Montserrat;

##

## Testing

I tested the responsiveness of the site on the below units, using chrome dev as well as some in real life testing:

**Mobile**

- Moto G4 (360x640)
- Galaxy S5 (360x640)
- Pixel 2 (411x731)
- Pixel 2 XL (411x823)
- iPhone 5/SE (320x568)
- iPhone 6/7/8 (375x667)
- iPhone 6/7/8 Plus (414x736)
- iPhone X (375x812)
- iPad (768x1024)
- iPad Pro (1024x1366)

**Browsers:**

- Chrome
- Mozilla Firefox
- Safari
- Edge

### Manual testing

See further on click [here](readme-testing.md)

### Lighthouse

![lighthouse](assets/images/lighthouse-memory-readme.png)

### Validator Testing

W3 HTML Validator:

![htmlvalidator](assets/images/html-validator-readme.png)

W3 CSS Validator:
![cssvalidator]()

Pep8 validator:
![jsvalidator](assets/images/js-validator-readme.png)

## Unfixed Bugs

No known bugs.

## Technologies used:

Python
Django
Cloudinary
Crispy forms
Github
Vscode
PostgreSQL
SQlite
Pep8
Prettier
ImgBot
Google Developer Tools
Bootstrap
Git
AmIResponsive

## Improvements

## Features Left to Implement

- A reply-to-comments-function.
- The ability for one person to write their argument, then through a link allow the second one write theirs, when received the post get created and published.
- Pagination on post_detail for a smoother site experience and a feeling of "just one more"

## Deployment

- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - https://marcroth0.github.io/memory-game/

## Credits

- A general shout-out to [StackOverflow](https://stackoverflow.com/)

## Media
