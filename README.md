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

- View [User Personas](static/documents/personas.pdf)

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
  - [Facebook](https://www.facebook.com/) for social features
  - [Jamie Oliver](https://www.jamieoliver.com/) for design inspiration
  - [BBC GoodFood](https://www.bbcgoodfood.com/) for recipe presentation

### Future Features

#### Audio Feedback
- I'd like to include audio feedback of the result of each battle. Positive sounds for a win and negative sounds for loss. This would aid in communication the outcome of the battle to the player and would be especially useful to visually impaired players in particular. A toggle to turn audio on and off would be included in the settings menu.

#### Image Upgrade
- Another upgrade which could be included would be swapping out the [Font Awesome](https://fontawesome.com/) icons for photos/realistic images or other art-styles such as pixelated/retro.

#### Multiplayer
- I'd like to include online-play so that people from around the world can compete with each other 1 vs 1 matches or in knock-out tournaments. This would keep things interesting for the player and improve the replayability. 
- A local multiplayer option would be another desirable option. Players could use letter keys to select their weapon (e.g. a, s & d for player 1 and j, k & l for player 2).

#### More Levels
- I'd like to add up to 10 levels and more upgrades to choose from so that the player can play for longer and has more choice of customisation.

### Testing
- Throughout the project, I relied heavily on [Chrome Devtools](https://developer.chrome.com/docs/devtools/) to help me view this project on different screen sizes so that I could adjust elements, create media queries for responsive design and debug JavaScript by logging outcomes to the console. 
- Please follow [this link](assets/documents/TESTING.md) for full list of tests carried out on this website

---
## Structure

### Wireframes
- After looking at common designs and features and deciding what I would like to include, I mapped out the intended features of the website using [Balsamiq](https://balsamiq.com/) to create wireframes of each page view.
- [View the wireframes here](assets/documents/wireframes.pdf)
- The key differences between planning and the final product are presentation of the settings menu & game rules. Originally I had planned to display these through an extending footer which would slide up from the bottom when one of the links were clicked and shrunk back down once no longer in use. This developed into a message band that slides from top to bottom instead.

### Information architecture
- Ultimate RPs is a single-page website which relies on JavaScript to manipulate the DOM and display different areas of the site in pop-up messages.
- The useful information is presented in an animated message container that slides in from the top of the screen and slides out through the bottom of the screen once the user has read the displayed information and interacted with the appropriate buttons. 
- The main game area is permanently displayed in the centre of the screen, tucked behind any displayed messages until the user is ready to resume playing. There are only 3 to 5 buttons to interact with but these manipulate various sections of the screen to display the user's choice, computer's choice, the outcome of the game and the amount of wins, losses and draws the user has achieved throughout their session.
- Once a player reaches the next level by incrementing the progress bar to fill the container, a message is displayed via the sliding message container letting the player know that they have leveled-up and offers them 3 upgrades to choose from. Once the player has chosen, the message slides out and the upgrade is applied.
- In the top right of the page is 2 buttons which call the settings menu where a player can enable and disable their unlocked upgrades, or the rules on how to play the game. Both icons temporarily disappear when a message is displayed to avoid overlapping messages.

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

#### Other resources
- [Gitpod](https://www.gitpod.io/) to alter and manage website files
- [Github](https://github.com/) to create and store website files
- [Github Pages](https://pages.github.com/) to deploy site
- [Chrome Devtools](https://developer.chrome.com/docs/devtools/) to test site throughout process
- [Balsamiq](https://balsamiq.com/) to create wireframes
- [Coolors](https://coolors.co/) to choose a colour scheme
- [CSS Gradient](https://cssgradient.io/#:~:text=Gradients%20are%20CSS%20elements%20of,be%20in%20a%20background%20element.) to help with CSS gradients for website backgrounds
- [Google Fonts](https://fonts.google.com/) for the website font (Cabin)
- [Font Awesome](https://fontawesome.com/) used to add icons
- [Favicon.io](https://favicon.io/favicon-generator/) used to create favicon
- [Code Institute](https://codeinstitute.net/) fullstack developer course to learn how to create
- [W3Schools](https://www.w3schools.com/) for help with common coding issues
- [Am I Responsive?](https://ui.dev/amiresponsive) for device simulations

---
## Surface

### Design

#### Colour scheme

![The colour scheme I used for the standard display](/assets/images/colour-scheme.png)

- The colour-scheme is vibrant but soft to provide a pleasing display without distracting from the game-play.
- For the upgrades, bolder colours and patterns were chosen to improve player customisation and feeling of reward and excitement.
- I used [Coolors](https://coolors.co/) to help pick a colour scheme and [CSS Gradient](https://cssgradient.io/#:~:text=Gradients%20are%20CSS%20elements%20of,be%20in%20a%20background%20element.) to help with coding the CSS gradients.
- There is a 135 degree angled gradient across all backgrounds ranging from more subtle to very striking.
- For the standard displa, the base colours are pale blue, mint green and a warm off-white with mustard and lime green acting as highlights.


#### Imagery
- There are currently no images used in this site.

#### Typography
- All text is in the Cabin font. It is a humanist sans which is clear and easily read at both larger and smaller font sizes. It’s classic-yet-modern style pairs well with the softer colours and rounded edges of the website.
- Sans serif has been used as the fallback option since it is the closest web-safe font.

#### Icons
- [Font Awesome](https://fontawesome.com/) icons were used for navigation buttons as well as for the main game display.

### Deployment
- This site was deployed on Github Pages, following the below steps:
    1. Acces the Github repository [here](https://github.com/BeckySkel/javascript-project-2)
    2. Navigate to the **Settings** tab (far right tab)
    3. Open the **Pages** information
    4. Select branch **main**
    5. Wait for site to deploy (this make take a few minutes) 
- Access the live site [here](https://beckyskel.github.io/javascript-project-2/)

---
## Credits

### Content
- Websites used for initial research:
     - [](https://www.rpsgame.org/random)
     - [](https://www.online-stopwatch.com/chance-games/rock-paper-scissors/)
     - [](https://www.twoplayergames.org/game/rock-paper-scissors)
- Issue with trying to display the chosen weapon icon by using code to map the index in an array solved with code from [Borislav Hadzhiev](https://bobbyhadz.com/blog/javascript-array-find-index-of-object-by-property)
- CSS Code for colourful 3D heading from [Mandy Michael](code for 3D effect from https://codepen.io/mandymichael/pen/VprZaq)
- Code for preloading and preconnecting links suggested by [Chrome Devtools](https://developer.chrome.com/docs/devtools/) Lighthouse feature
- 3D buttons inspired by [Arron Hunt](https://codepen.io/arronhunt/pen/WWOOeO) but heavily edited by myself to suit my design

### Media
- All icons from [Font Awesome](https://fontawesome.com/)
- All CSS gradients achieved with [CSS Gradient](https://cssgradient.io/#:~:text=Gradients%20are%20CSS%20elements%20of,be%20in%20a%20background%20element.)

### Acknowledgements
- [Code Institute](https://codeinstitute.net/) for providing excellent learning content and project idea
- Reuben Ferrante as my mentor and providing vital feedback throughout the project's development
- [W3Schools](https://www.w3schools.com/) for quick and easy guidance on HTML and CSS
- The users of [Stack Overflow](https://stackoverflow.com/) for asking and answering some of the harder JavaScript questions
- Other CI students for sharing their work and providing inspiration and guidance

---

Becky Skelcher 2022