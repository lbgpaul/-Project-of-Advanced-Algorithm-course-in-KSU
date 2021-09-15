import random

#function print array
def print_arr(arr):
  for i in range(5):
   for j in range(6):
     if arr[i*6+j] == "R":
       print("\033[1;31m"+arr[i*6+j]+"\033[0m", end = ' ')
     elif arr[i*6+j] == "B":
       print("\033[1;34m"+arr[i*6+j]+"\033[0m", end = ' ')
     elif arr[i*6+j] == "G":
       print("\033[1;32m"+arr[i*6+j]+"\033[0m", end = ' ')
     elif arr[i*6+j] == "Y":
       print("\033[1;33m"+arr[i*6+j]+"\033[0m", end = ' ')
     elif arr[i*6+j] == "P":
       print("\033[1;35m"+arr[i*6+j]+"\033[0m", end = ' ')
     else:
       print(arr[i*6+j], end = ' ')
   print("") 

#set compute
def set_compute(arr):
  set_num = 0
  exist_num = []
  
  for i in range(5):
    for j in range(6):
      if (j <= 3):
        if ((i*6+j) not in exist_num) & ((i*6+(j+1)) not in exist_num) & ((i*6+(j+2)) not in exist_num):
          #print("do run")
          if (arr[i*6+j] == arr[i*6+(j+1)]) & (arr[i*6+j] == arr[i*6+(j+2)]): 
            set_num = set_num + 1
            exist_num.append((i*6+j))
            exist_num.append((i*6+j+1))
            exist_num.append((i*6+j+2))
        elif ((i*6+j) not in exist_num) & ((i*6+(j+1)) in exist_num) & ((i*6+(j+2)) in exist_num):
          if (arr[i*6+j] == arr[i*6+(j+1)]) & (arr[i*6+j] == arr[i*6+(j+2)]): 
            exist_num.append((i*6+j))
            
      
      if (i <= 2):
        if ((i*6+j) not in exist_num) & (((i+1)*6+j) not in exist_num) & (((i+2)*6+j) not in exist_num):
          if (arr[i*6+j] == arr[(i+1)*6+j]) & (arr[i*6+j] == arr[(i+2)*6+j]):
            set_num = set_num + 1
            exist_num.append((i*6+j))
            exist_num.append(((i+1)*6+j))
            exist_num.append(((i+2)*6+j))
        elif ((i*6+j) not in exist_num) & (((i+1)*6+j) in exist_num) & (((i+2)*6+j) in exist_num):
          if (arr[i*6+j] == arr[(i+1)*6+j]) & (arr[i*6+j] == arr[(i+2)*6+j]):
            exist_num.append((i*6+j))


  return set_num


#Compute_weight
def evaluate_arr(arr):
  #initial a weight arr to storge the evaluation
  weight_arr = []
  for i in range(30):
    weight_arr.append(0)
  #for i in range(5):
    #weight_col = []
    #for j in range(6):
     # weight_col.append(0)
    #weight_arr.append(weight_col)
  
  
  for k in range(5):
    for l in range(6):
      #top & bot
      #left & right
      #left_top
      if (k > 0) & (l > 0):
        if (arr[(k-1)*6+(l-1)] == arr[k*6+l]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 1)
      #top
      if (k > 0):
        if (arr[(k-1)*6+(l)] == arr[(k)*6+(l)]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 2)
      #right_top
      if (k > 0) & (l < 5):
        if (arr[(k-1)*6+(l+1)] == arr[k*6+l]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 1)
      #left
      if (l > 0):
        if (arr[(k)*6+(l-1)] == arr[k*6+l]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 2)
      #right
      if (l < 5):
        if (arr[(k)*6+(l+1)] == arr[k*6+l]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 2)
      #left_bot
      if (k < 4) & (l > 0):
        if (arr[(k+1)*6+(l-1)] == arr[k*6+l]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 1)
      #bot
      if (k < 4):
        if (arr[(k+1)*6+(l)] == arr[k*6+l]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 2)
      #right_bot
      if (k < 4) & (l < 5):
        if (arr[(k+1)*6+(l+1)] == arr[k*6+l]):
          weight_arr[k*6+l] = (weight_arr[k*6+l] + 1)  
  return weight_arr

#Random_startpoint
def start_point_choose(weight):

  zero_points = []
  min_weight = 10000
  for i in range(30): #find the minimun weigt in weight arr
    if weight[i] < min_weight:
      min_weight = weight[i]
  for j in range(30): #find minimun weight point and save
    if weight[j] == min_weight:
      zero_points.append(j)
  

  #print(zero_points)
  #print(start_point)
  #print(arr[start_point])
  return(zero_points)

