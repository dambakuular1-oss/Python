st = {'18', '24', '34', '47', '81', '63'}
tst1 = '34'
tst2 = ('81', '12', '46')

r_tst1 = tst1 in st
print(r_tst1)

all_in = all(item in st for item in tst2)
print(all_in)
