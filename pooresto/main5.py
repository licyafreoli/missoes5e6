# number = int(input('número: '))

# if number >= 1:
#      for i in range(1, 31):
#         if number % i != 0:
#             print(number, 'é primo')
#         else:
#             print(number, 'não é primo')
#             break
# elif number == 0:
#     print(number, 'é zero')
# else:
#     print(number, 'é negativo')

def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

intervalo = range(10, 31)

primos = []

for num in intervalo:
    if primo(num):
        primos.append(num)
print("Números primos entre 10 e 30:", primos)
