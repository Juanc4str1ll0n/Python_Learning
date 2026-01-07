#Hacer un programa que dado un vector de 10 numeros determine el mayor y el menor

nums = []
for i in range(1, 11):
    num = int(input(f"Ingrese el numero {i} "))
    nums.append(num)
    
# mayor
mayor = 0
for num in nums:
    if num > mayor:
        mayor = num

print(mayor)

# menor
menor = nums[0]
for num in nums:
    if num < menor:
        menor = num

print(menor)