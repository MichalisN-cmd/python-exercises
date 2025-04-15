import pandas as pd


df = pd.read_excel("users.xlsx")


active_over30 = df[(df["Ylikia"] > 30) & (df["Energos"] == "Nai")]


avg_age = df["Ylikia"].mean()
avg_salary_active = df[df["Energos"] == "Nai"]["Misthos (€)"].mean()


print("Mesos oros ylikias:", round(avg_age, 2))
print("mesos misthos energon xriston:", round(avg_salary_active, 2))


active_over30.to_excel("active_users_over30.xlsx", index=False)
