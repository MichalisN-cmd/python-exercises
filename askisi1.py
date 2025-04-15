grades = []

for i in range(5):
    while True:
        try:
            grade = float(input(f"isagete arithmo {i+1} (0-100): "))
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("O vathmos prepi na ine apo 0 mexri 100.")
        except ValueError:
            print("Isagete engiro arithmo.")


average = sum(grades) / len(grades)
max_grade = max(grades)
min_grade = min(grades)


print(f"\nMesos oros: {average:.2f}")
print(f"Megaliteros vathmos: {max_grade}")
print(f"mikroteros vathmos : {min_grade}")
