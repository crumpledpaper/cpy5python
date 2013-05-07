carplate = input('Enter mystery carplate: ')
deleted = ''
if carplate[2].isalpha():
    deleted = carplate[0]
    carplate = carplate[1:]
check_map = {'A':0,'Y':1,'U':2,'S':3,'P':4,'L':5,'J':6,'G':7,'D':8,'B':9,
             'Z':10,'X':11,'T':12,'R':13,'M':14,'K':15,'H':16,'E':17,'C':18}
weights = [14,2,12,2,11,1]
sum_products = 0
sum_products += (ord(carplate[0])-ord('A')+1) * weights[0]
sum_products += (ord(carplate[1])-ord('A')+1) * weights[1]
for i in range(2,6):
    if carplate[i].isdigit():
        sum_products += int(carplate[i])* weights[i]
    else:
        mystery_position = i
remainder = sum_products % 19
final_remainder = check_map[carplate[-1]]
mystery = (final_remainder-remainder)%19
carplate = deleted + carplate[:mystery_position]+\
           str(mystery) + carplate[mystery_position+1:]
print(mystery,carplate)
