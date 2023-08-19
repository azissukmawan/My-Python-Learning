name1 = 'Azis'
name2 = 'azis'
print(name1 == name2)
# kenapa false ? karena python case sensitive

name_rev = 'Azis'
print(name_rev == name_rev)
# true karena perbandingan huruf sama sama case

print('\nPerbandingan lebih dari dan kurang dari pada string')
# katakan lah disini ucup dan udin memiliki nilai hobi
ucup = 'Bergulat'
udin = 'Mengaji'
print(ucup > udin)
# hasilnya false karena deret huruf b lebih awal dari huruf m

she = 'siti'
he = 'Subarjo'
print(she > he)
# disini menghasilkan nilai true karena huruf non kapital ada di deret setelah z kapital

print('\nLogika operator')
number1 = 250
number2 = 200
result = number1 == (number2 + 50)
print(not result) # operator not akan mengembalikan false jika kondisi itu benar
# sebaliknya jika kondisi itu false maka operator not akan menghasilkan true
result2 = 20 == 25
print(not result2)


print('\nBranch if else statment')
def user(username):
    if len(username) < 10: # len disini untuk menghitung jumlah karakter huruf
        print('Username tidak boleh kurang dari 10')
    else:
        print('username valid')
    # atau bisa juga tanpa else ketika menggunakan return
    #print('username valid')

user('Abdul Azis Sukmawan')

def angkaGenap(x):
    if x % 2 == 0:
        return 'angka genap'
    return 'angka ganjil'

print(angkaGenap(10))


print('\nelif statement')

def password(pw):
    if len(pw) < 3:
        return 'pw tidak boleh kurang dari 3 karakter'
    elif len(pw) > 10:
        return 'pw tidak boleh lebih dari 10 karakter'
    return 'pw valid'

print(password('azis123'))