#geneerate next three step and its arr  
def generate_next(arr, start_point):

  update_arr = []
  path = []

  for i in range(4):
    for j in range(4):
      for k in range(4):

        temp_array = []
        for l in range(len(arr)):
          temp_array.append(arr[l]) #for new arr
        current_point = start_point #for startpoint
        temp_path = []
        
        if i == 0: #top
          if current_point >= 6:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point-6]
            temp_array[current_point-6] = t 
            current_point = current_point - 6
            temp_path.append(current_point)
          else:
            continue

        elif i == 1: #right
          if (int(current_point % 6)) < 5:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point+1]
            temp_array[current_point+1] = t 
            current_point = current_point + 1
            temp_path.append(current_point)
          else:
            continue

        elif i == 2: #down
          if current_point < 24:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point+6]
            temp_array[current_point+6] = t
            current_point = current_point + 6
            temp_path.append(current_point) 
          else:
            continue

        elif i == 3: #left
          if (int(current_point % 6)) > 0:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point-1]
            temp_array[current_point-1] = t
            current_point = current_point - 1
            temp_path.append(current_point)
          else:
            continue

  #=============================================================================================
        if j == 0: #top
          if current_point >= 6:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point-6]
            temp_array[current_point-6] = t 
            current_point = current_point - 6
            temp_path.append(current_point)
          else:
            continue

        elif j == 1: #right
          if (int(current_point % 6)) < 5:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point+1]
            temp_array[current_point+1] = t 
            current_point = current_point + 1
            temp_path.append(current_point)
          else:
            continue

        elif j == 2: #down
          if current_point < 24:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point+6]
            temp_array[current_point+6] = t
            current_point = current_point + 6
            temp_path.append(current_point) 
          else:
            continue

        elif j == 3: #left
          if (int(current_point % 6)) > 0:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point-1]
            temp_array[current_point-1] = t
            current_point = current_point - 1
            temp_path.append(current_point)
          else:
            continue
  #=================================================================     
        if k == 0: #top
          if current_point >= 6:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point-6]
            temp_array[current_point-6] = t 
            current_point = current_point - 6
            temp_path.append(current_point)
          else:
            continue

        elif k == 1: #right
          if (int(current_point % 6)) < 5:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point+1]
            temp_array[current_point+1] = t 
            current_point = current_point + 1
            temp_path.append(current_point)
          else:
            continue

        elif k == 2: #down
          if current_point < 24:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point+6]
            temp_array[current_point+6] = t
            current_point = current_point + 6
            temp_path.append(current_point) 
          else:
            continue

        elif k == 3: #left
          if (int(current_point % 6)) > 0:
            t = temp_array[current_point]
            temp_array[current_point] = temp_array[current_point-1]
            temp_array[current_point-1] = t
            current_point = current_point - 1
            temp_path.append(current_point)
          else:
            continue
          
        update_arr.append(temp_array)
        path.append(temp_path)

  return(update_arr, path)
  #print(path)

  #for ar in range(len(update_arr)):
  # print_arr(update_arr[ar])
    #print("")

