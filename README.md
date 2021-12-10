# Challenge_2
Challenge #2 for the UNCC FinTech Bootcamp due by 11:59pm on 12/12/21

---

# What's being created
We’ll apply software-engineering best practices to add new features and enhancements to the loan qualifier application. Specifically, we'll create a GitHub repository that includes all of the following files:

- The primary application file, `app.py`

- A data folder that contains the CSV file that the application uses

- A qualifier folder that contains all of the functions imported into the main app, organized into two subfolders:

  - filters, which includes .py files for all of your filter functions

utils, which includes your financial calculator module and your fileio module

A README.md file that explains the purpose of the project and how to use the code

A text file that shows your command history, demonstrating that you used version control best practices

As you move through the Challenge, keep in mind the user story and acceptance criteria that apply to each task.

User Story
As a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet.

Acceptance Criteria
Given that I’m using the loan qualifier CLI, when I run the qualifier, then the tool should prompt the user to save the results as a CSV file.

Given that no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.

Given that I have a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file.

Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.

Given that I’m using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.
# guidelines for creating README file:
---
 Project Title

Just after the title, introduce your project by describing attractively what the project is about and what is the main problem that inspires you to create this project or what is the main contribution for the potential user of your project.

---

## Technologies

This application is written in Python.

Python libraries used:

Fire: [https://github.com/google/python-fire](https://github.com/google/python-fire).

Python Fire is a library for automatically generating command line interfaces (CLIs) from a Python object.

Questionary: [https://questionary.readthedocs.io/en/stable/](https://questionary.readthedocs.io/en/stable/)

Questionary is a library that enables you to receive user input to CLI questions.



---

## Installation Guide

prior to running these libraries, install them from the command line:
```python
pip install fire
pip install questionary
```

---

## Usage

This section should include screenshots, code blocks, or animations explaining how to use your project.

*This clip shows the results for the first part of the program in the CLI:*

![Sample of first part of program execution](./images/01_results_of_execution_part_1.png)
---

## Contributors

Geoff Tarleton - jobeycat@protonmail.com

---

## License

MIT
