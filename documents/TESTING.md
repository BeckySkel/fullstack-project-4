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
- Click [here](dcuments/desktop-lighthouse-testing.pdf) to see Lighthouse scores on desktop

### Mobile
- Click [here](documents/mobile-lighthouse-testing.pdf) to see Lighthouse scores on mobile

---
## Manual testing

### Homepage (https://pp4-recipebook.herokuapp.com/)
- All internal links tested manually on **29/12/22** and found to be working as intended
- All external links (social media links) tested manually on **29/12/22** and found to be working as intended
- All dynamic content tested manually on **29/12/22** and found to be working as intended
- All login-state sensitive content and links tested manually on **29/12/22** and found to be working as intended

### Browsing pages
- - All dynamic content tested manually on **29/12/22** and found to be working as intended
#### New (full) (https://pp4-recipebook.herokuapp.com/browse/new)
- All internal links tested manually on **29/12/22** and found to be working as intended
- All forms (search) tested manually on **29/12/22** and found to be working as intended
#### Gluten Free (empty) (https://pp4-recipebook.herokuapp.com/browse/gluten-free)
- All internal links tested manually on **29/12/22** and found to be working as intended
- All forms (search) tested manually on **29/12/22** and found to be working as intended
- All login-state sensitive content and links tested manually on **29/12/22** and found to be working as intended

#### Search Results (https://pp4-recipebook.herokuapp.com/search/)
- All internal links tested manually on **29/12/22** and found to be working as intended
- All dynamic content tested manually on **29/12/22** and found to be working as intended
- All login-state sensitive content and links tested manually on **29/12/22** and found to be working as intended

#### Login (https://pp4-recipebook.herokuapp.com/accounts/login/)
- All internal links tested manually on **29/12/22** and found to be working as intended
- Form tested manually on **29/12/22** and found to be working as intended

#### Logout (https://pp4-recipebook.herokuapp.com/accounts/logout/)
- All internal links tested manually on **29/12/22** and found to be working as intended

#### Register (https://pp4-recipebook.herokuapp.com/accounts/signup/)
- All internal links tested manually on **29/12/22** and found to be working as intended
- Form tested manually on **29/12/22** and found to be working as intended

#### Edit Profile (https://pp4-recipebook.herokuapp.com/profiles/edit_profile/)
- Form tested manually on **29/12/22** and found to be working as intended
- All dynamic content tested manually on **29/12/22** and found to be working as intended

#### Profile (https://pp4-recipebook.herokuapp.com/profiles/recipebook/profile/)
- All internal links tested manually on **29/12/22** and found to be working as intended
- All dynamic content tested manually on **29/12/22** and found to be working as intended
- Javascript to update DOM tested manually on **29/12/22** and found to be working as intended

#### Add Recipe (https://pp4-recipebook.herokuapp.com/recipes/add_recipe/)
- Form tested manually on **29/12/22** and found to be working as intended

#### Edit Recipe (https://pp4-recipebook.herokuapp.com/recipes/fried-rice/edit)
- Form tested manually on **29/12/22** and found to be working as intended
- All login-state sensitive content and links tested manually on **29/12/22** and found to be working as intended

#### Recipe Detail (https://pp4-recipebook.herokuapp.com/recipes/fried-rice/)
- All internal links tested manually on **29/12/22** and found to be working as intended
- All dynamic content tested manually on **29/12/22** and found to be working as intended
- All forms (like, save, comment, notes) tested manually on **29/12/22** and found to be working as intended
- All login-state sensitive content and links tested manually on **29/12/22** and found to be working as intended

#### 404 Error (https://pp4-recipebook.herokuapp.com/recipes/404/)
- All internal links tested manually on **29/12/22** and found to be working as intended
- All dynamic content tested manually on **29/12/22** and found to be working as intended

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
- Carousels on home page would not scroll when clicking button resolved by making sure IDs were unique.
- Bug where hosting 2 forms on same page meant that both were posted resolved with help from [https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page](https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page)
- I tried adding supporting pdf documents to the static file but this caused a bug so I removed them and hosted them in a documents folder.

### Unresolved Bugs
- Search page recieving poor Performance score on Ligthhouse despite my attempts to follow the advice about render blocking, etc. In the end the styling of the page suffered with all the changes so I reverted back to normal links but would like to try to resolve this issue in the future.

