# Challenge_2
Challenge #2 for the UNCC FinTech Bootcamp due by 11:59pm on 12/12/21

---

## What's being created
This is an update to the Loan Qualifier app that now includes the ability to save a list of qualifying loans to a CSV file. 

This GitHub repository includes all of the following files:

- The primary application file, `app.py`

- A data folder that contains the CSV file that the application uses

- A qualifier folder that contains all of the functions imported into the main app, organized into two subfolders:

  - `filters`, which includes .py files for all of your filter functions

  - `utils`, which includes your financial calculator module and your fileio module


### User Story
"As a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet."

### Acceptance Criteria
  - Given that I’m using the loan qualifier CLI, when I run the qualifier, then the tool should prompt the user to save the results as a CSV file.

  - Given that no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.

  - Given that I have a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file.

  - Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.

  - Given that I’m using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

---


## Technologies

This application is written in Python.

Python libraries used:

  - Fire: [https://github.com/google/python-fire](https://github.com/google/python-fire).

    Python Fire is a library for automatically generating command line interfaces (CLIs) from a Python object.

  - Questionary: [https://questionary.readthedocs.io/en/stable/](https://questionary.readthedocs.io/en/stable/)

    Questionary is a library that enables you to receive user input to CLI questions.

  - Pathlib: [https://docs.python.org/3.7/library/pathlib.html](https://docs.python.org/3.7/library/pathlib.html)

    Pathlib is a library that enables consistent input and output of files from the main app.


---

## Installation Guide

prior to running these libraries, install them from the command line:
```python
pip install fire
pip install questionary
```

---

## Usage


*This clip shows the results for the first part of the program in the CLI:*

![Sample of first part of program execution](./images/01_results_of_execution_part_1.png)



*After the addition of a new save_csv function, the user now has the ability to save a list of qualifying loans, such as this:*

![Saved loans](./images/02_saved_loans.png)
---

## Contributors

Geoff Tarleton - jobeycat@protonmail.com

adapted from Starter Code supplied by UNCC FinTech Online Bootcamp by Trilogy Educational Services, a 2U, Inc. brand.

---

## License

MIT
