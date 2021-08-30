def func(marks):
    if marks >= 700:
        scholarship = 3000
    elif marks >= 650 and marks <= 699:
        scholarship = 2500
    elif marks >= 600 and marks <= 649:
        scholarship = 2000
    else:
        scholarship = 0

    return scholarship

marks = int(input("Marks: "))

print(f"Scholarship is: Rs. {func(marks)}")