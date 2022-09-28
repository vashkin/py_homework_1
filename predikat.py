""" Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат.  """


xyz = ["X", "Y", "Z"]
received_number = []
for i in xyz:
    received_number.append(int(input(f"введите {i} :")))

left = not (received_number[0] or received_number[1] or received_number[2])
right = not received_number[0] and not received_number[1] and not received_number[2]
result = left == right

if result:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")
