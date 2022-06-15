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
