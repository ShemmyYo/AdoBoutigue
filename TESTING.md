Back to [README.md](README.md) file.

# Browser Compatibility

<img height="50" src="README/tests/browser/google_chrome_icon.png"><img height="50" src="README/tests/browser/png-transparent-microsoft-edge-new-icon.png"><img height="50" src="README/tests/browser/firefox-icon.png">

After publishing to Heroku, the site was tested on Google Chrome, Microsoft Edge and Mozilla Firefox, with no visible issues for the user. 

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

![Register](README/tests/html/sign-up.png)
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

Some features of the GamerOnGoard webshop, like storing details or browsing order history, are restricted to registered users. 
User is welcomed on landing page where it is invited to browse stock by clicking 'Shop Now' button. 
User is able to create 'Profile' at any stage however, it is possible to make a purchase withough creating one. 
Some functionality like 'Product Managment'is restricted to Superusers only.

## __Welcome Screen__

<details><summary> >>> Click for details</summary>

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

## __Update Profile Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| 'My Profile' link has opened and loaded correctly and as intended | Pass |
| Verified that the User can update Phone number | Pass |
| Verified that the User can update Street Address 1 | Pass |
| Verified that the User can update Street Address 2 | Pass |
| Verified that the User can update Town or City | Pass |
| Verified that the User can update County | Pass |
| Verified that the User can update Postal Code | Pass |
| Verified that the User can update Phone number | Pass |
| Verified that the User can update Country | Pass |
| Verified that the Country list API is working as intended  | Pass |
| Verified that 'Update Profile' button updates data | Pass |
| Verified that User is shown 'Order History'  | Pass |
| Verified that User can open any saved 'Order History' and view details  | Pass |
| Varified that the user is being updated by quick messages as intended | Pass |
</details>

## __Change Password Screen__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Change password screen has loaded correctly and as intended | Pass |
| Verified that the User can update their password via email| Fail |
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
| Verified that the User can click + button on quantity selector form to increases number + 1 | Pass |
| Verified that the User can click - button on quantity selector form to decreases number - 1 | Pass |
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
| Varified that the User logout page redirects user to 'All Products' | Pass |
| Varified that the User is being updated by quick messages as intended | Pass |
</details>

## __Bag__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Verified that Checkout screen has loaded correctly and as intended | Pass |
| Verified that Cash Register icon in main nav redirects user to bag page | Pass |
| Verified that + button on quantity selector form increases product by + 1 if it is less than or equal to product's stock | Pass |
| Verified that - button on quantity selector form decreases product by -1 if it is greater than one | Pass |
| Verified that update button under quantity selector form updates quantity of product in Bag to number in quantity select form | Pass |
| Verified that remove button under quantity selector form removes product from Bag completely | Pass |
| Verified that manually entered number greater than product stock in quantity selector form shows stock availabity error message | Pass |
| Verified that removing item from basket brings total to below €50 and changes delivery from FREE to 10% | Pass |
| Verified that 'Keep Shopping' button redirects to 'All Products' page | Pass |
| Verified that 'Pay Stripe' button redirects to checkout page | Pass |
| Varified that the User is being updated by quick messages as intended | Pass |
</details>

## __Checkout__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Checkout screen has loaded correctly and as intended | Pass |
| Verified that 'Pay Stripe' button redirects to checkout page | Pass |
| Click 'Complete Order' button without all required fields filled out shows error message | Pass |
| Checked 'Save delivery information to profile' button causes information to save data to profile if logged in | Pass |
| Verified that clicking 'Create Account' link, redirects to sign up page | Pass |
| Verified tha clicking 'Login' in nav, redirects to sign in page | Pass |
| Varified that clicking 'Complete Order' button without card details filled out shows error message | Pass |
| Verified that clicking 'Complete Order' button with all details filled out loads spinner and order is processed | Pass |
| Varified that 'Order completed' status sends confirmation email, updates stock levels and redirects to checkout success page | Pass | 
| Verified that the User is being updated by quick messages as intended | Pass |
</details>

