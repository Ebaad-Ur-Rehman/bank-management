# Bank Management System (Python)

A beginner-friendly command-line banking app built with Python, using OOP and JSON for data storage.

## Features
- Create an account (age 18+ check, unique CNIC check, 4-digit PIN, initial deposit)
- Auto-generated unique account number
- Login with PIN (3 attempts allowed)
- Check balance
- Deposit and withdraw money
- View transaction history
- View account info
- Transfer money to another account
- Change PIN
- Delete account (requires PIN and confirmation)
- All data saved in `accounts.json`

## Concepts Used
- Classes and objects
- File handling with the `json` module
- Loops, conditionals, and input validation
- Lists and dictionaries

## How to Run
1. Install Python 3.12 or newer.
2. Run:
```
   python main.py
```

## Future Improvements
- Hash PINs instead of storing them as plain text
- Better error handling for invalid input
- Add a GUI or database

## Author
Ebad ur Rehman