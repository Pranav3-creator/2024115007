# DASS Assignment 2 – Software Testing

**Name:** Muvvala Pranav  
**Roll Number:** 2024115007  

---

## 📌 Overview

This assignment covers three major types of testing:

1. **White Box Testing** – Analysis and testing of MoneyPoly code  
2. **Integration Testing** – StreetRace Manager modular system  
3. **Black Box Testing** – QuickCart API testing using HTTP requests  

---

# 🟦 1. White Box Testing (MoneyPoly)

## 📂 Location

whitebox/
code/
tests/
diagrams/


## ▶️ How to Run Code

```bash
python whitebox/code/main.py
🧪 How to Run Tests
pytest whitebox/tests
🔍 What Was Done
Control Flow Graph (CFG) created for play_turn()
Code analyzed using pylint and improved iteratively
White-box test cases implemented using pytest
Logical bugs identified and fixed with commits
🟦 2. Integration Testing (StreetRace Manager)
📂 Location
integration/
  code/
  tests/
  diagrams/
▶How to Run Code
python integration/code/main.py
🧪 How to Run Tests
pytest integration/tests
🔍 What Was Done
Implemented required modules:
Registration
Crew Management
Inventory
Race Management
Results
Mission Planning
Added additional modules:
Vehicle Maintenance
Leaderboard
Integration test cases written to validate module interactions
Call Graph created to show system flow
Multiple integration-level validation errors identified and fixed
🟦 3. Black Box Testing (QuickCart API)
📂 Location
blackbox/
  tests/
⚙️ Requirements
Python
requests
pytest

Install dependencies:

pip install requests pytest
▶️ Run API Server

Make sure the QuickCart API is running locally:

docker-compose up

OR run backend manually (if provided).

🧪 How to Run Tests
pytest blackbox/tests
🔍 What Was Done
Designed ~30 black-box test cases
Covered:
Valid inputs
Invalid inputs
Missing fields
Boundary conditions
Robustness scenarios
Identified multiple issues related to:
Input validation
Type handling
Header validation
Data constraints
🟦 📊 Tools Used
Python
pytest
requests
pylint
Git & GitHub
🟦 📌 Notes
All testing was performed according to assignment requirements
Proper commit history maintained for iterative development
Reports for each part are included in respective folders
🟦 🚀 Conclusion

This assignment demonstrates the application of:

White-box testing for internal logic validation
Integration testing for module interaction verification
Black-box testing for API validation without code access
https://github.com/Pranav3-creator/2024115007/tree/main
