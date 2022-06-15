Car_num_list=[1235,1232,1434,6435,2345,3456,2532,1435,1256,8654,3452,4634,2345,2341,2435,2353,2323,8532,6434,6543]
list2=[42352,12523,34554,25435,23453,45654,23463,76456,23464,34623,32345,32346,23463,34632,34654,23754,65346,24634,125389,167283]

def input_car(car_num):  #차번호 입력 받기(4자리 아니면 다시 입력 받기 위한 함수)
    if 1000<=car_num<=9999:
        return car_num
    else: #차번호  자릿수 틀리면 다시
        print("Car number should be four numbers. Please input your car number again")
        car_num= int(input('Car number : '))
        return input_car(car_num)
num=int(input('Car number : '))
input_car(num)

def input_mill(mill):  #mill 입력받기 (음수이면 다시 입력 받기위한 함수)
    if mill>=0:
        return mill
    else:  #마일리지 -안나오게
        print("Please input mileage again")
        mill= int(input('Mileage : '))
        return input_mill(mill)
mileage= int(input('Mileage : '))
input_mill(mileage)




#'Air Cleaner', 'Ignition Plug', 'Coolant', 'Fuel Filter', 'Drive Belt', 'Transmission', 'Tires', 'Timing Belt', 'Battery','Clutch Disk

repair=[0,0,0,0,0,0,0,0,0,0]

Car_num_list.sort()   #리스트 정렬

def binary_search(array,target,start,end):  #이진 탐색 함수
        if start>end:
            return False
        else:
            mid = (start+end) // 2
            if array[mid] == target:
                return True
            elif array[mid] > target:
                return binary_search(array,target,start,mid-1)
            else:
                return binary_search(array,target,mid+1,end)
        
start = Car_num_list[0]
end = Car_num_list[int(len(Car_num_list)-1)]
target = num  #입력 받은 차 번호
array = Car_num_list
n=len(Car_num_list)

result = binary_search(array,target,0,n-1)






if result == False:#신규고객
    print('Welcome!')
    d_mileage=mileage

    def re_repair(num):
        for i in range(num+1):
            repair[i]=1
 
    if 80000<=d_mileage:
        print("You need to replace 'Air Cleaner', 'Ignition Plug', 'Coolant', 'Fuel Filter', 'Drive Belt', 'Transmission', 'Tires', 'Timing Belt', 'Battery','Clutch Disk'")
        re_repair(9)
    elif 60000 <= d_mileage:
        print("You need to replace 'Air Cleaner', 'Ignition Plug', 'Coolant', 'Fuel Filter', 'Drive Belt', 'Transmission', 'Tires', 'Timing Belt', 'Battery'")
        re_repair(8)                 #repair[0:8]=1
    elif 50000 <= d_mileage:
        print("You need to replace 'Air Cleaner', 'Ignition Plug', 'Coolant', 'Fuel Filter', 'Drive Belt', 'Transmission', 'Tires'")
        re_repair(6)  
    elif 30000 <= d_mileage:
        print("You need to replace 'Air Cleaner', 'Ignition Plug', 'Coolant', 'Fuel Filter', 'Drive Belt', 'Transmission'")
        re_repair(5)
    elif 20000 <= d_mileage:
        print("You need to replace the 'Air Cleaner', 'Ignition Plug', 'Coolant', 'Fuel Filter', 'Drive Belt'")
        re_repair(4)
    elif 15000 <= d_mileage :
        print("You need to replace the 'Air Cleaner', 'Ignition Plug'")
        re_repair(1)    
    elif 4000 <= d_mileage :
        print("You need to replace the 'Air Cleaner'")
        repair[0]=1    
    elif 0 <= d_mileage:
        print("You don't have to replace anything Bye")
        sys.exit(0)
    else:
        print("input again please")

else:    #기존 고객
    print('Hi Let me show your previous record',end='\n\n\n')
    
    car=open('car_record.txt')
    for i in range(len(Car_num_list)):
        list1=car.readline()
        list2=list1.split()
        if int(list2[0])==num:
            index=i
            break
        else:
            continue
    #텍스트 파일 list로 저장해서 이전 마일리지값 불러내기
    pre_mil=int(list2[1])
    print('pre_mil: {}, Air Cleaner: {},Ignition Plug: {}, Coolant: {}, Fuel Filter: {},Drive Belt: {}, Transmission: {},Tires: {}, Timing Belt: {},Battery: {},Clutch Disk: {}'.format(list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[8],list2[9],list2[10],list2[11]))
    for i in range(12):
        list2[i]=int(list2[i])
    repaircri=[4000,15000,20000,20000,20000,30000,50000,60000,60000,80000]
    component=['Air Cleaner', 'Ignition Plug', 'Coolant', 'Fuel Filter', 'Drive Belt', 'Transmission', 'Tires', 'Timing Belt', 'Battery','Clutch Disk']
    num=0
    for i in range(10):
        if mileage-list2[i+2]*repaircri[i]>=repaircri[i]:
            num=num+1
    if num>0:
        print("->You need to replace ",end='')
        for i in range(10):
            if mileage-list2[i+2]*repaircri[i]>=repaircri[i]:
                print(component[i],end=' ')
                repair[i]=1
    else:
        print("You don't have to replace anything Bye")
        sys.exit(0)
    print()
    
    
    
def choice_repair_shop(num1,num2,num):
    if repair[num1]==1 or repair[num2]==1:
        repair_shop[num]=1
    
repair_shop=[0,0,0,0,0]  #정비소 초기 리스트,가야하는 정비소는 1로 표시

choice_repair_shop(1,9,0)
choice_repair_shop(2,7,1)
choice_repair_shop(3,8,2)
choice_repair_shop(4,0,3)
choice_repair_shop(5,6,4)
    
print()
print('You should visit ',end='')

for i in range(5):
    repair_sh=['A','B','C','D','E']
    if repair_shop[i]==1:
        print(repair_sh[i],end=' ')
print(" repair shop" ,end='\n\n')


def input_score(score,crit):
    
    if 1<=score<=3:
        return score
    else:
        print ("Please input score from 1 to 3")
        score=int(input("Score the importantance of {} (1~3)".format(crit)))
        return input_score(score,crit)
print('Let me recommend repair shop for each part! Input the score please.')
a=int(input("Score the importantance of professionality (1~3)"))
input_score(a,'professionality')
b=int(input("Score the importantance of price (1~3)"))
input_score(b,'price')
c=int(input("Score the importantance of distance (1~3)"))
input_score(c,'distance')

list_score = [a,b,c]  #고객이 생각하는 중요도(입력받은 값임)

