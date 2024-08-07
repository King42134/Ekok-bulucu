def ebob(a, b):
    while b:
        a, b = b, a % b
    return a

def ekok(a, b):
    return (a * b) // ebob(a, b)

print("Ilk sayiyi giriniz:")
y = int(input())
print("Ikinci sayiyi giriniz:")
x = int(input())

print("Ekok:", ekok(y, x))
