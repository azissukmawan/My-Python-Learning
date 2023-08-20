print('==== deret angka 1-5 ====')

for x in range(5):
    print(x)

print('==== example ====')
sum = 0
length = 0

for x in range(10):
    sum += x
    length += 1

print('this sum is: ', str(sum), ' - average is: ', str(sum/length))


print('\n==== Memunculkan data di dalam deret list ====')

orangTangerang= ['Azis', 'Udin', 'Ucup', 'Aceng']

for x in orangTangerang:
    print('hallo ', str(x))

print('==== example ====')
# menghitung deret angka 
number = (5,6,7,8,9,10)

sum = 0
length = 0
for x in  number:
    sum += x
    length += 1

print('this sum is: ', str(sum), ' - average is: ', str(sum/length))

print('\n==== about fungsi range ====')

# range(start, stop, increment)

for x in range(2, 10, 2):
    print(x)


for x in range(2, 10+1, 2):
    print('\n', str(x))


for x in range(10, 0, -1):
    print('\n', str(x))


for x in range(2, -2, -1):
    print('\n', str(x))

print('\n==== nested loop ====')

for left in range(7):
    for right in range(left, 7):
        print('[ ' + str(left) + ' | ' + str(right) + ' ]', end=" ")
    print()
    

print('\n==== example another neted loop====')
club = ['Liverpool', 'MU', 'PSG', 'Barcelona', 'Real madrid', 'Arsenal']

for team_a in club:
    for team_b in club:
        if (team_a != team_b):
            print(team_a, " vs ", team_b)


print('\nFor loops in iterable string')

def helloName(name):
    for x in name:
        print('hello ', x)

helloName("azis")