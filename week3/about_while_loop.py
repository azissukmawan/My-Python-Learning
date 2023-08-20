x = 1
sum = 0

while x < 10:
    sum += x 
    print("x ", str(x))
    x += 1

 # x = 1 --> inisialisasi dulu bila while loop kedua bisa berguna
product = 1
while x < 10:
    product *= x
    print("x", str(x))
    x += 1

print("this sum ", str(sum), ", this product ", str(product))
# hasil tersebut berbeda karena pada while loop kedua tidak akan di generate
# karena inisalisasi x sudah di pakai di loop pertama jadi nila x di loop kedua sudah 10
# alternatif bisa inisialisasi ulang x nya dengan nilai baru dari awal


print('\nInfinite loop')

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1 # tambahkan inisialisasi

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
