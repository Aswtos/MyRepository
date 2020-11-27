import math
a1 = float(input('a1 = '))
a2 = float(input('a2 = '))
b1 = float(input('b1 = '))
b2 = float(input('b2 = '))
costh = (a1*b1 + a2*b2)/(math.sqrt(math.pow(a1, 2) + math.pow(a2, 2)) * math.sqrt(math.pow(b1, 2) + math.pow(b2, 2)))
goniath = math.degrees(math.atan(a2/a1) - math.atan(b2/b1))
print('το συνημιτονο της γωνιας θ ειναι: ', costh, ' και η γωνια θ ειναι: ', goniath, ' μοιρες')