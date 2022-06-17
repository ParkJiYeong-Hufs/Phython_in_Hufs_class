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

import numpy
list1 = [[[5,2,3],[1,5,4],[4,2,3]],[[4,2,3],[2,5,2],[2,3,5]],[[5,3,1],[3,4,3],[3,2,5]],[[4,3,3],[2,5,3],[3,3,4]],[[5,3,1],[3,4,2],[4,2,4]]]
#부품 고정값 가져오기 A1=[5,2,3],A2=[1,5,4],A3=[4,2,3],B1=[4,2,3],B2=[2,5,2],B3=[2,3,5],C1=[5,3,1],C2=[3,4,3],C3=[3,2,5]
#D1=[4,3,3],D2=[2,5,3],D3=[3,3,4],E1=[5,3,1],E2=[3,4,2],E3=[4,2,4],


def weight_calcaulate(j): #가중치 * 고정값 하는 함수
    result= j[0]*list_score[0] + j[1]*list_score[1] + j[2]*list_score[2]
    return result


list5=[0,0,0,0,0]
for i in range(5):
    if repair_shop[i]==1:
        list3 = list1[i]
        k1 = list3[0]
        k2 = list3[1]
        k3 = list3[2]
        
        K1 = weight_calcaulate(k1)
        K2 = weight_calcaulate(k2)
        K3 = weight_calcaulate(k3)
        
        list4 = [K1,K2,K3]
        maxindex = numpy.argmax(list4)+1        
        list5[i]=maxindex

repair_sh=['A','B','C','D','E']
print("You should visit ",end='')

repairshop=[]
for i in range(5):
    if repair_shop[i]==1:
        repairshopp=repair_sh[i]+str(list5[i])
        print(repairshopp,end='  ')        
        
        repairshop.append(repairshopp)
print()

print("Let me recommend the path to visit repair shop(s)")




import queue

graph = {}
infinity = float("inf")
costs = {}
parents = {}
processed = []