## __Checkout Success Page__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Checkout success screen has loaded correctly and as intended | Pass |
| Varified that Order completed redirects to checkout success page | Pass |
| Varified that clicking 'Checkout latest deals' button redirects user to all products page | Pass |
| Varified that clicking Back to profile button button redirects user to their profile | Pass | 
| Varified that the User is being updated by quick messages as intended | Pass |
</details>
 
## __Add Product Page__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Add Product screen has loaded correctly and as intended | Pass |
| Varified that clicking 'Add Product' link from Admin dropdown redirects admin to 'Add product' page | Pass | 
| Varified that clicking 'Cancel' button redirects admin to all products page | Pass | 
| Varified that clicking 'Add Product' button with form filled correctly creates a new product | Pass | 
| Varified that clicking 'Add Product' button with form filled incorrectly shows error message | Pass | 
| Varified that set product's stock to be less than 1 creates product which is shown as sold out | Pass | 
| Varified that clicking 'Add Product' button with no image set displayes product with default product image | Pass | 
| Verified that forcing the URL to add a new product if not Admin  does not work | Pass | 
| Varified that the User is being updated by quick messages as intended | Pass |
</details>

## __Edit Product Page__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| 'Edit Product' screen has loaded correctly and as intended | Pass |
| Verified that clicking edit link on product card redirects user to Edit Product page | Pass |
| Verified that clicking 'Cancel' button Redirects Admin to 'All Products' page | Pass |
| Verified that clicking 'Update' Product button with form filled correctly updates product correctly | Pass |
| Verified that clicking 'Update' Product button with form filled incorrectly shows error message | Pass |
| Verified that setting product's stock to be less than 1 shows product as 'sold out' with add to basket button disabled | Pass |
| Verified that setting product's stock to be less than 3 shows product as limited availability | Pass |
| Verified that setting product's stock to be more than 3 shows product as 'in stock' | Pass |
| Varified that the User is being updated by quick messages as intended | Pass |
</details>

## __Delete Product__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| Verified that clicking 'delete' link on product causes a popup message to appear | Pass | 
| Varified that if the User clickes ok on popup message, product is deleted | Pass |
| Varified that forcing the URL to delete a product if not an admin does not work | Pass |
| Varified that the User is being updated by quick messages as intended | Pass |
</details>

## __Footer__

<details><summary> >>> Click for details</summary>

| Verification | Result |
| :----------------------------------------------------------: | :-------------: |
| screen has loaded correctly and as intended | Pass |
| Verified that clicking social media icons in footer opens social media site clicked in a new tab | Pass |
| Verified that clicking on Classic Games link in footer redirects to Classic category products page | Pass | 
| Verified that clicking on Chess Games link in footer redirectr to Chess category products page | Pass | 
| Verified that clicking on Strategy Games link in footer redirectr to Strategy category products page | Pass | 
| Verified that clicking on RPG's Games link in footer redirects to RPG category products page | Pass | 
| Verified that clicking on for One category link in footer redirects to products page by category | Pass |
| Verified that clicking on for Kids category link in footer redirects to products page by category | Pass |
| Verified that clicking on for Families category link in footer redirects to products page by category | Pass |
| Verified that clicking on for Parties category link in footer redirects to products page by category | Pass |
| Verified that clicking on Subscribe button on blank newsletter form shows error message | Pass |
| Verified that clicking on Subscribe button on filled newsletter form shows alert message | Pass |
| Verified that clicking subscribe to newsletter with already subscribed email address shows error message | Pass |
| Varified that the User is being updated by quick messages as intended | Pass |
</details>

