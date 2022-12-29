# Website Testing

## HTML and CSS Validation Testing

- All pages were passed through either the [W3C CSS validator](https://jigsaw.w3.org/css-validator/), [W3C HTML Validator](https://validator.w3.org/nu/), [JSHint JavaScript Linter](https://jshint.com/) or Github's local pycodestyle PROBLEMS tab (depending on relevance).
- Any issues found have been rectified and all pages now pass with no errors to show. Any warnings received explained below.


###  W3C HTML Validator (Validate by URI)

#### Homepage (https://pp4-recipebook.herokuapp.com/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2F)

#### Browsing pages
##### New (full) (https://pp4-recipebook.herokuapp.com/browse/new)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fbrowse%2Fnew)
##### Gluten Free (empty) (https://pp4-recipebook.herokuapp.com/browse/gluten-free)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fbrowse%2Fgluten-free)

#### Search Results (https://pp4-recipebook.herokuapp.com/search/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Fsearch%2F)

#### Login (https://pp4-recipebook.herokuapp.com/accounts/login/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Faccounts%2Flogin%2F)

#### Logout (https://pp4-recipebook.herokuapp.com/accounts/logout/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Faccounts%2Flogout%2F)

#### Register (https://pp4-recipebook.herokuapp.com/accounts/signup/)
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
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Frecipes%2Ffried-rice%2F)

#### 404 Error (https://pp4-recipebook.herokuapp.com/recipes/404/)
[Document checking completed. No errors or warnings to show.](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-recipebook.herokuapp.com%2Frecipes%2F404%2F)


###  W3C CSS Validator (Validate by direct input)

#### style.css
- Google Fonts import at top removed for validation
![Feedback from run through the W3 CSS validator for style.css](/static/images/css-w3c-result.png)


###  JSHint Validator
- /*jshint esversion: 6 */ applied to disable following irrelevant warnings: 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).

#### Script in profile.html
![Feedback from run through the JSHint linter for script in profile.html](/static/images/jshint-result.png)


###  Python Linter
- Pep8 website appears to not be working when visited. This was confirmed on Slack by posts from CI.
- All files, instead, checked against Github's local pycodestyle PROBLEMS tab.
- Any issues found have been rectified and all pages now pass with no errors or warnings to show.

---
## Lighthouse
- All pages were ran through Lighthouse on Chrome Devtools for both desktop and mobile device display. Ran in incognito mode. Any issues were dealt with and all now have a high passing mark with any exceptions detailed in linked documents.

### Desktop
- Click [here]() to see Lighthouse scores on desktop

### Mobile
- Click [here]() to see Lighthouse scores on mobile

---
## Automatic testing


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
- Form pages showing scroll-space to the left when on smaller screens fixed by applying `overflow: hidden` to form container.

### Unresolved Bugs
- 

