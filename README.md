<table>
<tr style="border: none">
<td style="border: none">

# THE Python Template Repository

</td>
<td align="right" style="border: none">
<img src="./img/scaleup.png" alt="Scaleup" height="100">
</td>
</tr>
</table>

This is a template repository for the Tel Hai Excellenteam (THE) Python course.

All exercises and submissions should follow the format of this repository. For your convenience, you can start each assignment by cloning this template.

## Grading and Conventions
Your assignment will be graded according to the following criteria. Please make sure your assignment follows the standards and conventions outlined below:

### Branching
Use the [CONTRIBUTING.md](CONTRIBUTING.md) file as your guideline for proper use of Git. For more information, you are encouraged to search online for "[GitHub Workflow Methodology](https://www.youtube.com/watch?v=U_IFGpJDbeU&ab_channel=DevOpsToolkit)."

### Environment
1. Use Python 3.10 as the interpreter.
2. At submission, ensure that the `requirements.txt` file is updated and contains all required packages for the application to run.

### Repository Structure
Please follow the guidelines in this section strictly.

<table>
<tr style="border: none">
<td style="border: none"><img src="./img/snakey_python.png" alt="Python Logo" width="70" height="70"></td>
<td style="border: none"><h4>Python Environment</h4></td>
</tr>
</table>

* The repository should include a `requirements.txt` file at the root directory.
  * Make sure that `requirements.txt` is up to date — it should contain **only** the dependencies that are actually used in the project. Missing or extra packages will negatively affect your grade.
* The repository **MUST NOT** include the `venv` directory.

#### GitHub Configuration
* The repository should include a `README.md` file at the root directory.
* The repository should include a `CONTRIBUTING.md` file at the root directory.
* You must have a `.gitignore` file, and there shouldn’t be any unnecessary files in the repository.
* 🚨 **CRITICAL:** Repositories without a workflow file at `.github/workflows/pylint.yml` will not be graded. :(
* You must have an `img` directory at the root directory.

#### Project's Files
* The repository should include a `main.py` file (this should be the entry point of the repository) at the root.
* The repository should include a `src` directory at the root.
  * All source files should be placed in the `src` directory.
* The repository should include a `test` directory at the root.
  * All tests should be placed in the `test` directory.

#### Project Tree
Project tree should match the following structure:

```bash
.
├── CONTRIBUTING.md
├── .git
│   ├── ...
├── .github
│   └── workflows
│       └── pylint.yml
├── .gitignore
├── img
│   ├── excellenteam.png
│   ├── scaleup.png
│   └── snakey_python.png
├── main.py
├── README.md
├── requirements.txt
├── src
│   ├── example.py
│   ├── ...
│   ├── ...
│   └── __pycache__
├── tests
│   ├── __pycache__
│   ├── ...
│   ├── ...
│   └── test_example.py
└── venv
    ├── bin
    ├── .gitignore
    ├── lib
    └── pyvenv.cfg
```
* `venv` directory should exist only on your local machine but not in the remote directory
* `...` notation stands for several files (might change from project to project, example files are just placeholders for examples)

## Don’ts
Please read this section carefully as there will not be any leniency when it comes to grading and undesired behavior.
1. You are not allowed to use GitHub Copilot, Cursor, or any other IDE-embedded LLM. All code that you submit must be written manually by you.
2. You are strongly discouraged (this means you should completely avoid) using ChatGPT or any other LLM to search for information, unless Google or other traditional search engines fail to provide what you need.
3. Do not copy under any circumstances. Students caught doing so will receive a `0` grade on all assignments (current, future, and past), regardless of previous grades.
4. The same applies to LLM usage mentioned in bullets `1` and `2`.
5. Submitting an empty assignment or leaving questions unanswered will result in a `20%` grade — simply for showing that you have a heartbeat and at least minimal care for the course and academic honesty.
6. The course staff reserves the right to conduct pop quizzes in case of suspicion of LLM misuse, plagiarism, or any other invalid behavior.

## How to Submit an Exercise
You are required to submit each exercise using "GitHub Classroom". To do this, you must upload a link to your "GitHub Classroom" repository via Moodle.

### Pre-submission Checkup
1. Make sure you've answered all the questions.
2. Review and refactor your code for better readability (ideally, review your code one or two days later — sometimes it's better to review with fresh eyes).
3. Ensure that all intended files are uploaded to Git and follow the structure convention outlined in the [Repository Structure](#repository-structure) section.
4. Ensure that your code is running.
5. Once you open a PR, review the changes **carefully**. You can leverage GitHub's built-in diff viewer.
6. Wait and confirm that the linter test completed successfully. If the linter test fails, assess the errors and refactor accordingly — otherwise, each error will negatively impact your grade.
7. Upload the repository link to Moodle.
8. Good luck :)

<!-- Center Excellenteam image -->
<p align="center">
  <img src="./img/excellenteam.png" alt="Excellenteam">
</p>