# 초기화
def init():
    global graph, infinity, costs, parents, processed
    graph = {} # 간선 정보 입력
    graph["Start"] = {}
    graph["A1"] = {}
    graph["A2"] = {}
    graph["A3"] = {}
    graph["B1"] = {}
    graph["B2"] = {}
    graph["B3"] = {}
    graph["C1"] = {}
    graph["C2"] = {}
    graph["C3"] = {}
    graph["D1"] = {}
    graph["D2"] = {}
    graph["D3"] = {}
    graph["E1"] = {}
    graph["E2"] = {}
    graph["E3"] = {}
    graph["Village"] = {}

    graph["Start"]["A1"] = 5
    graph["Start"]["A2"] = 8
    graph["Start"]["A3"] = 5
    graph["Start"]["B1"] = 5
    graph["Start"]["B2"] = 3
    graph["Start"]["B3"] = 9
    graph["Start"]["C1"] = 2
    graph["Start"]["C2"] = 4
    graph["Start"]["C3"] = 9
    graph["Start"]["D1"] = 6
    graph["Start"]["D2"] = 6
    graph["Start"]["D3"] = 7
    graph["Start"]["E1"] = 2
    graph["Start"]["E2"] = 4
    graph["Start"]["E3"] = 5
    graph["Start"]["Village"] = 8
    
    graph["A1"]["A2"] = 2
    graph["A1"]["A3"] = 3
    graph["A1"]["B1"] = 4
    graph["A1"]["B2"] = 5
    graph["A1"]["B3"] = 6
    graph["A1"]["C1"] = 5
    graph["A1"]["C2"] = 4
    graph["A1"]["C3"] = 7
    graph["A1"]["D1"] = 4
    graph["A1"]["D2"] = 6
    graph["A1"]["D3"] = 5
    graph["A1"]["E1"] = 1
    graph["A1"]["E2"] = 4
    graph["A1"]["E3"] = 5
    graph["A1"]["Village"] = 9

    graph["A2"]["A3"] = 4
    graph["A2"]["B1"] = 5
    graph["A2"]["B2"] = 4
    graph["A2"]["B3"] = 2
    graph["A2"]["C1"] = 6
    graph["A2"]["C2"] = 7
    graph["A2"]["C3"] = 8
    graph["A2"]["D1"] = 4
    graph["A2"]["D2"] = 3
    graph["A2"]["D3"] = 5
    graph["A2"]["E1"] = 9
    graph["A2"]["E2"] = 4
    graph["A2"]["E3"] = 5
    graph["A2"]["Village"] = 4

    graph["A3"]["B1"] = 5
    graph["A3"]["B2"] = 8
    graph["A3"]["B3"] = 4
    graph["A3"]["C1"] = 6
    graph["A3"]["C2"] = 1
    graph["A3"]["C3"] = 4
    graph["A3"]["D1"] = 5
    graph["A3"]["D2"] = 7
    graph["A3"]["D3"] = 8
    graph["A3"]["E1"] = 6
    graph["A3"]["E2"] = 1
    graph["A3"]["E3"] = 5
    graph["A3"]["Village"] = 2
    

    graph["B1"]["B2"] = 2
    graph["B1"]["B3"] = 3
    graph["B1"]["C1"] = 1
    graph["B1"]["C2"] = 5
    graph["B1"]["C3"] = 4
    graph["B1"]["D1"] = 9
    graph["B1"]["D2"] = 7
    graph["B1"]["D3"] = 8
    graph["B1"]["E1"] = 5
    graph["B1"]["E2"] = 6
    graph["B1"]["E3"] = 3
    graph["B1"]["Village"] = 5

    graph["B2"]["B3"] = 4
    graph["B2"]["C1"] = 4
    graph["B2"]["C2"] = 5
    graph["B2"]["C3"] = 6
    graph["B2"]["D1"] = 7
    graph["B2"]["D2"] = 8
    graph["B2"]["D3"] = 5
    graph["B2"]["E1"] = 4
    graph["B2"]["E2"] = 6
    graph["B2"]["E3"] = 1
    graph["B2"]["Village"] = 3

    graph["B3"]["C1"] = 3
    graph["B3"]["C2"] = 2
    graph["B3"]["C3"] = 5
    graph["B3"]["D1"] = 4
    graph["B3"]["D2"] = 7
    graph["B3"]["D3"] = 8
    graph["B3"]["E1"] = 5
    graph["B3"]["E2"] = 6
    graph["B3"]["E3"] = 2
    graph["B3"]["Village"] = 1

    graph["C1"]["C2"] = 2
    graph["C1"]["C3"] = 3
    graph["C1"]["D1"] = 5
    graph["C1"]["D2"] = 5
    graph["C1"]["D3"] = 4
    graph["C1"]["E1"] = 2
    graph["C1"]["E2"] = 6
    graph["C1"]["E3"] = 6
    graph["C1"]["Village"] = 9

    graph["C2"]["C3"] = 2
    graph["C2"]["D1"] = 6
    graph["C2"]["D2"] = 9
    graph["C2"]["D3"] = 2
    graph["C2"]["E1"] = 2
    graph["C2"]["E2"] = 4
    graph["C2"]["E3"] = 4
    graph["C2"]["Village"] = 2

    graph["C3"]["D1"] = 5
    graph["C3"]["D2"] = 6
    graph["C3"]["D3"] = 2
    graph["C3"]["E1"] = 2
    graph["C3"]["E2"] = 7
    graph["C3"]["E3"] = 9
    graph["C3"]["Village"] = 1

    graph["D1"]["D2"] = 2
    graph["D1"]["D3"] = 2
    graph["D1"]["E1"] = 1
    graph["D1"]["E2"] = 2
    graph["D1"]["E3"] = 7
    graph["D1"]["Village"] = 3

    graph["D2"]["D3"] = 4
    graph["D2"]["E1"] = 3
    graph["D2"]["E2"] = 2
    graph["D2"]["E3"] = 1
    graph["D2"]["Village"] = 7

    graph["D3"]["E1"] = 3
    graph["D3"]["E2"] = 2
    graph["D3"]["E3"] = 2
    graph["D3"]["Village"] = 1

    graph["E1"]["E2"] = 2
    graph["E1"]["E3"] = 3
    graph["E1"]["Village"] = 4

    graph["E2"]["E3"] = 2
    graph["E2"]["Village"] = 5

    graph["E3"]["Village"] = 2



    # ----------------------------------------
    infinity = float("inf")
    # ------------------------------------------
    costs = {} # 해당 노드 최단경로 입력
    costs["Start"] = infinity
    costs["A1"] = infinity
    costs["A2"] = infinity
    costs["A3"] = infinity
    costs["B1"] = infinity
    costs["B2"] = infinity
    costs["B3"] = infinity
    costs["C1"] = infinity
    costs["C2"] = infinity
    costs["C3"] = infinity
    costs["D1"] = infinity
    costs["D2"] = infinity
    costs["D3"] = infinity
    costs["E1"] = infinity
    costs["E2"] = infinity
    costs["E3"] = infinity
    costs["Village"] = infinity
    # -------------------------------------------
    parents = {} # 추적 경로를 위해 부모 설정
    parents["A1"] = None
    parents["A2"] = None
    parents["A3"] = None
    parents["B1"] = None
    parents["B2"] = None
    parents["B3"] = None
    parents["C1"] = None
    parents["C2"] = None
    parents["C3"] = None
    parents["D1"] = None
    parents["D2"] = None
    parents["D3"] = None
    parents["E1"] = None
    parents["E2"] = None
    parents["E3"] = None
    parents["Village"] = None
    # -------------------------------------------
    processed = []

# 최단 경로를 가진 노드를 구한다.
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

# 다익스트라 알고리즘
listcost=[]
def dijkstra(graph, start, final):
    cost=0
    node = start
    costs[start] = 0
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost: # 현재 가지고있는 cost보다 new_cost가 더 최단거리라면
                costs[n] = new_cost # 갱신
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    # 경로 추적 로직
    trace = []
    current = final
    while current != start:
        trace.append(current)
        current = parents[current]
    trace.append(start)
    trace.reverse()
    print("=== Dijkstra ===")
    print(start, "에서 ", final, "까지의 정보")
    print("최단 거리 : ", costs[final])
    listcost.append(costs[final])
    print("경로 : ", trace)

    
 
init()
repairshop.insert(0,'Start')
repairshop.append('Village')
print(repairshop)
total=0
for i in range(len(repairshop)+2):
    if repairshop[i+1]!='Village':
        dijkstra(graph, repairshop[i],repairshop[i+1])
    else:
        dijkstra(graph, repairshop[i],repairshop[i+1])
        for i in range(len(listcost)):
            total+=listcost[i]
        print("Finish The shortest distance is ",total)
        break
