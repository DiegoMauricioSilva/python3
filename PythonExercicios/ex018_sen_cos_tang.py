import math

ang = float(input('Digite o ângulo que você deseja: '))

ang_rad = math.radians(ang)

sen = math.sin(ang_rad)
cos = math.cos(ang_rad)
tan = math.tan(ang_rad)

print(f' O ângulo de {ang} tem SENO de {sen:.3f}')
print(f' O ângulo de {ang} tem COSSENO de {cos:.3f}')
print(f' O ângulo de {ang} tem TANGENTE de {tan:.3f}')
