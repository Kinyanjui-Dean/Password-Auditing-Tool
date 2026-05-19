from Checker import check_password
from Generator import generate_password

def main():
    print("=== Password Strength Tool ===")

    password = input("Enter password: ")

    strength, feedback, entropy = check_password(password)

    print(f"\nStrength: {strength}")
    print(f"Entropy: {entropy} bits")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("-", f)

    if strength == "Weak":
        print("\nSuggested Password:")
        print(generate_password())

if __name__ == "__main__":
    main()