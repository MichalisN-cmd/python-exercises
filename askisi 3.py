import pandas as pd

# Διαβάζουμε το αρχείο
df = pd.read_excel("users.xlsx")

# Φιλτράρουμε τους ενεργούς χρήστες άνω των 30
active_over30 = df[(df["Ηλικία"] > 30) & (df["Ενεργός"] == "Ναι")]

# Υπολογισμοί
avg_age = df["Ηλικία"].mean()
avg_salary_active = df[df["Ενεργός"] == "Ναι"]["Μισθός (€)"].mean()

# Εμφάνιση
print("Μέσος όρος ηλικίας:", round(avg_age, 2))
print("Μέσος μισθός ενεργών χρηστών:", round(avg_salary_active, 2))

# Αποθήκευση νέου αρχείου
active_over30.to_excel("active_users_over30.xlsx", index=False)
