# SmartSplit
Group Project for CMPE 131

# IDEA:
This app is designed in order to facilitate tracking and splitting payments between a group of people whenever more than one person is involved in a purchase or transactions. 

Examples:
1. Splitting a PG and E bill with your suitemates once an assigned person pays for it.
2. Splitting a restaurant bill amongst friends/cowerkers/relatives.

# Features:

1. User registers and creates an account.
2. Once logged in, the user gets the following options:
    * Even-Split
    * Custom-Split
    * Edit credentials
    * Log in
    * Log Out
    
# Models:    
    
   **Account Model** - Keeps track of details about a person’s credentials, including username, password, and any money that they     have paid/owed.  Communicates w/ most routes. 
   
  **Home route** - is responsible for keeping track of login credentials.  Information from it is displayed from the Login &     Logout view. 
  
  **Login & Logout view** - Show a user that they either need to log in with an account, or have logged out of an account.  Shows information from the Home route.
  
  **Calculator route** - Takes the total bill, and other custom credentials,  and calculates a way to split them evenly.  Takes values from, and gives values to the Payment view.
    
    
    
# How the app works:
  ## Features:

1. **Homepage** : The homepage includes all the options available to user once they go to the website. The options are listed below as features as well.

2. **Register** : Uses the database file to store credential information. Username, password, confirm password and submit fields are used. Once registered, the information is saved locally

3. **Login** : Asks for the username and password. After clicking on submit/ login : redirects user to the hoempage.

4. **Logout** : Logs the user out. The user still stays on the homepage but is not logged into their account anymore.

5. **Edit Credentials** : Allows user to change their password. Requires a user to have already been logged in. If not already logged in, redirects user to login screen. Else, redirects user to home screen when new password is submitted.

6. **Even Split** : Basic split option. User inputs total cost, number of people involved, and a comment. Shows the split cost as total cost divided by number of people. Posts the transaction w/ username, total cost, # people, and comment on the History page.

7. **Transaction History** : Displays transactions in order of username, total cost, # people, and comment.

8. **Survey** : Presents a survey to be filled out by the user.

9. **Rating** : The link helps get feedback from the user. It directs users to a page where they can rate the app accordingly.

12. **About Us** : Displays additional information about the site.

11. **CSS** : The web pages are styled and designed in their respective html files themselves to make it.



# Unit Tests

The unit tests can be located at the following link: https://github.com/senaig97/Project/tree/master/app/tests

To run the unit tests, install pytest by running:
```
pip install pytest
```
Then run the following command in the base directory:
```
pytest
```