[Back to top &uarr;](#browser-compatibility)

***

# <img height="50" src="README/tests/user/user-stories.png"> Tests based on user stories

|     |                                   Story                      | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| [EPIC 1](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/1) | Django & Project Basic Setup | Completed |
| ADMIN STORY | Setup Django Env, Project and App `MUST HAVE` | Pass | 
| ADMIN STORY | Create 'HOME' App `MUST HAVE` | Pass | 
| ADMIN STORY | Heroku Deployment `MUST HAVE` | Pass | 
| USER STORY | Home Page `MUST HAVE`  | Pass | 

***

|     |                                   Story                      | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| [EPIC 2](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/3) | User Authentication & Page Admin | Completed |
| ADMIN STORY | AllAuth Setup  `MUST HAVE` | Pass | 
| ADMIN STORY | AllAuth Login Templates `MUST HAVE`  | Pass |
| ADMIN STORY | Connect Google Social Account to AllAuth `COULD HAVE ` | Pass |
| USER STORY | Account Registration `SHOULD HAVE`  | Pass | 
| USER STORY | Personalised User Profile `SHOULD HAVE`  | Pass | 
| USER STORY | Login and Logout `SHOULD HAVE`  | Pass | 
| USER STORY | Email Confirmation after Registration `SHOULD HAVE`  | Pass | 

***

|     |                                   Story                      | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| [EPIC 3](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/2) | Product App | Completed |
| ADMIN STORY | Add Product  `MUST HAVE` | Pass | 
| ADMIN STORY | Edit/Update Product  `MUST HAVE` | Pass | 
| USER STORY | Special Offers `MUST HAVE` | Pass | 
| USER STORY | View a list of Products `MUST HAVE` | Pass | 
| USER STORY | View Product Details `MUST HAVE` | Pass | 
| USER STORY | Search Bar `SHOULD HAVE` | Pass | 
| USER STORY | View Product by Category `MUST HAVE` | Pass | 
| USER STORY | Sorting Products `MUST HAVE` | Pass | 
| USER STORY | Product Card details `COULD HAVE` | Pass | 
| USER STORY | Carousel on home page `COULD HAVE` | Pass | 

***

|     |                                   Story                      | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| [EPIC 4](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/4) | Bag, Checkout and Payment | Completed |
| USER STORY | Bag `MUST HAVE`  | Pass | 
| USER STORY | View total of my purchase `MUST HAVE`  | Pass | 
| USER STORY | Product Quantity `MUST HAVE`  | Pass | 
| USER STORY | View Bag `MUST HAVE`  | Pass | 
| USER STORY | Payment `MUST HAVE`  | Pass | 
| USER STORY | Safe and Secure Payment `MUST HAVE`  | Pass | 
| USER STORY | Email Confirmation after Purchase `MUST HAVE`  | Pass | 

***

|     |                                   Story                      | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| [EPIC 5](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/5) | Subscriptions | Completed |
| USER STORY | Subscribtion to newsletter `SHOULD HAVE`  | Pass |

***

|     |                                   Story                      | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| [EPIC 7](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/7) | Marketing and Search Engine Optimalisation | Not Completed |
| ADMIN STORY | Marketing `MUST HAVE`  | Pass | 
| ADMIN STORY | Social Media `MUST HAVE`  | Pass | 
| ADMIN STORY | Social Media Extra `SHOULD HAVE`  | Pass | 

***

|     |                          Story that have not been finished       | Result |
| --- | :----------------------------------------------------------: | :-------------: |
| USER STORY | Discount `WONT HAVE` |  | 
| USER STORY | Like Product `SHOULD HAVE` |  |
| USER STORY | View Liked Products `SHOULD HAVE` |  |
| [EPIC 6](https://github.com/ShemmyYo/game-on-board-p5-ecommerce-app/milestone/6) | Reviews and Blog | Not Completed |
| USER STORY | View Blog `COULD HAVE` |  | 
| USER STORY | Create Blog Posts `COULD HAVE` |  | 
| USER STORY | Edit Post `COULD HAVE` |  | 
| USER STORY | Deleted Blog Posts `COULD HAVE` |  | 

[Back to top &uarr;](#browser-compatibility)

***

# <img height="50" src="README/tests/error/bugs.png"> __Bugs:__

**Order Total, Delivery and Grand Total are not loading after Checkout**

**ISSUE**: After checkout button is pressed the order total, delivery and grand total are not showing correctly. 

![Alt text](README/tests/error/billing-info-not-showing-charges.png)

**FIX**: https://code-institute-room.slack.com/archives/C026VTHQDNY/p1698226453705119

***
**Python No AgeGroup matches the iven query error while adding products**

**ISSUE**: `No AgeGroup matches the given query` shows up everytime I add a new product either via Admin panel or Product Management page.

![Alt text](README/tests/error/error-agegroup-django.png)

**FIX**: model 'product_detail' incorrectly included
`age = get_object_or_404(Product, pk=product_id)` which caused the system to search for product id within id of category model.  
![Alt text](README/tests/error/error-agegroup.png)

***

**Deployment to Heroku now showing as it does in local**

**ISSUE**: The previous setup I had works fine for connecting to the database on Heroku because the project is able to find the DATABASE_URL in your config vars. On Gitpod it seems to be having difficulty finding the DATABASE_URL in the Gitpod variables. I would consider setting up an env.py file and storing DATABASE_URL (and stripe keys and secret key, etc) in there, and using the if/else setup for the databases like you have been doing.

**FIX**: Added variables to GitPod. For security, it's best not to have elephantSQL URLs etc. directly in settings.py

***

**Python AtributeError at Checkout error**

**ISSUE**: The below error come us everytime user clicks on checkout.

![Alt text](README/tests/error/atribute-error-oject-has-no-attribute-original_bag.png) 
![Alt text](README/tests/error/atribute-error-oject-has-no-attribute-original_bag-error-fixed.png) 

**FIX**: `order = stripe_pid = pid ` line in the checkout view had been written incorrectly and contained a `.` instead of `=`

![Alt text](README/tests/error/atribute-error-oject-has-no-attribute-original_bag-error-found.png) 


[Back to top &uarr;](#browser-compatibility)

***

# <img height="50" src="README/tests/error/bugs.png"> __Known Bugs__


[Back to top &uarr;](#browser-compatibility)

***

# <img height="50" src="README/tests/automated/test_python_icon.png"> __Python Unit Testing__

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test `


<details><summary> >>> Click for Bag - User Access</summary>

![Access to Product page](README/tests/automated/access-to-product-page-1.png)
</details>

<details><summary> >>> Click for Order Form Test - full_name</summary>

![Testing Order Form](README/tests/automated/order-form-test-1.png)
</details>

<details><summary> >>> Click for Order Form Test - email</summary>

![Testing Order Form](README/tests/automated/order-form-test-2.png)
</details>

<details><summary> >>> Click for Order Form Test - phone_number </summary>

![Testing Order Form](README/tests/automated/order-form-test-3.png)
</details>

<details><summary> >>> Click for Order Form Test - street_address_1</summary>

![Testing Order Form](README/tests/automated/order-form-test-4.png)
</details>

<details><summary> >>> Click for Order Form Test - town_or_city</summary>

![Testing Order Form](README/tests/automated/order-form-test-5.png)
</details>

<details><summary> >>> Click for Order Form Test - country</summary>

![Testing Order Form](README/tests/automated/order-form-test-6.png)
</details>

<details><summary> >>> Click for Product Form Test - name</summary>

![Product Form testing](README/tests/automated/product-form-test-1.png)
</details>

<details><summary> >>> Click for Product Form Test - min_players</summary>

![Product Form testing](README/tests/automated/product-form-test-2.png)
</details>

<details><summary> >>> Click for Product Form Test - max_players</summary>

![Product Form testing](README/tests/automated/product-form-test-3.png)
</details>

<details><summary> >>> Click for Product Form Test - description</summary>

![Product Form testing](README/tests/automated/product-form-test-4.png)
</details>

<details><summary> >>> Click for Product Form Test - game_play_time</summary>

![Product Form testing](README/tests/automated/product-form-test-5.png)
</details>

<details><summary> >>> Click for Product Form Test - price</summary>

![Product Form testing](README/tests/automated/product-form-test-6.png)
</details>

<details><summary> >>> Click for Product Form Test - stock</summary>

![Product Form testing](README/tests/automated/product-form-test-7.png)
</details>




[Back to top &uarr;](#browser-compatibility)

Back to [README.md](README.md) file.
