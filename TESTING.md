# Table of Contents

- [User Story Testing](#user-story-testing)
  - [Manage Recipes](#manage-recipes)
  - [Approve comments](#Approve-comments)
  - [Create drafts](#Create-drafts)
  - [View likes](#View-likes)
  - [View comments](#View-comments)
  - [Leave a comment](#Leave-a-comment)
  - [View list of recipes](#View-list-of-recipes)
  - [Open a recipe](#Open-a-recipe)
  - [Account registration](#Account-registration)
  - [Comment, like and save a recipe](#Comment,-like-and-save-a-recipe)
  - [Website navigation](#Website-navigation)
- [Validator Testing](#validator-testing)
  - [HTML](#html)
    - [Note 1](#note-1)
  - [CSS](#css)
  - [Javascript](#javascript)
  - [Python](#python)
  - [Lighthouse](#lighthouse)
    - [Desktop](#desktop)
    - [Mobile](#mobile)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
  - [Fixed Bugs](#fixed-bugs)
    - [Footer not staying at the bottom of the page](#Footer-not-staying-at-the-bottom-of-the-page)
    - [Number of comments not correct in the recipe detail page](#Number-of-comments-not-correct-in-the-recipe-detail-page)
    - [Error 404 when creating a recipe](#Error-404-when-creating-a-recipe)
    - [Error 500 when deleting a recipe](#Error-500-when-deleting-a-recipe)
    - [Error 500 when a new user Signs up and try to enter in the Profile page](#Error-500-when-a-new-user-Signs-up-and-try-to-enter-in-the-Profile-page)
  - [Unfixed bugs:](#unfixed-bugs)

## User Story Testing

### Manage Recipes

_As a Site User/Site Admin I can create, read, update and delete recipes so that I can manage the content of my recipes._

- A link to create a new recipe is present in the user profile page.

- [My Profile](docs/testing_images/us_manage_recipes_0.png)
- [Create a Recipe](docs/testing_images/us_manage_recipes_1.png)

- Icons are present in the recipe details to allow the author of the recipe to edit and delete the recipe.

- [Read a Recipe](docs/testing_images/us_manage_recipes_2.png)
- [Update a Recipe](docs/testing_images/us_manage_recipes_3.png)
- [Delete a Recipe](docs/testing_images/us_manage_recipes_4.png)

### Approve comments

_As a Site Admin I can create approve or disapprove a comment so that I can filter out objectionable comments._

- [Approve comments](docs/testing_images/us_approve_comments_1.png)

### Create drafts

_As a Site User/Site Admin I can create draft recipes so that I can finish writing the content later._

- At the end of the "create a recipe" page, Draft is the default status.

- [Create a Draft](docs/testing_images/us_create_draft_1.png)

- If Submit is clicked, the recipe will be saved as draft and a red label "(Draft)" will follow the title of the recipe.

- ["(Draft)" red label](docs/testing_images/us_create_draft_2.png)

- The recipe will be accessible to view, read, edited and delete in the "Personal Recipes".

- [Draft accessible in the "Personal Recipes" page](docs/testing_images/us_create_drafts_3.png)

### View likes

_As a Site User/Site Admin I can view the number of likes on each recipe so that I can see which one is the most popular._

- Views can be seen in the recipe's card and in the recipe details page (under the "Website" link).

- [View number of likes in the recipe's card](docs/testing_images/us_view_likes_1.jpeg)
- [View number of likes in the recipe details page](docs/testing_images/us_view_likes_2.png)

### View comments

_As a Site User/Site Admin I can view the comments on each recipe so that I can read the conversation._

- Comments can be seen in the recipe's card (just the number of comments) and at the end of the recipe details page.

- [View number of comments in the recipe's card](docs/testing_images/us_view_comments_1.png)
- [View number of comments in the recipe details page](docs/testing_images/us_view_comments_2.png)

### Leave a comment

_As a Site User/Site Admin I can leave a comment on a recipe so that I can be involved in the conversation._

- Comments can be left just by a registered user. He/she can leave a comment in the comments section at the end of the recipe details page.

- [Leave a comment](docs/testing_images/us_leave_a_comment_1.png)

### View list of recipes

_As a Site User I can navigate on all pages of the website so that I can see a list of all recipes._

- Recipes can be seen in the "All Recipes" page. They are shown as cards with a picture, a small description, number of likes and number of comments.

- [View list of recipes](docs/testing_images/us_view_list_of_recipes_1.png)

### Open a recipe

_As a Site User I can click on a recipe so that I can read the ingredients and method._

- To see and read the details of a recipe the user needs just to click the tile of the recipe.

### Account registration

_As a Site User I can register an account so that I can log in and logout._

- In all pages is given to the user the opportunity to Sign up, Sign in and Sign out if he/she is already signed in.

- [Sign Up / Sign In](docs/testing_images/us_account_reg_1.png)
- [Sign Up page](docs/testing_images/us_account_reg_2.png)
- [Sign In page](docs/testing_images/us_account_reg_3.png)
- [Sign Out](docs/testing_images/us_account_reg_4.png)

### Comment, like and save a recipe

_As a Site User I can log in so that I can comment, like and save a recipe._

- Comment, like and save a recipe is allowed to registered users in the recipe details page by writing in the "Comments" section at the end of the page (comment), by clicking the "heart" icon and the "bookmark" icon. If a recipe is saved will be shown in the user "Favourite recipes" page.

- [Like a recipe](docs/testing_images/us_comment_like_save_1.png)
- [Like and save a recipe](docs/testing_images/us_comment_like_save_2.png)
- [Saved recipe in the "Favourite Recipes" page](docs/testing_images/us_comment_like_save_3.png)

### Website navigation

_As a Site User/Site admin I can view the content of the website so that I can navigate through the website._

- User can navigate through the pages using the links in the navigation bar. Links that allow the user to browse through all recipes, main courses, dessert and other recipes.

## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page                  | Logged out | Logged in |
| --------------------- | ---------- | --------- |
| base.html             | No errors  | No errors |
| index.html            | No errors  | No errors |
| starters.html         | No errors  | No errors |
| maincourses.html      | No errors  | No errors |
| desserts.html         | No errors  | No errors |
| other.html            | No errors  | No errors |
| delete_recipe.html    | N/A        | No errors |
| edit_recipe.html      | N/A        | No errors |
| favourites.html       | N/A        | Note 1    |
| personal_recipes.html | N/A        | Note 1    |
| recipe_details.html   | No errors  | No errors |
| recipe_form.html      | N/A        | No errors |
| login.html            | No errors  | N/A       |
| logout.html           | N/A        | No errors |
| password_change.html  | N/A        | No errors |
| signup.html           | No errors  | N/A       |
| user_profile.html     | N/A        | No errors |

#### Note 1

When validating the Favourites and Personal recipes pages I recived an error stating "HTTP resource not retrievable. The HTTP status from the remote server was: 500. Document checking not completed. The result cannot be determined due to a non-document-error". After searching for a solution on line I tried to run refresh the page, to do the check later, to delete the browser cookies but the error is still present.

- [Personal recipes check](docs/testing_images/error_personal_recipes.png)
- [Favourite recipes check](docs/testing_images/error_favourite_recipes.png)

### CSS

No errors were found when checking the CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

- [CSS Validation](docs/testing_images/check_css.png)

### Javascript

No errors were found when passing my javascript through [Jshint](https://jshint.com/)

- [JavaScript Validation](docs/testing_images/js_check.png)

### Python

All Python files were run through [Pep8](http://pep8online.com/) with no errors found.

### Lighthouse

All site pages where validated using the Lighthouse validation for both desktop and mobile in order to check accessibility and performance.

#### Desktop

| Page                  | Performance | Accessibility | Best Practice | SEO |
| --------------------- | ----------- | ------------- | ------------- | --- |
| index.html            | 92          | 96            | 92            | 90  |
| starters.html         | 91          | 96            | 92            | 90  |
| maincourses.html      | 91          | 96            | 92            | 90  |
| desserts.html         | 92          | 96            | 92            | 90  |
| other.html            | 92          | 96            | 92            | 90  |
| delete_recipe.html    | 92          | 96            | 92            | 90  |
| edit_recipe.html      | 83          | 96            | 92            | 90  |
| favourites.html       | 92          | 96            | 92            | 90  |
| personal_recipes.html | 92          | 93            | 92            | 90  |
| recipe_details.html   | 80          | 96            | 92            | 90  |
| recipe_form.html      | 82          | 96            | 92            | 90  |
| login.html            | 91          | 97            | 92            | 90  |
| logout.html           | 93          | 98            | 92            | 90  |
| password_change.html  | 93          | 98            | 99            | 90  |
| signup.html           | 89          | 97            | 92            | 90  |
| user_profile.html     | 92          | 97            | 92            | 90  |

#### Mobile

| Page                  | Performance | Accessibility | Best Practice | SEO |
| --------------------- | ----------- | ------------- | ------------- | --- |
| index.html            | 87          | 96            | 92            | 90  |
| starters.html         | 86          | 96            | 92            | 90  |
| maincourses.html      | 87          | 96            | 92            | 90  |
| desserts.html         | 85          | 96            | 92            | 90  |
| other.html            | 85          | 93            | 92            | 90  |
| delete_recipe.html    | 85          | 96            | 92            | 90  |
| edit_recipe.html      | 79          | 93            | 85            | 92  |
| favourites.html       | 80          | 92            | 85            | 92  |
| personal_recipes.html | 83          | 93            | 85            | 92  |
| recipe_details.html   | 78          | 92            | 83            | 92  |
| recipe_form.html      | 75          | 95            | 83            | 92  |
| login.html            | 84          | 97            | 83            | 92  |
| logout.html           | 82          | 97            | 83            | 92  |
| password_change.html  | 80          | 98            | 92            | 92  |
| signup.html           | 81          | 97            | 83            | 92  |
| user_profile.html     | 80          | 97            | 83            | 90  |

## Browser Testing

- The Website was tested on Google Chrome, Firefox, Safari browsers with no issues encountered.

## Device Testing

- The website was browsed mainly on devices such as Desktop, Laptop and iPhone 12 to ensure responsiveness on various screen sizes. The website performed well as intended. The responsive design was checked using Chrome developer tools on different devices with no issues encountered.

## Manual Testing

Manual testing were performed for both desktop and mobile. Because of time restraints, the below table is shown just some of the tests carried out and the results.

| Element               | Action     | Expected Result                                                                                                                             | Pass/Fail |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Logo area             | Click      | Redirect to home                                                                                                                            | Pass      |
| All Recipes Link      | Click      | Open All Recipes page                                                                                                                       | Pass      |
| Starters Link         | Click      | Open Starters page                                                                                                                          | Pass      |
| Main Courses Link     | Click      | Open Main Courses page                                                                                                                      | Pass      |
| Desserts Link         | Click      | Open Desserts page                                                                                                                          | Pass      |
| Other Link            | Click      | Open Other page                                                                                                                             | Pass      |
| Title of a recipe     | Click      | Open the details of that particular recipe                                                                                                  | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                                                                                           | Pass      |
| Sign Up Link          | Display    | Not visible if the user is logged in                                                                                                        | Pass      |
| Log In Link           | Click      | Open Login page                                                                                                                             | Pass      |
| Log In Link           | Display    | Not visible if the user is logged in                                                                                                        | Pass      |
| user Dropdown         | Display    | Present just when the user is logged in                                                                                                     | Pass      |
| user Dropdown         | Click      | Open user dropdown                                                                                                                          | Pass      |
| My Profile Link       | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| My Profile Link       | Click      | Open My Profile page                                                                                                                        | Pass      |
| Change Password Link  | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| Change Password Link  | Click      | Open Change Password page                                                                                                                   | Pass      |
| New Recipe Link       | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| New Recipe Link       | Click      | Open Add a Recipe page                                                                                                                      | Pass      |
| Likes icon            | Click      | If user is not logged in none happens                                                                                                       | Pass      |
| Likes icon            | Click      | Clicking the likes icon it changes to solid red                                                                                             | Pass      |
| Bookmark icon         | Click      | If user is not logged in none happens                                                                                                       | Pass      |
| Bookmark icon         | Click      | Clicking the bookmark icon it changes to solid grey                                                                                         | Pass      |
| Edit Recipe icon      | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| Edit Recipe icon      | Click      | Open Edit a Recipe page                                                                                                                     | Pass      |
| Delete Recipe icon    | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| Delete Recipe icon    | Click      | Open a page where the user needs to confirm deletion                                                                                        | Pass      |
| Personal Recipes Link | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| Personal Recipes Link | Click      | Open Personal Recipes page                                                                                                                  | Pass      |
| Favourites Link       | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| Favourites Link       | Click      | Open Favourite Recipes page                                                                                                                 | Pass      |
| Sign Out Link         | Display    | Only visible if the user is logged in                                                                                                       | Pass      |
| Sign Out Link         | Click      | Open Sign Out confirm page                                                                                                                  | Pass      |
| Hamburger Menu        | Responsive | Display when screen size reduces to large size                                                                                              | Pass      |
| Link in footer        | Click      | Open in new tab and to correct website                                                                                                      | Pass      |
| Recipe Details        | Display    | Display correct recipe title, image, author, website, likes, bookmarks and comments icons, ingredients, Recipe details, method and comments | Pass      |
| Likes icon            | Click      | If user is not logged in none happens                                                                                                       | Pass      |
| Likes icon            | Click      | Clicking the likes icon it changes to solid red                                                                                             | Pass      |
| Bookmark icon         | Click      | If user is not logged in none happens                                                                                                       | Pass      |
| Bookmark icon         | Click      | Clicking the bookmark icon it changes to solid grey                                                                                         | Pass      |
| User Comments         | Display    | Displays correct name date time and comment                                                                                                 | Pass      |
| User Comments         | Display    | Comments are ordered oldest to newest                                                                                                       | Pass      |

## Bugs

### Fixed bugs

#### Footer not staying at the bottom of the page

- **Fix** I set “main” bottom margin and I created a new class “main-min-height” and set the min height.

#### Number of comments not correct in the recipe detail page

- **Bug** The number of comments was not correct in the recipe detail page showing the sum of all comments (included the not approved once)
- **Fix** I Added to models.py “approved_comments”.

#### Error 404 when creating a recipe

- **Fix** I changed the queryset of from filter status=1 to get all.

#### Error 500 when deleting a recipe

- **Fix** I added "success_url" in the "RecipeDeleteView".

#### Error 500 when a new user Signs up and try to enter in the Profile page

- **Fix** Solution obtained following the video at this [link](https://www.youtube.com/watch?v=Kc1Q_ayAeQk).

#### Error 500 when a user Signs up or Signs in

- **Fix** I made sure that each item in the list of the "AUTH_PASSWORD_VALIDATORS" in settings.py was in a single line.

### Unfixed bugs

Currently there are no known unfixed bugs.