total = 0
#set_ar = []
b = -1
s = 1000
for tim in range(100):

  arr =[]
  for i in range(30):
    ch = random.choice("RGBYPA")
    arr.append(ch)

  #print("initial array: ")
  #print_arr(arr)
  set_n = 0
  #es_num = []
  set_n = set_compute(arr)
  #print("initial set number: ", end = "")
  #print(set_n)

  weight = []
  weight = (evaluate_arr(arr))
  #print_arr(weight)

  G_path = []
  G_arr = []
  G_arr.append(arr)


  #print("#===========first===========#")
  #pick the valuable result
  start_point_list = []
  start_point_list = start_point_choose(weight) #input weight arr give start point list
  max_set_num_lst = -1

  first_set_num = -1
  find = -1
  for c1 in range(len(start_point_list)): #make sure choose good start point

    start_point = (start_point_list[c1])
    update_arr, path = generate_next(arr, start_point) #input arr and start_point give next three step and update_arr

    for n in range(len(update_arr)): # find the maxmum set number in update next arr
      if first_set_num < set_compute(update_arr[n]):
        first_set_num = set_compute(update_arr[n])
    
  for c2 in range(len(start_point_list)): #make sure choose good start point

    start_point = (start_point_list[c2])
    update_arr, path = generate_next(arr, start_point) #input arr and start_point give next three step and update_arr

    
    for n in range(len(update_arr)): # find the maxmum set number in update next arr
      if set_compute(update_arr[n]) == first_set_num:
        find = 1
        break
    if find == 1:
      G_path.append(start_point)
      break

  pick_num = [] #number for index of the result in update_arr
  #print("set number after 123 step (stage 1): ", end = "")
  #print(first_set_num)   #some update_arr may have same set num 
  for n2 in range(len(update_arr)):
    if set_compute(update_arr[n2]) == first_set_num:
      pick_num.append(n2)
  #print("star_point:", end = '')
  #print(start_point)

  first_gen_path = []
  first_gen_update_arr = []
  for p in range(len(pick_num)): #print those 
    #print(path[pick_num[p]])
    first_gen_path.append(path[pick_num[p]])

    #print_arr(update_arr[pick_num[p]])
    first_gen_update_arr.append(update_arr[pick_num[p]])

  #next generate 456  steps
  #print("#===========second===========#")
  second_set_num = -1
  for nb in range(len(first_gen_path)):
    s_point = first_gen_path[nb][2]
  
    update_arr_2, path_2 = generate_next(first_gen_update_arr[nb], s_point) #input arr and start_point give next three step and update_arr

    for n in range(len(update_arr_2)): # find the maxmum set number in update next arr
      if second_set_num < set_compute(update_arr_2[n]):
        second_set_num = set_compute(update_arr_2[n])

  for nb in range(len(first_gen_path)):
    s_point = first_gen_path[nb][2]
    
    update_arr_2, path_2 = generate_next(first_gen_update_arr[nb], s_point) #input arr and start_point give next three step and update_arr

    for n in range(len(update_arr_2)): # find the maxmum set number in update next arr
      if set_compute(update_arr_2[n]) == second_set_num:
        break
    if set_compute(update_arr_2[n]) == second_set_num:
      G_path.append(first_gen_path[nb])
      G_arr.append(first_gen_update_arr[nb])
      break        
    
  pick_num_2 = []

  #print("Set number after 456 step(stage 2): ", end = '')
  #print(second_set_num)   #some update_arr may have same set num 
  for n2 in range(len(update_arr_2)):
    if set_compute(update_arr_2[n2]) == second_set_num:
      pick_num_2.append(n2)
  #print("start point of(stage 2): ", end = '')
  #print(s_point)
  #for p in range(len(pick_num_2)): #print those 
    #print(path_2[pick_num_2[p]])
    #print_arr(update_arr_2[pick_num_2[p]])

  #print("#===========third===========#")
  #next generate 789  steps
  third_set_num = -1
  for nb in range(len(path_2)):
    s_point = path_2[nb][2]
    
    update_arr_3, path_3 = generate_next(update_arr_2[nb], s_point) #input arr and start_point give next three step and update_arr
    
    
    for n in range(len(update_arr_3)): # find the maxmum set number in update next arr
      if third_set_num < set_compute(update_arr_3[n]):
        third_set_num = set_compute(update_arr_3[n])

  for nb in range(len(path_2)):
    s_point = path_2[nb][2]
    
    update_arr_3, path_3 = generate_next(update_arr_2[nb], s_point) #input arr and start_point give next three step and update_arr
    
    for n in range(len(update_arr_3)): # find the maxmum set number in update next arr
      if set_compute(update_arr_3[n]) == third_set_num:
        break
    if set_compute(update_arr_3[n]) == third_set_num:
      G_path.append(path_2[nb])
      G_arr.append(update_arr_2[nb])
      break    

  pick_num_3 = []
  #print("Set number after 789 step(stage 3): ", end = '')
  #print(third_set_num)   #some update_arr may have same set num 
  for n2 in range(len(update_arr_3)):
    if set_compute(update_arr_3[n2]) == third_set_num:
      pick_num_3.append(n2)
  #print("Start point of stage 3: ", end = '')
  #print(s_point)
  #for p in range(len(pick_num_3)): #print those 
    #print(path_3[pick_num_3[p]])
    #print_arr(update_arr_3[pick_num_3[p]])
  G_path.append(path_3[pick_num_3[0]])
  G_arr.append(update_arr_3[pick_num_3[0]])

  #print("#===========final===========#")
  #compute set number and print final result
  #G_path.append(path_3[0])
  #G_arr.append(update_arr_3[0])
  print(tim+1, end = '')
  print(" Times path: ", end='')
  print(G_path, end = '')
  print(" Set number: ", end= '')
  print(third_set_num)
  #for f in range(len(G_arr)):
    #if f > 0:
    #  print("stage: ", end = '')
    #  print(f)
    #else:
    #  print("initial: ")  
    #print_arr(G_arr[f])
  #set_ar.append(third_set_num)
  if third_set_num > b:
    b = third_set_num
  if third_set_num < s:
    s = third_set_num
  total = total + third_set_num
  

print("Largest set number: ", end = '')
print(b)

print("Smallest set number: ", end = '')
print(s)

print("Average set number: ", end = '')    
print(total / 100)  
