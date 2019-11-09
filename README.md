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
    * Look up history
    * Log Out
    
# Models:    
    
   **Account Model** - Keeps track of details about a person’s credentials, including username, password, and any money that they     have paid/owed.  Communicates w/ most routes. 
   
  **Home route** - is responsible for keeping track of login credentials.  Information from it is displayed from the Login &     Logout view. 
  
  **Login & Logout view** - Show a user that they either need to log in with an account, or have logged out of an account.  Shows information from the Home route.
  
  **Calculator route** - Takes the total bill, and other custom credentials,  and calculates a way to split them evenly.  Takes values from, and gives values to the Payment view.
    
    
    
# How the app works:

1. **Register** : Uses the files app.db which is the database file to store credential information. The python files used to run it include init.py and forms.py 

2. **Login** : Python files required: config.py, run.py, forms.py . The lofin page then navigates to main homepage.

3. **Logout** : Button takes us back to the home page. 

OTHER FEATURES IN PROGRESS.


    

    












 
