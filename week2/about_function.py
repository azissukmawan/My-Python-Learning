def hallo(name):
    print("Hallo ", name)

myName = hallo('azis')
print(myName) # this result is none because not return value another when initialize in variabel 

print('\nWith return value')
def convert_second(second):
    hours = second // 3600
    minutes = (second - hours * 3600) // 60
    remaining_second = second - hours * 3600 - minutes * 60
    return hours, minutes, remaining_second
    
result = convert_second(5000)
print(result) # sedangkan ini mencetak tuple secara keseluruhan
x, z, y = convert_second(5000)
print(x, y, z) # hasil tersebut memisahkan data di dalem tuple