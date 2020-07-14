import lenses

round_amount = 3

f1 = 10
f2 = 15
f3 = 30

s1 = 30
f2_diff = 45
f3_diff = 35

y1 = 5

s1p = lenses.image_distance(s1, f1)
s2 = f2_diff - s1p
s2p = lenses.image_distance(s2, f2)
s3 = f3_diff - s2p
s3p = lenses.image_distance(s3, f3)

print(round(s1p, round_amount), round(s2p, round_amount), round(s3p, round_amount))


y1p = lenses.image_height(y1, s1, s1p)
y2 = y1p
y2p = lenses.image_height(y2, s2, s2p)
y3 = y2p
y3p = lenses.image_height(y3, s3, s3p)


print(round(y2, round_amount), round(y3, round_amount), round(y3p, round_amount))