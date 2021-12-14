import math

ab = int(input())
bc = int(input())
ac = (ab ** 2 + bc ** 2) ** (1 / 2)
new_ac = math.sqrt((ab ** 2 + bc ** 2))
mc = ac / 2
angle_a = math.asin(bc / ac)
angle_c = 1.5708 - angle_a
bm = (((bc ** 2) + (mc ** 2) - (2 * bc * mc * math.cos(angle_c)))) ** (1/2)
angle_b = math.asin(mc * math.sin(angle_c) / bm)
angle_deg = str(round(math.degrees(angle_b)))

print(f"{angle_deg}\u00b0")
