# Lab Front Desk System: Patient Info + Billing + Discount + VAT + Blood Draw + Survey

import random

# Available laboratory tests and prices
tests = [
    ("CBC", 80),
    ("Liver Function", 150),
    ("Renal Function", 140),
    ("Vitamin D", 200),
    ("Thyroid Panel", 180),
    ("Lipid Profile", 160),
]

# Discount categories based on patient type
discount_categories = [
    ("General Patient", 5),
    ("Hospital Staff", 25),
    ("University Student", 30),
    ("Senior Citizen", 40),
]

# Blood draw rooms available
blood_draw_rooms = ["Room 1", "Room 2", "Room 3", "Room 4"]


def show_tests():
    """Display available lab tests."""
    print("\nAvailable lab tests:")
    for i, t in enumerate(tests):
        name, price = t
        print(f"{i + 1}. {name} - {price} SAR")


def parse_selection(raw):
    """Parse test selections entered by user."""
    parts = raw.replace(",", " ").split()
    indices = []
    for part in parts:
        if not part.isdigit():
            continue
        num = int(part)
        if 1 <= num <= len(tests):
            indices.append(num - 1)
    return indices


def choose_discount_category():
    """Ask user to choose patient category for discount."""
    print("\nPatient Category:")
    for i, (name, percent) in enumerate(discount_categories):
        print(f"{i + 1}. {name} ({percent}% discount)")

    while True:
        choice = input("Choose category number: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(discount_categories):
                return discount_categories[idx - 1]
        print("Please enter a number from 1 to 4.")


def ask_yes_no(prompt):
    """Reusable yes/no question."""
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please enter y or n.")


def main():
    print("=== Lab Front Desk System ===")

    # 1) Patient info
    first_name = input("Patient first name: ").strip()
    surname = input("Patient surname: ").strip()
    full_name = f"{first_name} {surname}".strip()

    print(f"\nWelcome, {first_name}.")

    all_selected_indices = []

    # 2) First test selection (mandatory)
    while True:
        show_tests()
        raw = input("\nEnter test numbers (comma or space separated): ").strip()
        indices = parse_selection(raw)
        if indices:
            all_selected_indices.extend(indices)
            break
        print("No valid tests selected, try again.")

    # Optional second test selection
    if ask_yes_no("Do you want to add more tests?"):
        while True:
            show_tests()
            raw = input("\nEnter additional test numbers: ").strip()
            indices = parse_selection(raw)
            if indices:
                all_selected_indices.extend(indices)
                break
            print("No valid tests selected, try again.")

    # 3) Build selection list
    selected_tests = [tests[i] for i in all_selected_indices]

    total_before = sum(price for (name, price) in selected_tests)

    # Simple summary before category
    print("\nSelected tests:")
    for name, price in selected_tests:
        # Format: CBC 80
        print(f"{name} {price}")

    print(f"\nTotal {total_before} before discount")

    # 4) Patient category / discount
    category_name, discount_percent = choose_discount_category()

    # 5) Apply discount & VAT
    discount_amount = total_before * (discount_percent / 100)
    total_after_discount = total_before - discount_amount

    vat_percent = 15
    vat_amount = total_after_discount * vat_percent / 100
    final_total = total_after_discount + vat_amount

    # 6) Blood draw ticket and room assignment
    ticket_number = random.randint(100, 999)
    room = random.choice(blood_draw_rooms)

    # 7) Final invoice
    print("\n=== Final Invoice ===")
    print(f"Patient: {full_name}")
    print(f"Category: {category_name} ({discount_percent}% discount)")

    print("\nTests chosen:")
    for name, price in selected_tests:
        print(f"- {name}: {price} SAR")

    print(f"\nTotal before discount: {total_before:.2f} SAR")
    print(f"Total after discount (before VAT): {total_after_discount:.2f} SAR")
    print(f"VAT ({vat_percent}%): {vat_amount:.2f} SAR")
    print(f"Total after discount including VAT: {final_total:.2f} SAR")

    print("\nBlood draw ticket number:", ticket_number)
    print("Room to proceed to:", room)

    print("\n💚 We wish you good health. Take care of yourself. 💚")

    # 8) Service rating – LAST thing
    print("\nHow happy are you with the service? (1 is the least, 5 is the most)")
    rating = input("Enter your rating (1-5): ").strip()
    print(f"Your rating: {rating}/5")

    print("\n📝 Thank you for completing the survey.")
    print("We continuously improve our services to serve you better.")
    print("Thank you for choosing our lab! 💚\n")


if __name__ == "__main__":
    main()
