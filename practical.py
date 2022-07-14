#q1 
def swap():
    a = int(input("first num: "))
    b = int(input("second num: "))
    print(f"initial values: a={a}, b={b}")
    a = a + b
    b = a - b
    a = -(b - a)
    print(f"swapped values: a={a}, b={b}")

#q2
def sales():
    q1 = int(input("first quarter: "))
    q2 = int(input("second quarter: "))
    q3 = int(input("third quarter: "))
    q4 = int(input("fourth quarter: "))
    tsales = q1 + q2 + q3 + q4
    commission = 0
    com_stat = "no commission"
    if tsales >= 250000:
        commission = (7 * tsales) / 100
        com_stat = "7 %"
    elif 100000 <= tsales < 250000:
        commission = (5 * tsales) / 100
        com_stat = "5 %"
    elif 50000 <= tsales < 100000:
        commission = (2 * tsales) / 100
        com_stat = "2 %"
    print(f"total sales: {tsales}\ncommission given: {com_stat}\ntotal commission: {commission}")

#q3
def marks():
    m1 = int(input("first sub marks: "))
    m2 = int(input("second sub marks: "))
    m3 = int(input("third sub marks: "))
    m4 = int(input("fourth sub marks: "))
    m5 = int(input("fifth sub marks: "))
    percent = (m1 + m2 + m3 + m4 + m5) / 5
    grade = 'A'
    if percent >= 95:
        grade = 'A'
    elif 90 <= percent < 95:
        grade = 'A-'
    elif 80 <= percent < 95:
        grade = 'B'
    elif 70 <= percent < 80:
        grade = 'C'
    elif 60 <= percent < 70:
        grade = 'D'
    else:
        grade = 'F'
    print(f"percentage: {percent}\nGrade: {grade}")

marks()
