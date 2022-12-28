# Website Testing

## HTML and CSS Validation Testing

- All pages were passed through either the [W3C CSS validator](), [W3C HTML Validator](), [JSHint JavaScript Linter]() or [pep8online Python Linter]() (depending on relevance).
- Any issues found have been rectified and all pages now pass with no errors to show. Any warnings received explained below.

###  W3C HTML Validator

#### Homepage (https://pp4-recipebook.herokuapp.com/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2F)

#### Browsing pages
##### New (full) ()
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fbrowse%2Fnew)
##### Gluten Free (empty) ()
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fbrowse%2Fgluten-free)

#### Search Results ()
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fsearch%2F)

#### Search Results ()
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fsearch%2F)

#### Login ()
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Faccounts%2Flogin%2F)

#### Logout ()
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Faccounts%2Flogout%2F)

#### Register ()
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Faccounts%2Fsignup%2F)

#### Edit Profile (https://pp4-recipebook.herokuapp.com/profiles/edit_profile/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fprofiles%2Fedit_profile%2F)
- 1 Info instance: *Trailing slash on void elements has no effect and interacts badly with unquoted attribute values*. Line created with model form/crispy forms so unable to edit.

#### Profile (https://pp4-recipebook.herokuapp.com/profiles/recipebook/profile/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fprofiles%2Frecipebook%2Fprofile%2F)

#### Add Recipe (https://pp4-recipebook.herokuapp.com/recipes/add_recipe/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Frecipes%2Fadd_recipe%2F)
- 1 Info instance: *Trailing slash on void elements has no effect and interacts badly with unquoted attribute values*. Line created with model form/crispy forms so unable to edit.

#### Edit Recipe (https://pp4-recipebook.herokuapp.com/recipes/fried-rice/edit)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Frecipes%2Ffried-rice%2Fedit)
- 1 Info instance: *Trailing slash on void elements has no effect and interacts badly with unquoted attribute values*. Line created with model form/crispy forms so unable to edit.

#### Recipe Detail (https://pp4-recipebook.herokuapp.com/recipes/fried-rice/)
[Document checking completed. No errors or warnings to show.]()

#### 404 Error ()
[Document checking completed. No errors or warnings to show.]()

#### 500 Error ()
[Document checking completed. No errors or warnings to show.]()











#### card.html
![Feedback from run through the W3 HTML validator for card.html](/assets/images/card-w3c-result.png)

#### carousel.html
![Feedback from run through the W3 HTML validator for carousel.html](/assets/images/carousel-w3c-result.png)

#### scroller.html
![Feedback from run through the W3 HTML validator for scroller.html](/assets/images/scroller-w3c-result.png)

#### search_results.html
![Feedback from run through the W3 HTML validator for search_results.html](/assets/images/search-w3c-result.png)

#### profile.html
![Feedback from run through the W3 HTML validator for profile.html](/assets/images/profile-w3c-result.png)

#### edit_profile.html
![Feedback from run through the W3 HTML validator for edit_profile.html](/assets/images/edit_profile-w3c-result.png)

#### recipe_detail.html
![Feedback from run through the W3 HTML validator for recipe_detail.html](/assets/images/recipe-w3c-result.png)

#### add_recipe.html
![Feedback from run through the W3 HTML validator for add_recipe.html](/assets/images/add_recipe-w3c-result.png)

#### edit_recipe.html
![Feedback from run through the W3 HTML validator for edit_recipe.html](/assets/images/edit_recipe-w3c-result.png)

#### 404.html
![Feedback from run through the W3 HTML validator for 404.html](/assets/images/404-w3c-result.png)

#### 500.html
![Feedback from run through the W3 HTML validator for 500.html](/assets/images/500-w3c-result.png)






###  W3C CSS Validator

#### style.css
![Feedback from run through the W3 CSS validator for style.css](/assets/images/css-w3c-result.png)







###  JSHint Validator
- Some warnings displayed due to splitting of JavaScript betweeen multiple files. When code combined and ran together, these warnings disappear.
- All other warnings determined to be unavoidable and do not affect running of code ("Functions declared within loops referencing an outer scoped variable may lead to confusing semantics").

