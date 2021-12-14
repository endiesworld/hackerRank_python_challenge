import math

ab = int(input())
bc = int(input())
ac = (ab ** 2 + bc ** 2) ** (1 / 2)
mc = ac / 2
# bm = (bc ** 2 - mc ** 2) ** (1/2)
angle_r = math.asin(mc / bc)
angle_deg = round(math.degrees(angle_r))
print(angle_deg)
