valid_emails = []


print("Isagete 5 email adresses:")

for i in range(5):
    email = input(f"Email {i+1}: ").strip()
    
    
    if "@" in email and (email.endswith(".com") or email.endswith(".gr") or email.endswith(".cy")):
        print(f"✅ Το email \"{email}\" is valid.")
        valid_emails.append(email)
    else:
        print(f"❌ Το email \"{email}\" is NOT valid.")


with open("valid_emails.txt", "w", encoding="utf-8") as file:
    for email in valid_emails:
        file.write(email + "\n")

print("\nTa emails apothikeftikan sto arxio valid_emails.txt.")
