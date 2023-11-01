# Browser Compatibility

<img height="50" src="README/tests/browser/google_chrome_icon.png"><img height="50" src="README/tests/browser/png-transparent-microsoft-edge-new-icon.png"><img height="50" src="README/tests/browser/safari-icon-hd.png"><img height="50" src="README/tests/browser/firefox-icon.png">

After publishing to Heroku, the site was tested on Google Chrome, Microsoft Edge, Safari and Mozilla Firefox, with no visible issues for the user. 

The site has loaded correctly and had no issues across all browsers.

[Back to top &uarr;](#browser-compatibility)

# __Validation__

## <img height="50" src="README/readme-files/html.png"> __HTML__

All pages were run through the [W3C Markup Validator](https://validator.w3.org/nu/). 

Initially, there were some errors however all errors have been rectified.

<details><summary> >>> Click for Home validation img</summary>

![Home](README/tests/html/main.png)
</details>


<details><summary> >>> Click for Product validation img</summary>

![Product](README/tests/html/product.png)
</details>


<details><summary> >>> Click for Product detaills validation img</summary>

![Product detaills](README/tests/html/product-details.png)
</details>


<details><summary> >>> Click for Add Product validation img</summary>

![Add Product](README/tests/html/product-add.png)
</details>


<details><summary> >>> Click for Edit Product validation img</summary>

![Edit Product](README/tests/html/product-edit.png)
</details>


<details><summary> >>> Click for Profile Update validation img</summary>

![Profile Update]()
</details>


<details><summary> >>> Click for Register Profile validation img</summary>

![Register](README/tests/html/sign-up.png)
</details>


<details><summary> >>> Click for Profile Login validation img</summary>

![Login](README/tests/html/sign-in.png)
</details>


<details><summary> >>> Click for Profile Logout validation img</summary>

![Logout](README/tests/html/logout.png)
</details>


[Back to top &uarr;](#browser-compatibility)

***




## <img height="50" src="README/readme-files/css.png"> __CSS__
[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the site's CSS code.

All issued rectified.

<details><summary> >>> Click for CSS base validation img</summary>

![CSS base validation](README/tests/css/base.png)
</details>


<details><summary> >>> Click for CSS checkout validation img</summary>

![CSS checkout validation](README/tests/css/checkout.png)
</details>


<details><summary> >>> Click for CSS profile validation img</summary>

![CSS profile validation](README/tests/css/profile.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***




## <img height="50" src="README/readme-files/js.png"> __JS__

[JSHint](https://jshint.com/) was used to validate the Javascript code used in the project. 

No issues to report.

<details><summary> >>> Click for JSHint products script validation img</summary>

![JSHint products script](README/tests/js/product-scripts.png)
</details>


<details><summary> >>> Click for JSHint product details script validation img</summary>

![JSHint product details script](README/tests/js/product-details-script.png)
</details>


<details><summary> >>> Click for JSHint edit product script validation img</summary>

![JSHint edit product script](README/tests/js/edit-product-script.png)
</details>


<details><summary> >>> Click for JSHint bag script validation img</summary>

![JSHint bag script](README/tests/js/bag-script.png)
</details>


<details><summary> >>> Click for JSHint quantity input script validation img</summary>

![JSHint quantity input script](README/tests/js/quantity-input-script.png)
</details>


<details><summary> >>> Click for JSHint stripe elements script validation img</summary>

![JSHint stripe elements script](README/tests/js/stripe-elements.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***

## <img height="50" src="README/tests/lighthouse/google-lighthouse-featured-image.png"> __Lighthouse__

Every page of the site was passed through the Lighthouse via the Chrome Dev Tools.

Performance issued are due mainly to image sizing however, some pages have shown also unused js code usage (GSAP code which in only used on index page) 

<details><summary> >>> Click for Home Page Lighthouse Report</summary>
Desktop 

![Lighthouse Desktop](README/tests/lighthouse/main.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/main-mob.png)
![Lighthouse Mobile](README/tests/lighthouse/main-mob-expl.png)
![Lighthouse Mobile](README/tests/lighthouse/main-mob-expl2.png)
</details>


<details><summary> >>> Click for Product Lighthouse Report img</summary>

Desktop 

![Lighthouse Desktop](README/tests/lighthouse/product.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/product-mob.png)
![Lighthouse Mobile](README/tests/lighthouse/product-mob-expl.png)
</details>


<details><summary> >>> Click for Product details Lighthouse Report img</summary>

Desktop 

![Lighthouse Desktop](README/tests/lighthouse/product-details.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/product-details-mob.png)
![Lighthouse Mobile](README/tests/lighthouse/product-details-mob-expl.png)
</details>


<details><summary> >>> Click for Add Product Lighthouse Report img</summary>

Desktop 

![Lighthouse Desktop](README/tests/lighthouse/add-product.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/add-product-mob.png)
</details>


<details><summary> >>> Click for Edit Product Lighthouse Report img</summary>

Desktop 

![Lighthouse Desktop](README/tests/lighthouse/edit-product.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/edit-product-mob.png)
</details>


<details><summary> >>> Click for Profile UpdateLighthouse Report img</summary>

Desktop 

![Lighthouse Desktop](README/tests/lighthouse/profile.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/profile-mob.png)
![Lighthouse Mobile](README/tests/lighthouse/sign-in-mob-expl.png)
</details>


<details><summary> >>> Click for Register Profile Lighthouse Report img</summary>

Desktop 

![Lighthouse Desktop](README/tests/lighthouse/sign-up.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/sign-up-mob.png)

</details>


<details><summary> >>> Click for Profile Login Lighthouse Report img</summary>

Desktop 

![Lighthouse Desktop](README/tests/lighthouse/sign-in.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/sign-in-mob.png)
![Lighthouse Mobile](README/tests/lighthouse/sign-in-mob-expl.png)
</details>


<details><summary> >>> Click for Profile Logout Lighthouse Report img</summary>

Desktop

![Lighthouse Desktop](README/tests/lighthouse/sign-out.png)

Mobile

![Lighthouse Mobile](README/tests/lighthouse/sign-out-mob.png)
![Lighthouse Mobile](README/tests/lighthouse/sign-out-mob-expl.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***


## <img height="50" src="README/tests/python/pep8-images.jpeg"> __PEP8 CI Validation__

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project. The results are outlined in below:

***

app: __gameronboard__

<details><summary> >>> Click for urls.py validation img</summary>

![Alt text](README/tests/python/gameonboard-urls.png)
</details>

***

app: __home__

<details><summary> >>> Click for urls.py validation img</summary>

![Alt text](README/tests/python/home-urls.png)
</details>

<details><summary> >>> Click for views.py validation img</summary>

![Alt text](README/tests/python/home-views.png)
</details>

<details><summary> >>> Click for apps.py validation img</summary>

![Alt text](README/tests/python/home-apps.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***

app: __bag__

<details><summary> >>> Click for urls.py validation img</summary>

![Alt text](README/tests/python/bag-urls.png) 
</details>

<details><summary> >>> Click for views.py validation img</summary>

![Alt text](README/tests/python/bag-views.png)
</details>

<details><summary> >>> Click for apps.py validation img</summary>

![Alt text](README/tests/python/bag-apps.png)
</details>

<details><summary> >>> Click for context.py validation img</summary>

![Alt text](README/tests/python/bag-context.png) 
</details>

<details><summary> >>> Click for bag_tools.py validation img</summary>

![Alt text](README/tests/python/bag-tools.png) 
</details>

[Back to top &uarr;](#browser-compatibility)

***

app: __checkout__

<details><summary> >>> Click for urls.py validation img</summary>

![Alt text](README/tests/python/checkout-URLS.png)
</details>

<details><summary> >>> Click for views.py validation img</summary>

![Alt text](README/tests/python/checkout-views.png)
</details>

<details><summary> >>> Click for forms.py validation img</summary>

![Alt text](README/tests/python/checkout-forms.png)
</details>

<details><summary> >>> Click for models.py validation img</summary>

![Alt text](README/tests/python/checkout-models.png)
</details>

<details><summary> >>> Click for signals.py validation img</summary>

![Alt text](README/tests/python/checkout-signals.png)
</details>

<details><summary> >>> Click for admin.py validation img</summary>

![Alt text](README/tests/python/checkout-admin.png)
</details>

<details><summary> >>> Click for apps.py validation img</summary>

![Alt text](README/tests/python/checkout-apps.png)
</details>

<details><summary> >>> Click for webhook.py validation img</summary>

![Alt text](README/tests/python/webhoocks.png)
</details>

<details><summary> >>> Click for webhook_handler.py validation img</summary>

![Alt text](README/tests/python/webhook-handler.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***

app: __newsletter__

<details><summary> >>> Click for urls.py validation img</summary>

![Alt text](README/tests/python/newsletter-urls.png)
</details>

<details><summary> >>> Click for views.py validation img</summary>

![Alt text](README/tests/python/newsletter-views.png)
</details>

<details><summary> >>> Click for forms.py validation img</summary>

![Alt text](README/tests/python/newsletter-forms.png)
</details>

<details><summary> >>> Click for admin.py validation img</summary>

![Alt text](README/tests/python/newsletter-admin.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***

app: __product__

<details><summary> >>> Click for urls.py validation img</summary>

![Alt text](README/tests/python/product-urls.png)
</details>

<details><summary> >>> Click for views.py validation img</summary>

![Alt text](README/tests/python/product-views.png)
</details>

<details><summary> >>> Click for forms.py validation img</summary>

![Alt text](README/tests/python/product-forms.png)
</details>

<details><summary> >>> Click for models.py validation img</summary>

![Alt text](README/tests/python/product-models.png)
</details>

<details><summary> >>> Click for apps.py validation img</summary>

![Alt text](README/tests/python/product-apps.png)
</details>

<details><summary> >>> Click for widgets.py validation img</summary>

![Alt text](README/tests/python/product-widgets.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***

app: __profile__

<details><summary> >>> Click for urls.py validation img</summary>

![Alt text](README/tests/python/profile-urls.png)
</details>

<details><summary> >>> Click for views.py validation img</summary>

![Alt text](README/tests/python/profile-views.png)
</details>

<details><summary> >>> Click for models.py validation img</summary>

![Alt text](README/tests/python/profile-models.png)
</details>

<details><summary> >>> Click for forms.py validation img</summary>

![Alt text](README/tests/python/profile-forms.png)
</details>

<details><summary> >>> Click for apps.py validation img</summary>

![Alt text](README/tests/python/profile-apps.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***

app: __main folder__

<details><summary> >>> Click for manage.py validation img</summary>

![Alt text](README/tests/python/manage-py.png)
</details>

<details><summary> >>> Click for custom_storages.py validation img</summary>

![Alt text](README/tests/python/custom-storages.png)
</details>

[Back to top &uarr;](#browser-compatibility)

***

# <img height="50" src="README/tests/manual/manual-testing.png"> Manual tests:

## __Welcome Screen__

<details><summary> >>> Click for details</summary>

Some features of the GamerOnGoard webshop, like storing details or browsing order history, are restricted to registered users. 
User is welcomed on landing page where it is invited to browse stock by clicking 'Shop Now' button. 
User is able to create 'Profile' at any stage however, it is possible to make a purchase withough creating one. 
Some functionality like 'Product Managment'is restricted to Superusers only.

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Welcome screen has loaded correctly and as intended | Pass |
| Verified that the user can click sign-up button when not authenticated | Pass |
| Verified that the user can click login button when not authenticated | Pass |
| Verified that the user can logout from user profile dropdown when authenticated | Pass |
| Verified that the user can click browse products by pressing 'Shop Now' button | Pass |
| Verified that the user gets redirected to home page when logo is clicked  | Pass |
| Verified that the user gets redirected to 'Shoppin Bag' when 'Bag' icon is clicked  | Pass |
| Verified that the user can search product (search inludes product name and description) | Pass |
| Verified that the 'Keep Shopping' link on empty 'Bag' page works as intended  | Pass |
| Verified that the user can use a drop down links | Pass |
| Verified that the user can click links in navbar and each link opens as intended | Pass |
| Verified that the user can choose user add product from 'My Account' dropdown when authenticated | Pass |
| Verified that the user can choose user profile from 'My Account' dropdown when authenticated | Pass |
| Verified that the nav search menu works as intended and takes user to particular search | Pass |
| Verified that the nav filtering menu works as intended and takes user to particular filter  | Pass |
| Verified that the footer social links work as intended  | Pass |
| Verified that the user can click each social link and all open on a new page | Pass |
| Verified that the footer category links work as intended  | Pass |
| Verified that the footer subscription function work as intended  | Pass |
| Varified that the user is being updated by quick messages as intended | Pass |
</details>


## __Sign Up__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Sign Up screen has loaded correctly and as intended | Pass |
| Varified that the User is edirected to sign up page when 'Register' is clicked in "My Account' nav menu | Pass |
| Varified that the User must type in correct characters in username, email and passwrods fields | Pass |
| Varified that the when all required info is provided, User account is created after pressing sign up button | Pass |
| Varified that a confirmation email is sent to user requesting to confirm email address  | Pass |
| Varified that after account is created and email confirmed, User can login menu shows only create profile link | Pass |
| Varified that after account is created and email confirmed, User can update his details | Pass |
| Varified that the user is being updated by quick messages as intended | Pass |
</details>

## __Login__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Login screen has loaded correctly and as intended | Pass |
| Varified that the User must type in username and passwrod to login | Pass |
| Varified that after login User is redirected to main screen | Pass |
| Varified that after login User is presented with correct nav links | Pass |
| Varified that after login User given all user rights | Pass |
| Varified that after login Superuser is redirected to main screen | Pass |
| Varified that after login Superuser is presented with correct nav links | Pass |
| Varified that after login Superuser given all superuser rights | Pass |
| Verified that when User clicks 'Forgot Password' it's being redirected to password reset page | Pass |
| Varified that the user is being updated by quick messages as intended | Pass |
</details>

## __Search__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Search product screen has loaded correctly and as intended | Pass |
| Varified that the User is allowed to search product db when authenticated or not | Pass |
| Varified that the User is presented with search result page regardles of whether capital or lowercase characters are typed in | Pass |
| Varified that the User is redirected to search results screen once clicked 'Search' | Pass |
| Verified that the user can open products loaded from search results | Pass |
| Verified that the user can go back to products page when clicking 'Home' | Pass |
| Varified that the user is being updated by quick messages as intended | Pass |
</details>

## __Products Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Products screen has loaded correctly and as intended | Pass |
| Verified that the user can open Products loaded when authenticated or not  | Pass |
| Verified that the user can sort by category by clicking category name | Pass |
| Verified that pagination is working as intended | Pass |
| Verified that 'All Products' link in navbar redirects to 'All Products' page | Pass |
| Verified that 'All Products' by Price after clicking are being shown sorted as intended  | Pass |
| Verified that 'All Products' by Age after clicking are being shown sorted as intended  | Pass |
| Verified that 'All Products' by Rating after clicking are being shown sorted as intended  | Pass |
| Verified that 'All Products' by Category after clicking are being shown sorted as intended  | Pass |
| Verified that 'Board Games' link in navbar redirects user to chosen 'Category' as intended  | Pass |
| Verified that 'Classic Games' link in navbar redirects user to chosen 'Category' as intended | Pass |
| Verified that 'Game Accessories' link in navbar redirects user to chosen 'Category' as intended  | Pass |
| Verified that 'Special Offers' link in navbar redirects user to chosen 'Category' as intended   | Pass |
| Verified that 'Products Home' link on top-left of the page redirects user to chosen 'home' page as intended   | Pass |
| Verified that Products count on top-left of the page counts products correctly and as intended   | Pass |
| Verified that product cards are displayed correctly with all links working  | Pass |
| Verified that product images are displayed correctly with all links working  | Pass |
| Verified that product details are displayed correctly  | Pass |
| Verified that product badges are displayed correctly  | Pass |
| Verified that User can click on Product image to be redirected and view Product details page  | Pass |
| Verified that User can click on Product category to be redirected and shown all Product in this category  | Pass |
| Verified that User can click on 'Add to bag' for the product to be added to the bag  | Pass |
| Verified that User cannot click on 'Add to bag' when product is out of stock  | Pass |
| Verified that 'Add to bag' is replaced by 'Out of stock" when product is out of stock | Pass |
| Verified that when logged in as Superuser, edit and delete links are shown | Pass |
| Verified that when logged in as Superuser and clicked Edit, User is redireced to 'Edit Product' page | Pass |
| Verified that when logged in as Superuser and clicked Delete, confirmation msg comes up to confirm deletion | Pass |
| Varified that the user is being updated by quick messages as intended | Pass |
</details>


## __Product details Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Verified that the breadcrumbs have loaded correctly and links are working as intended  | Pass |
| Verified that the User can scroll carousell pictures | Pass |
| Verified that the User can play a video | Pass |
| Verified that the User can see product name, description, age restrictions, number of players, time of play info  | Pass |
| Verified that product badges are displayed correctly  | Pass |
| Verified that the User can click on Product category to be redirected and shown all Product in this category  | Pass |
| Verified that the User can click + button on quantity selector form | Quantity number increases if number + 1 | Pass |
| Verified that the User can click - button on quantity selector form | Quantity number increases if number - 1 | Pass |
| Verified that the User is shown a message if added more to the bag then what's in stock | Pass |
| Verified that the User is shown a message if added more to the bag then what's in stock| Pass |
| Verified that the User is shown a message if manually enter number greater than product stock in quantity selector form  | Pass |
| Verified that the User 'Add to bag' button works as intended  | Pass |
| Verified that when the User clicks on 'Add to bag' button, product is added to the bag  | Pass |
| Verified that the User 'Keep shipping' link redirects user to Products page and works as intended | Pass |
| Verified that the User is presented with addditional category description for each category | Pass |
| Verified that the User is presented with addditional age restriction (PEGI) description for each age category | Pass |
| Verified that when logged in as Superuser, edit and delete links are shown | Pass |
| Verified that when logged in as Superuser and clicked Edit, User is redireced to 'Edit Product' page | Pass |
| Verified that when logged in as Superuser and clicked Delete, confirmation msg comes up to confirm deletion | Pass |
| Varified that the User is being updated by quick messages as intended | Pass |
</details>



## __(Create) Profile Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| My Profile screen has loaded correctly and as intended | Pass |
| Verified that 'Edit Bio & Social Links' button brings user to edit page | Pass |
| Verified that 'Edit Profile Settings' button brings user to edit page | Pass |
| Verified that 'Back to Your Recipes' button brings user to my recipes page | Pass |
| Verified that 'Back to Blog' button brings user to blog page | Pass |
| Verified that each social media links open correctly | Pass |
</details>


## __Update Profile Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Edit Profile Bio & Social Links screen has loaded correctly and as intended | Pass |
| Verified that the User can update Bio | Pass |
| Verified that the User can update Profile pic | Pass |
| Verified that the User can update All Social Links | Pass |
| Verified that 'Back to Your Profile' button brings user to profile page | Pass |
</details>


## __Change Password Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Change password screen has loaded correctly and as intended | Pass |
| Verified that the User can update their password | Fail |
</details>

## __Add Product Screen__ 

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Add Recipe screen has loaded correctly and as intended | Pass |
| Verified that the User is presented with a form to be completed as intended | Pass |
| Verified that the 'Recipe' Title field is mandatory | Pass |
| Verified that the 'Category' field is mandatory | Pass |
| Verified that the 'Category' field is pulls data from Category model as intended | Pass |
| Verified that the 'Feature Comment' field is mandatory | Pass |
| Verified that the 'Recipe ingridients' & 'Recipe instructions' fields are shown as Summernote fields | Pass |
| Verified that the User can add additionl information in Excerpt field (not mandatory) | Pass |
| Verified that the User can add image which is saved in Cloudinary | Pass |
| Verified that the User is shown page and message on succesfull submittion | Pass |
| Verified that 'Back' button brings user to recipes page | Pass |
</details>


## __Admin__ (Superuser only)

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Superuser can use a quick link from User manu to open Admin Panel | Pass |
</details>

## __Logout__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Varified that the User can logout by clicking Logout in User manu quick link | Pass |
| Varified that the User is shown confirmation page before logout | Pass |
| Varified that the User is logout after confirmation | Pass |
| Varified that the User logout page shows user profile pin and username | Pass |
| Verified that 'Back to Blog' button brings user to blog page | Pass |
| Verified that 'Back to Recipes' button brings user to recipes page | Pass |
</details>

[Back to top &uarr;](#browser-compatibility)

***

# Tests based on user stories

|     |                                   Story                      | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| ADMIN STORY | As an Admin I will set up Django and install the supporting libraries predicted to be needed so that I am ready to start development MUST HAVE | Pass |
| ADMIN STORY | As an Admin I need to create the env.py and add to .gitignore so that I can securely deploy the site without exposing the developer MUST HAVE | Pass |
| ADMIN STORY | As an Admin I can deploy the site to Heroku early so that I can confirm everything works before the development of the site and to enable continuous testing within the production environment MUST HAVE | Pass |
| USER STORY | As a User, I would like to view the site on my different devices so that I can view the site on the go MUST HAVE | Pass |
| USER STORY | As a User I want to see a clear way of navigating the site so that I can find the information relative to my needs MUST HAVE | Pass |
| USER STORY | As a User, I want to be shown an interesting, inviting index page so that I know exactly what is the page about and it gives me an enhanced experience MUST HAVE | Pass |
| USER STORY | As a User, I want to be able to get in touch with the Developer so that I can enquire about issues/suggestions I may have MUST HAVE | Pass |
| ADMIN STORY | As an Admin I want to install and import the AllAuth library to the project so that I can use it to manage users MUST HAVE | Pass |
| ADMIN STORY | As an Admin I want to add functionality to verify email and reset the password so that the user has better security over their email being used and can reset the password if they forget it COUNLD HAVE | Pass |
| USER STORY | As a User, I want to be able to signup/login/logout securely so that I can view/edit my profile COULD HAVE | Pass |
| USER Story | As a User, I would like to access my profile so that I can upload an image or alter my bio, social media links etc. SHOULD HAVE | Pass |
| USER STORY | As a User, I would like to access my profile with single sign login so that I can login quicker and more securely WONT HAVE | Pass |
| USER STORY | As a User, I want to view the recipe details so that I can read the ingredients, instructions etc. MUST HAVE | Pass |
| ADMIN STORY | As an Admin I want to build a page to display recipes for the users so that they have a clear overview and can find the information they look for MUST HAVE | Pass |
| USER STORY | As a User, I want to view my recipes listed on my page so that I can edit recipe details (e.g.ingredients, instructions etc.) or delete my recipe MUST HAVE | Pass |
| ADMIN STORY | As an Admin I want to create a Recipe model so that the recipe details can be viewed/edited and added to the database MUST HAVE | Pass |
| USER STORY | As a user, I want to be able to click on a recipe so that I can read the full-text MUST HAVE | Pass |
| USER STORY | As a User, I want to be able to view my recipes so that I can edit or delete them MUST HAVE | Pass |
| ADMIN STORY | As an Admin, I want to be able to login to Admin Panel so that I can CRUD manage data MUST HAVE | Pass |
| USER STORY | As a User, I want to have a section where I can search for a Recipe so that I can easily find it access it and comment/like it SHOULD HAVE | Pass |
| ADMIN STORY | As an Admin I want to create the recipe search url, view & template so that the User can search db SHOULD HAVE | Pass |
| USER STORY | As a User, I want to be able to view the recipes by category so that I can easily find what I'm interested in SHOULD HAVE | Pass |
| ADMIN STORY | As an Admin I want to build a page to display recipes by category for the users so that they have a clear overview and can find the information they look for SHOULD HAVE | Pass |
| USER STORY | As a User, I want to have access to my Profile so that I can upload an image or change my bio or social media urls SHOULD HAVE | Pass |
| ADMIN STORY | As an Admin I will create a User Profile page so that they can update their details and setting SHOULD HAVE | Pass |
| USER STORY | As a User, I want the ability to like or comment on recipes so that I can share my thoughts and feel included in the community MUST HAVE | Pass |
| USER STORY | As a User, I want the ability to view all comments for the recipe so that I can see what my fellow commenters think of a recipe MUST HAVE | Pass |
| ADMIN STORY | As an Admin I will provide commenting/like functionality for the User so that they have an enjoyable experience reviewing/liking recipes MUST HAVE | Pass |
| ADMIN STORY | As an Admin I want to have the ability to delete any comment so that I can manage comments effectively MUST HAVE | Pass |
| ADMIN STORY | As an Admin I will implement a 400 bad request page to redirect the user to the home page COULD HAVE | Pass |
| ADMIN STORY | As an Admin I will implement a 403 error page to redirect the user to the home page COULD HAVE | Pass |
| ADMIN STORY | As an Admin I will implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist and redirect the user to the home page COULD HAVE | Pass |
| ADMIN STORY | As an Admin I will implement a 500 error page so that I can alert users when an internal server error occurs and redirect the user to the home page COULD HAVE | Pass |

[Back to top &uarr;](#browser-compatibility)

***

# __Bugs:__


The below Type Error has showed up as I have forgotten to add .as_view() in urls - RESOLVED
![Type Error](README/errors/type_error.png)

---

Heroku deloyment failed: JS (GSAP) animation in home screen started acting up as soon as I moved to production and deployed to Heroku.

    -----> Building on the Heroku-22 stack
    -----> Using buildpack: heroku/python
    -----> Python app detected
    -----> No Python version was specified. Using the same version as the last build: python-3.11.2
    To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
    !
    ! A Python security update is available! Upgrade as soon as possible to: python-3.11.3
    ! See: https://devcenter.heroku.com/articles/python-runtimes
    !
    -----> No change in requirements detected, installing from cache
    -----> Using cached install of python-3.11.2
    -----> Installing pip 23.1.2, setuptools 67.7.2 and wheel 0.40.0
    -----> Installing SQLite3
    -----> Installing requirements with pip
    -----> $ python manage.py collectstatic --noinput
    Traceback (most recent call last):
    File "/tmp/build_bfd91198/manage.py", line 22, in <module>
    main()
    File "/tmp/build_bfd91198/manage.py", line 18, in main
    execute_from_command_line(sys.argv)
    File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
    File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
    File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
    File "/app/.heroku/python/lib/python3.11/site-packages/django/core/management/base.py", line 398, in execute
    output = self.handle(*args, **options)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/app/.heroku/python/lib/python3.11/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 187, in handle
    collected = self.collect()
    ^^^^^^^^^^^^^^
    File "/app/.heroku/python/lib/python3.11/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 114, in collect
    handler(path, prefixed_path, storage)
    File "/app/.heroku/python/lib/python3.11/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 348, in copy_file
    self.storage.save(prefixed_path, source_file)
    File "/app/.heroku/python/lib/python3.11/site-packages/django/core/files/storage.py", line 54, in save
    name = self._save(name, content)
    ^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/app/.heroku/python/lib/python3.11/site-packages/cloudinary_storage/storage.py", line 252, in _save
    if not self._exists_with_etag(name, content):
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/app/.heroku/python/lib/python3.11/site-packages/cloudinary_storage/storage.py", line 241, in _exists_with_etag
    etag = response.headers["ETAG"].split('"')[1]
    ~~~~~~~~~~~~~~~~^^^^^^^^
    File "/app/.heroku/python/lib/python3.11/site-packages/requests/structures.py", line 52, in __getitem__
    return self._store[key.lower()][1]
    ~~~~~~~~~~~^^^^^^^^^^^^^
    KeyError: 'etag'
    ! Error while running '$ python manage.py collectstatic --noinput'.
    See traceback above for details.
    You may need to update application code to resolve this error.
    Or, you can disable collectstatic for this application:
    $ heroku config:set DISABLE_COLLECTSTATIC=1
    https://devcenter.heroku.com/articles/django-assets
    ! Push rejected, failed to compile Python app.
    ! Push failed

I have used a tutor seesion to resolve this issue:
the 'etag' error pops up sometimes when using cloudinary and can be a tricky one to troubleshoot as there doesn't seem to be a consistent solution. Can you try creating a copy of one of your static files, with a different name? You can just select the file here, and use Ctrl+C, then Ctrl+V - RESOLVED 

---

After DEBUG=FALSE and Heroku deployment, index page could not load.
I discovered that that I have typed in incorrect {%%} url in the body of index.html - RESOLVED
![Error on load](README/errors/error-server.png)

[Back to top &uarr;](#browser-compatibility)

***

# __Known Bugs__

GSAP Warnings

![GSAP Warnings](README/validators/warnings.png)

---

Profile Edit does not update username, first or last name or email address.

---

Password change does not update user password

[Back to top &uarr;](#browser-compatibility)

***
Back to [README.md](README.md) file.









![Alt text](README/tests/python/bag-apps.png) 
![Alt text](README/tests/python/bag-context.png) 
![Alt text](README/tests/python/bag-tools.png) 
![Alt text](README/tests/python/bag-urls.png) 
![Alt text](README/tests/python/bag-views.png) 
![Alt text](README/tests/python/checkout-admin.png) 
![Alt text](README/tests/python/checkout-apps.png) 
![Alt text](README/tests/python/checkout-forms.png) 
![Alt text](README/tests/python/checkout-models.png) 
![Alt text](README/tests/python/checkout-signals.png) 
![Alt text](README/tests/python/checkout-URLS.png) 
![Alt text](README/tests/python/checkout-views.png) 
![Alt text](README/tests/python/custom-storages.png) 
![Alt text](README/tests/python/gameonboard-urls.png) 
![Alt text](README/tests/python/gameonboard-wsgi.png) 
![Alt text](README/tests/python/home-apps.png) 
![Alt text](README/tests/python/home-urls.png) 
![Alt text](README/tests/python/home-views.png) 
![Alt text](README/tests/python/manage-py.png) 
![Alt text](README/tests/python/product-apps.png) 
![Alt text](README/tests/python/product-forms.png) 
![Alt text](README/tests/python/product-models.png) 
![Alt text](README/tests/python/product-urls.png) 
![Alt text](README/tests/python/product-views.png) 
![Alt text](README/tests/python/product-widgets.png) 
![Alt text](README/tests/python/webhoocks.png) 
![Alt text](README/tests/python/webhook-handler.png)
![Alt text](README/tests/python/newsletter-admin.png) 
![Alt text](README/tests/python/newsletter-forms.png) 
![Alt text](README/tests/python/newsletter-model.png) 
![Alt text](README/tests/python/newsletter-urls.png) 
![Alt text](README/tests/python/newsletter-views.png)



![Alt text](README/tests/manual/confirm-email-test.png) 
![Alt text](README/tests/manual/login-email-test.png) 
![Alt text](README/tests/manual/logout-email-test.png) 
![Alt text](README/tests/manual/order-email-confirm.png) 
![Alt text](README/tests/manual/signup-email-test.png) 
![Alt text](README/tests/manual/verify-email-test-confirm.png) 
![Alt text](README/tests/manual/verify-email-test.png)