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

#geneerate next three step and its arr  
def generate_next(arr, start_point):

  update_arr = []
  path = []
  
  count_ar = ['a','b','c','d','e','f','g','h','i']
  for a in range(4):
    for b in range(4):
      for c in range(4):
        for d in range(4):
          for e in range(4):
            for f in range(4):
              for g in range(4):
                for h in range(4):
                  for i in range(4):  
                    
                    #initialize
                    temp_array = []
                    for l in range(len(arr)):
                      temp_array.append(arr[l]) #for new arr
                    current_point = start_point #for startpoint
                    temp_path = []
                    
                    for count in range(len(count_ar)):
                      if count_ar[count] == 'a':
                        n = a
                      elif count_ar[count] == 'b':
                        n = b
                      elif count_ar[count] == 'c':
                        n = c
                      elif count_ar[count] == 'd':
                        n = d 
                      elif count_ar[count] == 'e':
                        n = e 
                      elif count_ar[count] == 'f':
                        n = f 
                      elif count_ar[count] == 'g':
                        n = g 
                      elif count_ar[count] == 'h':
                        n = h 
                      elif count_ar[count] == 'i':
                        n = i     

                      if n == 0: #top
                        if current_point >= 6:
                          t = temp_array[current_point]
                          temp_array[current_point] = temp_array[current_point-6]
                          temp_array[current_point-6] = t 
                          current_point = current_point - 6
                          temp_path.append(current_point)

                      elif n == 1: #right
                        if (int(current_point % 6)) < 5:
                          t = temp_array[current_point]
                          temp_array[current_point] = temp_array[current_point+1]
                          temp_array[current_point+1] = t 
                          current_point = current_point + 1
                          temp_path.append(current_point)
                        
                      elif n == 2: #down
                        if current_point < 24:
                          t = temp_array[current_point]
                          temp_array[current_point] = temp_array[current_point+6]
                          temp_array[current_point+6] = t
                          current_point = current_point + 6
                          temp_path.append(current_point) 
                        

                      elif n == 3: #left
                        if (int(current_point % 6)) > 0:
                          t = temp_array[current_point]
                          temp_array[current_point] = temp_array[current_point-1]
                          temp_array[current_point-1] = t
                          current_point = current_point - 1
                          temp_path.append(current_point)
                        
                    if len(temp_path) > 8:   
                      update_arr.append(temp_array)
                      path.append(temp_path)

  
  return(update_arr, path)

L_score = -1
S_score = 10000
total = 0
set_ar = []
for tim in range(100):  

  arr =[]
  for i in range(30):
    ch = random.choice("RGBYP")
    arr.append(ch)

  #print("initial array: ")
  #print_arr(arr)
  set_n = 0
  #es_num = []
  set_n = set_compute(arr)
  #print("initial set number: ", end = "")
  #print(set_n)

  G_path = []
  G_arr = []
  G_arr.append(arr)

  arr_result = []
  arr_score = []
  arr_path = []
  for p in range(30): #from every point generate all possible path point 0~29
    update_arr, path = generate_next(arr, p)
      
    set_num = [] #every points' set number temperate
    for arr_n in range(len(update_arr)):
      set_num.append(set_compute(update_arr[arr_n]))
      
    max_set = -1 #pick up the largerest set from this point
    for j in range(len(set_num)):
      if set_num[j] > max_set:
        max_set = set_num[j]

    for k in range(len(set_num)):
      if set_num[k] == max_set:
        arr_result.append(update_arr[k])
        arr_path.append(path[k])
        arr_score.append(max_set)

        break
  max_score = -1
  pick_n = 0
  for p2 in range(30):
    if arr_score[p2] > max_score:
      max_score = arr_score[p2]
      pick_n = p2
  total = total + arr_score[pick_n]
  print(tim + 1, end = '')
  print(" Times path: ", end='')
  print(arr_path[pick_n], end = '')
  print(" Set number: ", end= '')
  print(arr_score[pick_n])
  if arr_score[pick_n] > L_score:
    L_score = arr_score[pick_n]
  if arr_score[pick_n] < S_score:
    S_score = arr_score[pick_n]

print("Largest set number: ", end = '')
print(L_score)

print("Smallest set number: ", end = '')
print(S_score)

print("Average set number: ", end = '')    
print(total / 100)
  #for p2 in range(30):
    #print('')
    #print("Start Point: ", end = '')
    #print(p2)
    #print("Set number: ", end = '')
    #print(arr_score[p2])
    #print_arr(arr_result[p2])
    #print(arr_path[p2])
  
  #print(path)
  #for ar in range(len(update_arr)):
      #print_arr(update_arr[ar])
      #print("")
