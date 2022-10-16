# Треугольник ли?
# Напишите функцию для определения возможности построения
# треугольника на основании длин трех его потенциальных сторон.

def tringle_def(a, b, c):
    if a <= 0 and b <= 0 and c <= 0:
        return False
    else:
        if a >= b + c or b >= a + c or c >= a + b:
            return False
        else:
            return True


a = float(input('Enter first side of tringle: '))
b = float(input('Enter second side of tringle: '))
c = float(input('Enter third side of tringle: '))

print(tringle_def(a, b, c))