#### script.js
![Feedback from run through the JSHint linter for script.js](/assets/images/jshint-result.png)






---
## Lighthouse
- All pages were ran through Lighthouse on Chrome Devtools for both desktop and mobile device display. Ran in incognito mode. Any issues were dealt with and all now have a high passing mark.

#### index.html
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)

#### browse.html
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)

#### search_results.html
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)

#### edit_profile.html
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)

#### profile.html
##### Own profile
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)
##### Other's profile
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)

#### add_recipe.html
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)

#### edit_recipe.html
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)

#### recipe_detail.html
- Desktop

![Screenshot of Lighthouse score for standard display of index.html on desktop](/assets/images/index-desktop.png)

- Mobile

![Screenshot of Lighthouse score for standard display of index.html on mobile](/assets/images/index-mobile.png)







---
## Automatic testing

### index.html
- All navigation buttons tested manually **8/7/22** and found to be working as intended
- All game buttons tested manually **8/7/22** and found to be working as intended
- All game levels tested manually on **8/7/22** and found to be working as intended
- All upgrade unlocks tested manually on **8/7/22** and found to be working as intended
- All uprgade toggles tested manually on **8/7/22** and found to be working as intended

### 404.html
- All navigation buttons tested manually **10/7/22** and found to be working as intended

---
## Manual testing

### index.html
- All navigation buttons tested manually **8/7/22** and found to be working as intended
- All game buttons tested manually **8/7/22** and found to be working as intended
- All game levels tested manually on **8/7/22** and found to be working as intended
- All upgrade unlocks tested manually on **8/7/22** and found to be working as intended
- All uprgade toggles tested manually on **8/7/22** and found to be working as intended

### 404.html
- All navigation buttons tested manually **10/7/22** and found to be working as intended

---
## Different browsers
- Tested and found to be working as intended on the following browsers:
    - Chrome
    - Firefox
    - Microsoft Edge
- Unable to test on Safari as unble to download on my Windows PC
- Certain features are not supported on Internet Explorer and therefore some feature are not displaying properly. However, Internet Explorer was retired by Microsoft in August 2021 and is no longer supported.

---
## Different devices with Chrome Devtools
- Tested on the following devices via Chrome Devtools and found to be working as intended:
    - iPhone SE
    - iPhone XR
    - iPhone 12 Pro
    - Pixel 5
    - Samsung Galaxy S8+
    - Samsung Galaxy S20 Ultra
    - iPad Air
    - iPad Mini
    - Surface Pro 7
    - Surface Duo 
    - Samsung Galaxy A51/71
    - Nest Hub
    - Nest Hub Max

---
## Media Queries
- Media queries were provided by vootstrap and introduced at the below break points:
    - xs 0px
    - s 576px
    - m 768px
    - l 992px
    - xl 1200px
    - xxl 1400px

---
## Bugs
### Resolved Bugs
- Issue where screen would inch to left slightly when displayed message at bottom of screen, solved with help from by adding `overflow: hidden;` to budy during function and removing once element removed.
- Issue with dividing width of score bar and multiplying by points to increment progress bar not calling a level-up solved by reducing precision of condition.
- Issue with level 5 progress bar extending past the container solved by applying `overflow: hidden;` to container.
- Originally tried to call multiple messages to display but this caused a bug as it meant multiples of the same ID. Fixed by removing old message once finished with.
- Error was displayed in console when displaying the rules message type. This did not affect the message being displayed. Solved by altering function to display message by removing code to populate butttons if rules message called.
- Bug where upgraded backgrouns colour was not taking up whole screen when applied solved by adding JavaScript to add in-line style to overide any other styles.
- Issue with trying to display the chosen weapon icon by using code to map the index in an array solved with code from [Borislav Hadzhiev](https://bobbyhadz.com/blog/javascript-array-find-index-of-object-by-property)
- Issue where player is able to display multiple level-up messages by raidly clicking game buttons, thus causing mutliple elements of the same ID and causing the the game to break. Solved by calling the disableBackground function immediately after level-up is established, before the message is displayed.

### Unresolved Bugs
- Scrolling on mobile device very briefly displays white background at the bottom of the page - have tried a few combinations of background properties but none have fixed this. It is only brief and does not affext user experience.

