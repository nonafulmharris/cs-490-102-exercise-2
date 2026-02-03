# Source Code Management Exercise

## Objective

In this exercise, you will demonstrate your understanding of Git and GitHub by forking this repository, adding a Python function, and submitting a pull request. You will write a function to calculate the Greatest Common Divisor (GCD) of two integers using the **Euclidean algorithm** and follow a precise workflow to manage your source code.

## Instructions

### Step 1: Fork the Repository

- Fork this repository to your own GitHub account by clicking the **Fork** button in the upper right corner. _Note_ if you change the name of your repository, then you will need to use your repo name instead of `cs-490-102-exercise-2` when following the examples below.

### Step 2: Clone Your Fork

- Clone the forked repository to your local machine. Open your terminal and run the following command:
  ```bash
  git clone https://github.com/<your-github-username>/cs-490-102-exercise-2.git
  ```

### Step 3: Create a New Branch

- Create a new branch to work on your feature. Name your branch `<ucid>-gcd-feature` where <ucid> is your student ucid (`wfm8`). Example commands:
  ```bash
  cd cs-490-102-exercise-2
  git checkout -b <ucid>-gcd-feature
  ```

### Step 4: Create Your Submission File

- Inside the `students_submissions/` directory, create a new Python file named `gcd_<ucid>.py`. Replace `<ucid>` with your student ucid.
  - Example: If your ucid is `wfm8`, name your file `gcd_wfm8.py`.

### Step 5: Implement the `gcd` Function

- In your `gcd_<ucid>.py` file, a greatest common divisor function. Use this exact function signature: `def gcd(a: int, b: int) -> int:`. DO NOT USE LOOPS in your function. Be sure to consider edge cases, like prime numbers, negative numbers, etc. Have errors print an informative message and return `None`.

  ```python
  def gcd(a: int, b: int) -> int:
      """
      Calculate the greatest common divisor (GCD) of two integers a and b
      using the Euclidean algorithm.
      """
      # Implement your solution here
      pass
  ```

- Test your function with some basic test cases inside your file. You can use `print` statements to verify your implementation.

Example:

```python
def gcd(a: int, b: int) -> int:
    # This uses a loop, so DO NOT COPY AND PASTE this example
    while b:
        a, b = b, a % b
    return a

# Test cases
print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
```

### Step 6: Commit Your Changes

- Once your function is implemented, stage and commit your changes:
  ```bash
  git add students_submissions/gcd_<ucid>.py
  git commit -m "Implemented GCD function"
  ```

### Step 7: Push the Branch to GitHub

- Push your changes to the `<ucid>-gcd-feature` branch in your forked repository:
  ```bash
  git push origin <ucid>-gcd-feature
  ```

### Step 8: Create a Pull Request

- Go to your forked repository on GitHub and click the **Compare & pull request** button.
- Make sure to select your `<ucid>-gcd-feature` branch as the source and the original repository’s `main` branch as the destination.
- Submit the pull request.

When choosing repositories and branches, the GitHub screen will look something like:

```
base repository: [njit-prof-bill/cs-490-102-exercise-2][base: main] <- [head repository: iambillmccann/cs-490-102-exercise-2][compare: wfm8-gdc-feature]
```

---

## Naming Conventions

To ensure your submission is automatically checked, you must follow these naming conventions:

1. Your Python file must be placed in the `students_submissions/` directory.
2. The file must be named `gcd_<ucid>.py`, where `<ucid>` is your actual GitHub username (e.g., `gcd_wfm8.py`).
3. Your file must contain a function named `gcd(a: int, b: int) -> int`.

If you do not follow these conventions, your submission will not be automatically tested, and you may be asked to resubmit.

---

## Grading Rubric

On point for each of the following:

- Repo cloned and branched
- Create PR that will merge automatically
- Function has no loops
- Code passes basic tests
- Code passes edge cases

---

## Submission Deadline

- Your pull request must be submitted by Sunday mm/dd/2026 at 11:59.

---

### Notes:

- If you encounter any issues, feel free to reach out for help.
- Remember to test your function with a variety of inputs to ensure it works correctly.
- Follow the naming conventions carefully to avoid any issues with the automatic testing.

---
