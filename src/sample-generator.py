import random

n = int(input("\nMasukkan panjang sequence DNA yang: "))
sequence = ''.join(random.choices('ACGT', k=n))


print(f"\nContoh input -> DNA-sample-1/seq-{n}.txt")
filename = input("masukkan path dan nama file untuk menyimpan sequence: ")
with open(f'../test/{filename}', 'w') as f:
  f.write(sequence)