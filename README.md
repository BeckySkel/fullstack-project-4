# Recipebook

![The Recipebook website displayed on different devices](/assets/images/responsive-test.png)

- Recipebook is a social recipe website which combines the functionality of social media with the practicality of a recipe hosting site. Users can sign-up to share their own recipes, save and like other's, and interact with each other through commenting.   

## Links

[Link to the live project hosted on Heroku (right click to open in new tab)](https://pp4-recipebook.herokuapp.com/)

[Link to the project repository hosted on Github (right click to open in new tab)](https://github.com/BeckySkel/fullstack-project-4)

---
## Table of Contents
- [Strategy](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#strategy)
    - [Target Audience](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#target-audience)
    - [User Stories](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#user-stories)
- [Scope](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#scope)
    - [Research](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#research)
    - [Future Features](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#future-features)
    - [Testing](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#testing)
- [Structure](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#structure)
    - [Wireframes](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#wireframes)
    - [Information Architecture](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#information-architecture)
- [Skeleton](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#skeleton)
    - [Current Features](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#current-features)
    - [Technologies Used](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#technologies-used)
- [Surface](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#surface)
    - [Design](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#design)
    - [Deployment](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#deployment)
- [Credits](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#credits)
    - [Content](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#content)
    - [Media](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#media)
    - [Acknowledgemnets](https://github.com/BeckySkel/fullstack-project-4/blob/main/README.md#acknowledgements)

---
## Strategy

### Target Audience
- This site is targeted towards anyone who enjoys cooking - beginner or advanced - who would like to either share their own recipes with others or search for some new ones to try.

- View [User Personas](documents/personas.pdf)

### User Stories

#### Admin
*These are staff/admin users who maintain the site and manage it's contents.*
- [#1](https://github.com/BeckySkel/fullstack-project-4/issues/1) As an admin, I can edit and remove recipes so that I can manage the site contents.
- [#2](https://github.com/BeckySkel/fullstack-project-4/issues/2) As an admin, I can read and remove comments so that inappropriate comments can be removed.

#### Recipe Sharers
*These are users who intend to share recipes on the platform.*
- [#3](https://github.com/BeckySkel/fullstack-project-4/issues/3) As a recipe sharer, I can post my own recipes so that I can share them with others.
- [#4](https://github.com/BeckySkel/fullstack-project-4/issues/4) As a recipe sharer, I can set my posted recipes to private or public so that I can control who views them.
- [#5](https://github.com/BeckySkel/fullstack-project-4/issues/5) As a recipe sharer, I can edit my posted recipes so that I can update any mistakes/changes.
- [#6](https://github.com/BeckySkel/fullstack-project-4/issues/6) As a **user**, I can create an account so that I can interact with other users content and create my own.
- [#8](https://github.com/BeckySkel/fullstack-project-4/issues/8) As a **user**, I can categorise my posted/saved recipes so that I can find them more easily in the future.
- [#11](https://github.com/BeckySkel/fullstack-project-4/issues/11) As a **user**, I can attach notes to my saved recipes so that I can view them later and make my own adjustments.
- [#12](https://github.com/BeckySkel/fullstack-project-4/issues/12) As a recipe sharer, I can add tags to my recipes so that they are more visible to others.

#### Recipe Viewers
*These are users who intend to view recipes that others have posted.*
- [#6](https://github.com/BeckySkel/fullstack-project-4/issues/6) As a **user**, I can create an account so that I can interact with other users content and create my own.
- [#7](https://github.com/BeckySkel/fullstack-project-4/issues/7) As a recipe viewer, I can save recipes to my library so that I can access them again later.
- [#8](https://github.com/BeckySkel/fullstack-project-4/issues/8) As a **user**, I can categorise my posted/saved recipes so that I can find them more easily in the future.
- [#9](https://github.com/BeckySkel/fullstack-project-4/issues/9) As a recipe viewer, I can like and comment on other's recipes so that I can share my opinion.
- [#10](https://github.com/BeckySkel/fullstack-project-4/issues/10) As a recipe viewer, I can search for recipes so that I can find one that matches what I'm looking for.
- [#11](https://github.com/BeckySkel/fullstack-project-4/issues/11) As a **user**, I can attach notes to my saved recipes so that I can view them later and make my own adjustments.
- [#13](https://github.com/BeckySkel/fullstack-project-4/issues/13) As a recipe viewer, I can view the nutritional information of a recipe so that I can make an informed decision based on my dietary needs.
- [#14](https://github.com/BeckySkel/fullstack-project-4/issues/14) As a recipe viewer, I can view the recipe difficulty so that I can select a recipe which would suit my skill set.
- [#15](https://github.com/BeckySkel/fullstack-project-4/issues/15) As a recipe viewer, I can view the time requirements for the recipe so that I can select a recipe based on the time it takes to prepare.
- [#16](https://github.com/BeckySkel/fullstack-project-4/issues/16) As a recipe viewer, I can create a printable shopping list from the ingredients list so that I can purchase the necessary ingredients to try the recipe.
- [#17](https://github.com/BeckySkel/fullstack-project-4/issues/17) As a recipe viewer, I can increment the required servings so that it can serve more or less people.

---
## Scope

### Research
- Before any planning, I conducted research into both social media and recipes websites and took note of the conventional layouts and formats as well as which features I thought enhanced the user's experience and would be good to include for my target audience(s).

### Future Features

#### Categorising Recipes
- In the future, I'd like to give the users an option to file their saved recipes into different categorised folders. This would involve adding a "New Folder" form where user's could create their own categories and a drop down on the save buton where users could select the folder/category they'd like to save the recipe to. These folders and their contents would then be available from the user's dashboard.

#### Nutritional Info
- Another helpful feature would be to add nutritional information to the recipes. This would either be an input from the recipe poster or, to make it more efficient and accurate, a connection to a nutrition API. The ingredients input would have to be changed to seperate the ingredients into their own inputs so that the API could be called based on the value.

#### Difficulty
- Either inputted by the poster at time of creation or voted on by the community (or both), the recipe could be assigned a difficulty (beginner, intermediate or pro) so that user's can select based on their current abilities. There is currently already a 'Quick & Easy' tag so this could be extended to include other difficulty tags.

#### Time Requirements
- Similarly to difficulty, the time requirememnts (prep and cook times) could be added to the recipe so that users can select based on their available time. Could be input by poster and/or voted on by community.

#### Shopping List
- A shopping list feature could be added to combine ingredients from multiple recipes into 1 printable list to save times for the user.

#### Required Servings
- Adding a counter to increment the required portions and thus adjusting the ingredient amounts. Similarly to the nutritional info, this would require splitting the ingredients into their own inputs and seperate amounts to make the mathematical adjustments possible. 

### Testing
- Throughout the project, I relied heavily on [Chrome Devtools](https://developer.chrome.com/docs/devtools/) to help me view this project on different screen sizes so that I could adjust elements, create media queries (by adding bootstrap classes) for responsive design and debug JavaScript by logging outcomes to the console.
- Code was also run through validators and automatic tests were run through Django
- Please follow [this link](documents/TESTING.md) for full list of tests carried out on this website

---
## Structure

### Wireframes
- After looking at common designs and features and deciding what I would like to include, I mapped out the intended features of the website using [Balsamiq](https://balsamiq.com/) to create wireframes of some of the page views.
- [View the wireframes here](documents/wireframes.pdf)
- The key differences between planning and the final product are presentation of the nav bar and the forms.

### Flowchart
- [Lucid](https://lucid.app/) was used to create a flowchart to map out the functions and processes of the application. Follow [this link](/assets/documents/flowchart.pdf) to view

### Information architecture
- Recipebook is a blog-style site with multiple pages which relies on the MVC framework: Django to present information from a recipe database and provide CRUD functionality.
- Recipes are presented as cards whilst browsing and full page views when viewing. the cards link to the recipe viewer.
- Recipes can be browsed using tags or searching in the search bar in the top right of the navbar.
- The home page displays 2 carousels with recipe cards for the newest and most popular recipes with a 'View more...' link on the last card (maximum 9 cards).
- All pages are responsive thanks to bootstrap classes.
- Browsing/search results pages present the related recipes in a large flex container.
- Profile pages can be viewed by either clicking the author/username at the top of the recipe detail page or selecting Dashboard from the Profile dropdown menu in the navbar (this will show your own profile if logged in).

### Data model
- The app is linked to a Google Sheets database and uses a variety of functions to interact with and manipulate the data.
- The database is split into 2 worksheets: users & entries.
- In the 'users' worksheet exists a table with each user's user id (their unique identifier, used to acceess the correct data), their name, username, password (both used to provide a level of security before accessing the data), their chosen goal month and goal amount for their savings budget (both used to calculate how much they should be saving each month in order to reach their goals).
- The 'entries' sheet holds a table with the entry id (unique identifier of the entry, used by the app to locate the correct entry when editing), the user's id (their unique identifier), the entry number (used by the user to interact with the entry), the month, incoming and outgoing data (all used to store and display the user's saving data) and the net savings calculated from the incoming and outgoing amounts.
- The majority of the functions use the user_id to locate the correct user's data to be manipulated but some also use indexing.

---
## Skeleton

### Current Features

#### Header
- Contains the site logo and navigation buttons

![Screenshot of the header on desktop](/assets/images/header-desktop.png)
![Screenshot of the header on mobile](/assets/images/header-mobile.png)
##### Logo
- Large and central, the logo features bright and bold colours with text shadow providing a 3D-effect to make it stand out.

![Screenshot of the logo](/assets/images/logo.png)
##### Navigation
- The navigation menu appears in top right on desktop with the icons splitting and appearing in each top corner on mobile to make selection easier on smaller screens. 
- A gear icon leads to the settings and a book has been used to represent a rulebook which brings up the game rules/hot to play.

![Screenshot of the navigation bar](/assets/images/navigation.png)

#### Game Board
- The main game area; contains boxes to display the user's and computer's choices of weapon, a weapon selection area with 3 to 5 buttons (depending on game mode) and a scoreboard area to communicate the outcome and scores.

![Screenshot of the game board on desktop](/assets/images/gameboard-desktop.png)
![Screenshot of the game board on mobile](/assets/images/gameboard-mobile.png)
##### Display Boxes
- Both blank to start with but later contain large icons representing the weapon choices once a game has been played. On desktop, both appear side-by-side to fill the landscape aspect of the screen, placed one on top of the other on mobile to fit into the the smaller portrait aspect. 
- Whilst the player is selecting their choice, a preview is displayed in a pale grey colour so that the user can see what they will be selecting. Once the player has chosen, the icon is displayed in a darker grey along with the computer choice in the other box to indicate that the battle has played-out.

![Screenshot of the display boxes](/assets/images/display-boxes.png)
##### Weapon Select
- 3 weapon choices displayed inline (Rock, Paper & Scissors). These buttons are where the player selects their weapon to battle with. This is then shown in the display box.
- After upgrading, the player has the option to add fourth and fifth options of Lizard and Spock to offer more possibilities of battle outcomes. These extra buttons can then be removed again if the player so chooses.

![Screenshot of the weapon choices with 3 options](/assets/images/weapons-rps.png)
![Screenshot of the weapon choices with 5 options](/assets/images/weapons-rpsls.png)
##### Scoreboard
- The scoreboard area is made up of the outcome display, progress bar and scores display stacked atop each other. 
- The progress is incrememented after each battle to either increase with a win, decrease with a loss or stay the same with a draw. Once the bar fills up, the player reaches the next level and unlock an upgrade. The bar is used to make it easy for the user to track their progress towards the next upgrade. The requirement to fill the bar gets more difficult with each level.
-  3 scores are displayed below: Wins, Losses and Draws. The current level is also tracked and displayed. The goal of the game is to beat the computer in as many turns as possibly so these scores can help the player track their progress and their ratio of successes and fails.

![Screenshot of the scoreboard on desktop](/assets/images/scoreboard.png)

#### Message Container
- Sliding in from the top of the screen when called, the message container can host 5 different messages. Some message can only be removed by selecting one of the button options whilst others can be removed with an exit icon in the top right. Slides out at the bottom of the screen when dismissed.
- Sizing differences between mobile and desktop but otherwise largely unchanged.
- The game buttons and navigation icons are disabled when a message is being displayed to avoid the game playing-out when not intended.

![Screenshot of the message container on desktop](/assets/images/message-desktop.png)
![Screenshot of the message container on mobile](/assets/images/message-mobile.png)
##### Welcome Message
- Welcomes the player to the game and gives them the opportunity to check the rules and settings before beginning the game. Or they can jump straight in with the **Begin!** button. Slides out when

![Screenshot of the welcome message](/assets/images/welcome.png)
##### Rules Display
- Can be called from the welcome message before the player begins the game if they have not played before. Can also be called by clicking the gear icon in the top right of the screen once the game has begun if a player needs some more help later on.
- Includes a brief paragraph with a description of the game and it's mechanics and an unordered list with details the outcome of each battle combination. The user can refer to this if they are unsure which weapon wins in a battle or if they are confused why a certain weapon would beat another.

![Screenshot of the rules display](/assets/images/rules.png)
##### Settings Menu
- This is where the user can toggle their unlocked upgrades on and off and choose between available background themes.
- The player may choose to swap out a background if they find it harder to view the content on certain colours/patterns so it was important to include an pportunity for them to do so.
- The addiditon of the Lizard & Spock buttons can make the game significantly more difficult so an option to remove them has been provided for players who do not wish to use them.
- buttons are disabled and greyed out

![Screenshot of the settings menu](/assets/images/settings.png)
##### Level-up Message
- Appears when the player has beaten the computer enough times to fill the progress bar and reach the next level. Provides the player with 3 (or less) random locked upgrades to choose from and is dismissed once one has been chosen. The ability to select an upgrade between levels is a way of rewarding the player for player and progressing and provide them with some customisation options.
- If there are less than 3 locked upgrades, any remaining buttons are disabled and display a message to say that no more upgrades are available to unlock.

![Screenshot of the level-up message](/assets/images/level-up.png)
##### Completion Message
- Once the player has completed the game and beat all 5 levels, one final message is displayed to congratulate them and ask if they would like to restart and try to beat their score. This message can only be removed by clicking restart. 
- The total number of turns it took for the player to complete the game is repoorted back to them so they have a goal to beat next time they play.

![Screenshot of the winner message](/assets/images/winner.png)

#### Backgrounds
- Different backgrounds are unlocked by playing the game and progressing through the levels. These are applied when unlocked and can be changed again in the settings menu if the player so chooses.
##### Blue Theme
- This is the standard background and features a subtle gradient from mint grenn to pale blue. It is a soft background and harmonises well with the other colours used on the site.

![Screenshot of the blue theme](/assets/images/blue.png)
##### Pink Theme
- Very similar to the blue theme, the pink theme is a subtle gradient of pale pink to a darker pink.

![Screenshot of the pink theme](/assets/images/pink.png)
##### Rainbow Theme
- This is the boldest background of the game. I suspect that it will be the most popular amongst players as it adds an extra layer of excitement to the game. A transparent white backing is added to the scoreboard so that the text can be more easily read against the busy background.

![Screenshot of the rainbow theme](/assets/images/rainbow.png)
##### Dark Theme
- The dark theme will be good for those who are playing in a dark room and find the lighter colours too much for their eyes. It also ups the contrast between elements if the player is having trouble viewing the screen in very bright light. The text on the screen is changed from grey to white to provide sufficient contrast. The gradient is similar to that of the blue and pink themes. 

![Screenshot of the dark theme](/assets/images/dark.png)
#### 404 Page
- A custom 404 page has been added for broken links and navigation back to the main page

![Screenshot of the 404 page on desktop](/assets/images/404-desktop.png)
![Screenshot of the 404 page on mobile](/assets/images/404-mobile.png)

### Technologies used

#### Languages
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Git](https://en.wikipedia.org/wiki/Git) for version control
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

#### Imported modules
- [os](https://docs.python.org/3/library/os.html)

#### Installed Libraries
- [cloudinary](https://pypi.org/project/cloudinary/)
- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/)
- [gunicorn](https://pypi.org/project/gunicorn/)
- [oauthlib](https://pypi.org/project/oauthlib/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [whitenoise](https://pypi.org/project/whitenoise/)

#### Frameworks
- [Django](https://www.djangoproject.com/)

#### Other resources
- [Gitpod](https://www.gitpod.io/) to alter and manage website files
- [Github](https://github.com/) to create and store website files
- [Heroku](https://dashboard.heroku.com/apps) to deploy web application
- [Chrome Devtools](https://developer.chrome.com/docs/devtools/) to test site throughout process
- [Balsamiq](https://balsamiq.com/) to create wireframes
- [Coolors](https://coolors.co/) to choose a colour scheme
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to help with styling and responsive design
- [Cloudinary](https://cloudinary.com/) for database and staic file storage
- [Google Fonts](https://fonts.google.com/) for the website font (Cabin)
- [Font Awesome](https://fontawesome.com/) used to add icons
- [Pexels](https://www.pexels.com/) for submitted recipe examples
- [Favicon.io](https://favicon.io/favicon-generator/) used to create favicon
- [Code Institute](https://codeinstitute.net/) fullstack developer course to provide learning materials
- [W3Schools](https://www.w3schools.com/) for help with common coding issues
- [Geeks For Geeks](https://www.geeksforgeeks.org/)  for help with common coding issues
- [Stack Overflow](https://stackoverflow.com/) for help with common coding issues
- [Am I Responsive?](https://ui.dev/amiresponsive) for device simulations

---
## Surface

### Design

#### Colour scheme

![The colour scheme I used for the standard display](static/images/colour-scheme.png)

- The colour-scheme is vibrant but soft to provide a pleasing display and compliment any recipe images displayed on the site.
- Bootstrap border and background colours were used on secondary features. Bootstrap button colours also used.
- I used [Coolors](https://coolors.co/) to help pick a colour scheme.

#### Imagery
- Images are uploaded by the users and stored in Cloudinary database.
- There are placeholder images for both recipes and profiles if image field empty
- Example recipes uploaded with images from Pexels

![Placeholder for recipe image](static/images/recipe_placeholder.png)
![Placeholder for profile image](static/images/profile_placeholder.png)

#### Typography
- All text is in the Quicksand font. It is a display sans serif with rounded terminals. It is designed for display purposes but kept legible enough to use in small sizes as well[*](https://fonts.google.com/specimen/Quicksand/about?query=quicksand). It pairs well with the softer colours and rounded corners of the design.
- Sans serif has been used as the fallback option since it is the closest web-safe font.

#### Icons
- [Font Awesome](https://fontawesome.com/) icons were used for navigation buttons as well as in creation of the placeholder images.

### Deployment
- This site was developed using [Gitpod](https://www.gitpod.io/), stored on [Github](https://github.com/) and deployed with [Heroku](https://dashboard.heroku.com/apps).

- Testing on Gitpod:
    1. In the terminal, type "python3 manage.py runserver" and press enter to begin the application
    2. Click "Open in Browser" on the pop-up
    3. Once finished, use Ctrl + C in the terminal to close the application

- Deploying on Heroku:
    1. From the homescreen, click "New" and select "Create new app"
    2. Choose app name, select region and click "Create"
    3. Go to "Settings" and add PORT : 8000 to the Config Vars (CLOUDINARY_URL : {cloudinary url}, DATABASE_URL: {postgres url}, SECRET_KEY: {django secure key} also added but excluded from Github for security reasons)
    4. Add heroku/python buildpack
    5. Go to "Deploy" and connect Github repository
    6. Select "Enable Automatic Deploys" and click "Deploy Branch"

---
## Credits

### Content
- Websites used for initial research:
  - [Facebook](https://www.facebook.com/) for social features
  - [Jamie Oliver](https://www.jamieoliver.com/) for design inspiration
  - [BBC GoodFood](https://www.bbcgoodfood.com/) for recipe presentation
- Code for ordering by count of ManyToMany field (used when browsing by popularity) from [https://stackoverflow.com/questions/28254142/django-order-by-count-of-many-to-many-object](https://stackoverflow.com/questions/28254142/django-order-by-count-of-many-to-many-object)
- Retrieving search term from search bar to display matches from [https://www.youtube.com/watch?v=AGtae4L5BbI](https://www.youtube.com/watch?v=AGtae4L5BbI)
- Custom error pages from tutorial at [https://www.geeksforgeeks.org/django-creating-a-404-error-page/](https://www.geeksforgeeks.org/django-creating-a-404-error-page/)
- Signals tutorial and code to connect Profile database to User inspired by [https://www.youtube.com/watch?v=Kc1Q_ayAeQk](https://www.youtube.com/watch?v=Kc1Q_ayAeQk)
- Recipe card banner to show private/public recipes provided by [https://codepen.io/alexerlandsson/pen/NqXWwX](https://codepen.io/alexerlandsson/pen/NqXWwX)
- Idea for TAGS list -> tuple for better code consistency and less error-prone tags provided by Reuben Ferrante (CI Mentor)
- Saving new slug when updating a recipe at [https://stackoverflow.com/questions/33176569/slugfield-in-django-and-overriding-save](https://stackoverflow.com/questions/33176569/slugfield-in-django-and-overriding-save)
- Lking posts as well as counting likes and saves inspired by [Code Institute](https://codeinstitute.net/) 'I Think Therefore I Blog' walkthrough project.
- Code for multiple forms in one template from [https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page](https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page)
- Formatting textarea widget from [https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models](https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models)
- How to return to same page from [https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request](https://stackoverflow.com/questions/50006147/how-to-return-redirect-to-previous-page-in-django-after-post-request)
- Idea for holding temporary data and cleaning before saving from [https://www.geeksforgeeks.org/multiplechoicefield-django-forms/](https://www.geeksforgeeks.org/multiplechoicefield-django-forms/)
- Prepopulating form after failed attempt from [https://www.reddit.com/r/django/comments/4oie1d/how_to_automatically_prepopulate_data_in_forms/](https://www.reddit.com/r/django/comments/4oie1d/how_to_automatically_prepopulate_data_in_forms/) and [https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values](https://docs.djangoproject.com/en/dev/ref/forms/api/#dynamic-initial-values)
- Fixing mime-type bug in settings file from [https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django](https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django)


### Media
- All icons from [Font Awesome](https://fontawesome.com/)
- All uploaded images from [Pexels](https://www.pexels.com/)

### Acknowledgements
- [Code Institute](https://codeinstitute.net/) for providing excellent learning content
- Reuben Ferrante as my mentor and providing vital feedback throughout the project's development
- [W3Schools](https://www.w3schools.com/) for quick and easy tutorials on programming languages
- [Geeks For Geeks](https://www.geeksforgeeks.org/) for quick and easy tutorials on programming languages
- The users of [Stack Overflow](https://stackoverflow.com/) for asking and answering some of the harder Django questions
- Other CI students for sharing their work and providing inspiration and guidance through the Slack channels

---

Becky Skelcher 2022