""" Напишите программу для. проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
для всех значений предикат.  """


xyz = ["X", "Y", "Z"]
numb = []
for i in xyz:
    numb.append(int(input(f"введите {i} :")))

left = not (numb[0] or numb[1] or numb[2])
right = not numb[0] and not numb[1] and not numb[2]
result = left == right

if result == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")
