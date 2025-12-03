# Lab Front Desk System 🩺

A simple command-line application that simulates a medical laboratory front desk:
patient check-in, test selection, billing with discounts and VAT, blood draw queue,
and a short satisfaction survey.

---

## 🧾 What this project does

This script models the basic workflow at a lab reception desk:

1. **Patient information**
   - Asks for patient first name and surname.
   - Greets the patient by first name.

2. **Test selection**
   - Shows a list of predefined lab tests:
     - CBC
     - Liver Function
     - Renal Function
     - Vitamin D
     - Thyroid Panel
     - Lipid Profile
   - Patient can select multiple tests at once.
   - Option to add more tests in a second step.

3. **Billing & discounts**
   - Calculates the total price before discount.
   - Applies a discount based on patient category:
     - General Patient (5%)
     - Hospital Staff (25%)
     - University Student (30%)
     - Senior Citizen (40%)
   - Calculates:
     - Total before discount
     - Total after discount (before VAT)
     - VAT (15%)
     - Final total price (after discount + VAT)

4. **Blood draw queue system**
   - Generates a random blood draw ticket number.
   - Assigns the patient to a random room:
     - Room 1 / Room 2 / Room 3 / Room 4

5. **Patient satisfaction survey**
   - Asks: *“How happy are you with the service? (1 is the least, 5 is the most)”*
   - Prints the rating and a thank-you message.

---

## 🛠 Tech & Python concepts used

- **Language:** Python
- **Core concepts:**
  - Lists and tuples
  - Loops
  - Input validation
  - Basic arithmetic & percentage calculations
  - Simple functions for modular code

This project was built to practice Python fundamentals on a realistic healthcare scenario.

---




