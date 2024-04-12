# Fit Freak's README

[View the live project here.](https://fit-freak-e89ae93eb2ed.herokuapp.com/)

## Desktop Homepage

![Image of the homepage from a Desktop user's perspective](/media/readme/homepage-desktop.png)

## Mobile Homepage

![Image of the homepage from a Mobile user's perspective](/media/readme/homepage-mobile.png)

## Description

Welcome to Fit Freak, the best place for your e-commerce gym-based needs!

### Project Goal

#### CI Project Example Idea 2

- Fit Freak is aiming to provide top end merchandise and supplements to anyone and everyone that enjoys fitness.

#### Site owner's goal:

- Build an e-commerce store focused on the needs of regular gym-goers, and newbies alike.

#### External user’s goal:

- To join a ﬁtness community and purchase exercise merchandise and supplements.

## UX

### Exisiting Features

#### Navigation bar

Summary:
- The navigation bar allows us to select a part of the page that we'd like to navigate to, as well as having the logo as a top of the page button.

![Image of the branded5 navbar from a Desktop user's perspective](/media/readme/feature-navbar-desktop.png)

#### Accurate Basket Total

Summary:
- The basket total stays up to date with whatever you put in your basket.

![Image of the basket total after adding products to the bag](/media/readme/basket-total-mobile.png)

#### Toast Messages

Summary:
- The toast messages vary depending on the response from the user's action. 

![Successful toast message](/media/readme/toast-message-mobile.png)
![Warning toast message](/media/readme/toast-message-alert-mobile.png)
![Error toast message](/media/readme/toast-message-error-mobile.png)

#### Product Creation Form

Summary:
- The add product form allows store managers to add their own products. 

![Image of the product add page](/media/readme/product-add-page-mobile.png)

## Design

### Website Color Scheme

- Main Background: #edcd1d (Body / Light Text)
- Dark Accent: #111 (Navbar / Dark Contrast Elements)
- Light Accent: #fff (Certain Titles / Accenting / Light Elements)

### Font

I predominantly use the "Lato" font as it's clear and easy to read for new customers. 
The font is also asthetically pleasing and versatile when it comes to matching a simpler and sharper design like mine.

## Testing

### Validation/Code Linter

1. W3C (https://jigsaw.w3.org/css-validator/#validate_by_input)
- Checked all CSS manually using the above site. 

2. Python (https://extendsclass.com/python-tester.html)
- Checked all Python code within the main.py file using the site above.

3. Flake8 (https://flake8.pycqa.org/en/latest/)
- Checked all local python files (
    excluding any files within these folders since they're not in my control =
    "migrations",
    "__pycache__",
    ".venv",
    "venv"
    )

3. HTML (https://marketplace.visualstudio.com/items?itemName=CelianRiboulet.webvalidator)
- Checked using W3C VS Code extension (https://marketplace.visualstudio.com/items?itemName=CelianRiboulet.webvalidator)

4. CSS (https://marketplace.visualstudio.com/items?itemName=CelianRiboulet.webvalidator)
- There are no clear CSS errors within the project. Checked using W3C VS Code extension.

5. JavaScript (https://www.site24x7.com/tools/javascript-validator.html)
- There are no clear JS errors within the JavaScript files.

### Test Environments: The test will be conducted on multiple devices and browsers, including:

Desktop (Windows and macOS):
- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Safari

Mobile (iOS and Android):
- Safari (iOS)
- Google Chrome (Android)
To confirm, I only tested as low as 380px on mobile, since this is the lowest a generic device goes.

### Automated Testing
Automated testing involves using tools and scripts to test the application automatically. This can include unit tests, integration tests, and end-to-end tests. Automated testing is beneficial for catching regressions and ensuring that the application functions as expected after code changes.

### Manual Testing
Manual testing is performed by human testers who interact with the application to identify bugs, usability issues, and other problems. Manual testing is valuable for evaluating the user experience, design, and overall functionality.

### User Stories

#### Story 1: Test Register Functionality

- Registering: This test will be able to confirm whether the account register function works as expected.

Steps:- 
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Click on the "Register" button located at the top right corner of the homepage.
3. Fill in the registration form with valid details including email, password, full name, etc.
4. Click on the "Register" button to submit the form.
5. Check the registered email inbox for a verification email.
6. Open the verification email and click on the provided verification link.
7. Verify that the account is successfully activated by logging in with the registered credentials.

Expected Result:-
- The user should be able to register with their email address, as long as they've not signed up before.

![Image of the confirmation email](/media/readme/confirmation-email.png)

#### Story 2: Test Login functionality

- Logging in: This test will be able to confirm whether the account login function works as expected.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Click on the "Login" button located at the top right corner of the homepage.
3. Enter the registered email and password.
4. Click on the "Login" button to submit the credentials.
5. Verify that the user is successfully logged into the account.

Expected Result:-
- The user should be able to login with their newly created account.

![Image of the a successful login toast confirmation](/media/readme/successful-login.png)

#### Story 3: Testing Product Sort Functionality

- Sorting/Filtering: This test will be able to confirm whether the sort & filter functions work as expected.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Select "All Products" from the navigation menu.
3. Choose different categories such as "Clothing," "Equipment," and "Plans."
4. Verify that each category displays a dropdown menu for sorting options.
5. Select sorting options such as "Price: Low to High," "Price: High to Low," etc.
6. Verify that the products are displayed according to the selected sorting option.

Expected Result:- 
- When sorting and filtering by a specified option, the user should see the relevant data returned in the product results.

![Image of the product sort from high to low, and filtered accessories](/media/readme/product-filter-accessories-high-to-low.png)

#### Story 4: Updating Account Details

- Updating Account Info: This test will be able to confirm whether the update details function works as expected.

1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Log in to your account on the website.
3. Click on the "My Account" dropdown button and select "My Profile."
4. Update any of the account details such as phone number, postal code, etc.
5. Ensure that all required fields are filled.
6. Select "Update Information" to save the changes.
7. Verify that a successful toast message appears confirming the update.

Expected Result:- 
- When editing the fields within the edit form, the user should see be only able to input relevant data and the save button should retain their details.

![Image of the successful profile update toast.](/media/readme/successful-profile-detail-update.png)

#### Story 5: Completing A Purchase

- Adding a Product to Bag and Checkout:

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Search for a specific product (e.g., "swim shorts").
3. Click on the desired product to view its details.
4. Click on the "Add to Bag" button to add the product to the shopping bag.
5. Navigate to the shopping bag by clicking on the shopping bag icon.
6. Click on the "Checkout" button to proceed to the checkout page.
7. Verify that the delivery details are pre-filled (if applicable).
8. Fill out the required fields for name and card details including card number, expiry date, CVV, ZIP code, etc.
9. Complete the checkout process by clicking on the "Place Order" or similar button.
10. Verify that a successful toast message appears upon completing the payment.
11. Check the registered email for an order confirmation email.

![Image of the successful purchase](/media/readme/completed-payment-screen.png)

#### Story 6: Order History

- Checking Order History: This test will validate the order history form's functionality.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Login to an account.
3. Click on the "My Account" dropdown button and select "My Profile."
4. Scroll down to find the "Order History" section.
5. Verify that the correct items and order details are displayed.
6. Click on the order ID
7. Observe the correct data on the Order receipt (Delivery address, items, etc.)
8. Observe the toast message (alert) that makes the user aware of this being a past order.

![Image of the user's order-history](/media/readme/order-history.png)

#### Story 7: Logout

- Logging in: This test will be able to confirm whether the user logout function works as expected.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Login to an account.
3. Click on the "My Account" dropdown button.
4. Select Logout.
5. Observe "Are you sure?" screen.
6. Select 'Sign Out'
7. Observe the user is redirected to the homepage.
8. Select 'My Account'
9. Observe user is able to register or login.

![Image of the successful logout, login button visible post logout.](/media/readme/login-button.png)

#### Story 8: Forgot Password?

- Forgot Password: This test will be able to confirm whether the password reset function works as expected.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Click on the "My Account" dropdown button.
3. Select Login.
4. Select 'Forgot Password?'
5. Input an email address for an existing account.
6. Navigate to user's email
7. Select Forgotten Password link within email
8. Input new password
9. Select 'Change password'
10. Observe password changed confirmation. 

![Image of the successful password change toast](/media/readme/toast-password-change.png)

#### Story 9: Adding a Product

- Adding a new product: This test will be able to confirm whether the add product form works.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Click on the "My Account" dropdown button.
3. Select Login.
4. Login as an admin or staff member.
5. Select My Account
6. Select Product Management
7. Fill out form with relevant data
8. Choose an image file for the product
9. Select 'Add Product'
10. Observe Successful product added toast. 

![Image of the successful product add toast](/media/readme/successful-add-product.png)

#### Story 10: Edit a product

- Adding a new product: This test will be able to confirm whether the add product form works.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Click on the "My Account" dropdown button.
3. Select Login.
4. Login as an admin or staff member.
5. Search for a product
6. Select edit
7. Edit form fields
8. Select Update Product
9. Search for the recently edited product
10. Observe updated product details

![Image of a product being edited by an admin](/media/readme/edit-existing-product-as-admin.png)

#### Story 11: Delete a product

- Adding a new product: This test will be able to confirm whether the add product form works.

Steps:-
1. Open a web browser and navigate to https://fit-freak-e89ae93eb2ed.herokuapp.com/.
2. Click on the "My Account" dropdown button.
3. Select Login.
4. Login as an admin or staff member.
5. Search for a product
6. Select a product
7. Select delete
8. Observe toast pop up
9. Search for product
10. Validate product no longer present

![Image of the successful product add toast](/media/readme/delete-product-toast.png)

#### Story 12: Negative Test Cases

Objective: Confirming the negative cases are accounted for.

Examples:-

1. Registering an Account: Attempt to register with an already registered username.
- Expected Result: An error will be thrown when attempting to do so.
- Actual Result: Confirmed, an error was returned.
![Image of the error after trying to use a taken username](/media/readme/username-error.png)

2. Logging in: Use incorrect credentials and verify login failure.
- Expected Result: An error will be thrown when attempting to do so.
- Actual Result: Confirmed, an error was returned.
![Image of the error after trying to login with the incorrect credentials](/media/readme/error-login.png)

3. Register without required field: Leave a required field blank and attempt to register an account.
- Expected Result: An error will be thrown when attempting to do so.
- Actual Result: Confirmed, an error was returned.
![Image of the error after trying to register an account without filling out required fields](/media/readme/field-validation.png)

4. Adding Product to Bag and Checkout: Attempt to checkout with an expired card.
- Expected Result: An error will be thrown when attempting to do so.
- Actual Result: Confirmed, an error was returned.
![Image of the error after trying to checkout with an expired card](/media/readme/expired-card-error.png)

5. Adding Product to Bag and Checkout: Proceed to checkout without filling in any payment details.
- Expected Result: An error will be thrown when attempting to do so.
- Actual Result: Confirmed, an error was returned.
![Image of the error when trying to checkout without inputting card details](/media/readme/expired-card-error.png)

#### Examples of Exploratory Testing for "Fit Freak"

Testing Responsiveness:
- Expected Result: Page layout remains responsive depending on what kind or size of device you're using.
- Actual Result: Confirmed, page layout is responsive.

Testing Scripts:
- Expected Result: JavaScript functions without console errors.
- Actual Result: Confirmed, no errors in the console.

Testing Compatibility:
- Expected Result: Page functions correctly in different browsers.
- Actual Result: Confirmed, page works in various browsers.

Documentation:
- Expected Result: README.md is updated with instructions.
- Actual Result: Confirmed, documentation is updated.

Final Checks:
- Expected Result: No spelling or grammatical errors in the copy.
- Actual Result: Confirmed, no errors found.

### Automated Testing Examples (NOT IMPLEMENTED):

#### Regression Testing:

- Scenario: After implementing new features or making changes to the codebase, there is a need to ensure that existing functionalities still work as expected.

Automation Approach:
- Develop a suite of regression tests covering critical functionalities.
- Automate the execution of these tests to run after each code change.
- This ensures that existing features are not broken by new updates.

#### Cross-browser Testing:

- Scenario: Verifying that a web application works consistently across different web browsers (Chrome, Firefox, Safari, Edge) and versions can be time-consuming if done manually.

Automation Approach:

- Use a testing framework such as Selenium or Playwright to automate browser interactions.
- Develop scripts that simulate user interactions on different browsers.
- Automate the execution of these scripts to run on various browser configurations.
- This ensures the application's compatibility with multiple browsers.

#### Load Testing:

- Scenario: Assessing the performance and scalability of a web application under various load conditions (multiple users, high traffic) is crucial to identify potential bottlenecks.

Automation Approach:

- Use tools like Apache JMeter, Gatling, or locust.io to simulate a large number of virtual users.
- Develop test scenarios to mimic real-world user interactions.
- Automate the execution of these load tests to analyze the application's performance under different load levels.
- This helps identify performance issues and ensures the application can handle expected user traffic.

### Further Testing

- The Website was tested on Google Chrome, Internet Explorer, Opera and Safari browsers.
- The website was viewed on a variety of devices such as Desktop (OSX & Windows), Laptop (OSX & Windows), Tablet, iOS (iPhone) and Android (Google Pixel).
- A large amount of testing was done to ensure that all pages were linking correctly.
- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.


## Technologies Used

Fit Freak uses the following technologies:

- JavaScript: [Learn more about JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- Python: [Learn more about Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- Django: [Learn more about Django](https://en.wikipedia.org/wiki/Django_(web_framework))
- HTML: [Learn more about HTML](https://en.wikipedia.org/wiki/HTML)
- CSS: [Learn more about CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- Bootstrap: [Learn more about Bootstrap](https://startbootstrap.com/theme/agency)

## Data Model 

In this section, describe the data model designed for your project. You can include information about the entities, attributes, and relationships in your data model. Based on the example provided, your data model could look like this:

### Attributes:

#### Category Schema

- pk = Primary key is a unique identifier for each record 
- model = Type of Products object
- name = Name used predominantly for code usage
- friendly_name = Name for front-end customer view

e.g.
    <!-- {
      "pk": 1,
      "model": "products.category",
      "fields": {
        "name": "upper_body",
        "friendly_name": "Upper Body"
      } -->

Here's an example entry in the dataset:
![Image of the category schema in use](/media/readme/category_admin_example.png)

#### Product Schema

- pk = Primary key is a unique identifier for each record 
- model = Type of Products object
- sku = Stock Keeping Unit (A unique code assigned to each distinct product or item)
- name = Name used predominantly for code usage
- friendly_name = Name for front-end customer view
- description = Defines the product / item
- price = The cost of the item
- category = Which family of products / items it belongs to
- rating = A rating out of 5 by the end user of the product / item
- image_url = A path for the product's image
- image = The file name of the image

  <!-- {
    "pk": 2,
    "model": "products.product",
    "fields": {
      "sku": "ff1000002",
      "name": "Bucket Hat",
      "description": "Stay cool and stylish with our Fitness Freak Bucket Hat. Perfect for outdoor workouts or casual wear. Made from durable materials to withstand any activity.",
      "price": 14.99,
      "category": 3,
      "rating": 4.32,
      "image_url": "/media/bucket-hat-context.png",
      "image": "bucket-hat-context.png"
    } -->

Here's an example entry in the dataset:
![Image of the product schema in use](/media/readme/product_admin_example.png)

#### User profile Schema

- user = The user that is associated with the delivery address
- phone_number = The phone number of the user
- post_code = Name used predominantly for code usage
- town_or_city = The town or city the user lives in
- street_adress1 / 2 = The street the user lives on
- post_code = The post code of the user
- county = The county of the user
- country = The country of the user

Here's an example entry in the dataset:
![Image of the user delivery details](/media/readme/delivery-data.png)

### AWS S3

Guide used: [Boutique Ado guide (CI)](https://learn.codeinstitute.net/ci_program/level5diplomainwebappdevelopment)

In this guide, I was assisted by Chris (CI Dev) via a video that is designed to help students setup and implement a AWS as a database.

#### AWS Integration:

- AWS Implementation:

1. Create an AWS S3 Bucket: Sign in to AWS Management Console, navigate to S3, and create a bucket.
2. Upload Data to the Bucket: Upload your files to the S3 bucket using AWS Management Console or CLI.
3. Permissions: Add a permission policy so that Heroku is able to interact freely.
4. Set Up IAM Credentials: Create an IAM user with S3 permissions and get access keys.
5. Configure Heroku: Set AWS credentials as environment variables.
6. Access Data in Your Heroku App: Write code to interact with S3 using AWS SDK.
7. Deploy Your Heroku App: Deploy your app to Heroku, ensuring correct environment variables.
8. Testing and Monitoring: Test app functionality, monitor performance, and AWS usage.


#### Benefits

- Scalability: Easily scale resources up or down based on demand.
- Reliability: High availability with data centers in multiple regions.
- Cost-effectiveness: Pay-as-you-go pricing model reduces upfront costs.
- Security: Robust security measures and compliance certifications.
- Global Reach: Deploy applications close to users worldwide.
- Flexibility: Wide range of services for various workloads.
- Ecosystem: Rich ecosystem of integrations and support resources.

## Frameworks, Libraries & Programs Used

- AWS (aws.amazon.com)
- ElephantSQL (https://www.elephantsql.com)
- Spire (https://stripe.com/gb/payments)
- Google Fonts (https://fonts.google.com/specimen/Lato)
- Font Awesome (https://fontawesome.com/)
- GitHub (https://github.com/)
- Django (https://www.djangoproject.com)
- Heroku (https://dashboard.heroku.com)

## Deployment

### Heroku
The project was deployed to Heroku following a guide from CodeInstitute.
1. See CI link: (Boutique Ado)
- https://learn.codeinstitute.net/ci_program/level5diplomainwebappdevelopment

2. Live project link here:
- https://fit-freak-e89ae93eb2ed.herokuapp.com/

### Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...
1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

## Credits

### Content

- Printify - Product designs (https://printify.com/)
- All text-based content was written by the developer or generated generically by ChatGPT
- Custom code written by developer
- Hero image - (https://www.freepik.com/free-photo/fitness-stuff-grey-background_5162337.htm#from_view=detail_serie)
- Bootstrap - Theme  / Components (https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- Fontawesome - Icons (https://fontawesome.com)

### Acknowledgements

- Stackoverflow for JS/Python error troubleshooting.
- YouTube for JS/Python error troubleshooting.
- ChatGPT - Data generation (e.g, list of descriptions for products, etc.)

### Code inspiraton from external sources

- Stack Overflow - Bug fixing
- Code Institute - https://learn.codeinstitute.net/courses/
