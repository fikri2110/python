'''membuat fungsi dengan return'''

'''
rumus p = V * I
'''
def kalkulasi_P(voltase,arus):
    output = voltase * arus
    return output

pemakaian1 = kalkulasi_P(220,4)
pemakaian2 = kalkulasi_P(220,1.5)
pemakaian3 = kalkulasi_P(220,2.5)
pemakaian4 = kalkulasi_P(220,3)

print(f"pemakaian 1 = {pemakaian1}")
print(f"pemakaian 2 = {pemakaian2}")
print(f"pemakaian 3 = {pemakaian3}")
print(f"pemakaian 4 = {pemakaian4}")