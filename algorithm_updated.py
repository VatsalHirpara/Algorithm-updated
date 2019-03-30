import csv

# TIME-TABLE FOR B-TECH FIRST YEAR

faculty_lecture_final_map = {}

class Faculty:
    def __init__(self):
        self.preferences_map = {}
        self.max_lectures = {}
        self.faculty_slot_map = {}
    def fill_the_map(self,faculty_id,preference):
        if faculty_id not in self.preferences_map:
            self.preferences_map[faculty_id]=[]
            self.preferences_map[faculty_id].append(preference)
        else:
            self.preferences_map[faculty_id].append(preference)
        #print(name,row,column)
    def printxyz(self):
        print(self.preferences_map)
    def set_max_lectures(self,faculty_id,max_lec):
        self.max_lectures[faculty_id] = max_lec
    def get_max_lectures(self,faculty_id):
        return self.max_lectures[faculty_id]
    def add_faculty_and_slot(self,faculty_id,slot):
        self.faculty_slot_map[faculty_id] = slot
 
class Time_table:
    def __init__(self):
        self.time_table_map = {}    
        self.faculties_name = []
        self.final_time_table = {}
        self.counter = {}
        self.max_lec = {}
        self.blocked_slot = []
        self.faculty_lectures = {}
        self.batch = ""
    def set_max_lectures(self,name,max_lecs):
        self.max_lec[name] = max_lecs
    def fill_the_map(self,faculty_id,preference):
        if preference not in self.time_table_map:
            self.time_table_map[preference]=[]
            self.time_table_map[preference].append(faculty_id)
        else:
            self.time_table_map[preference].append(faculty_id)
        #print(name,row,column)
    def fill_counter(self,name):
        self.counter[name] = 0
    def add_faculty(self,name):
        self.faculties_name.append(name)
        self.faculty_lectures[name] = []
    def make_time_table(self):
        while_count = 0
        while 1:
            delete = []
            while_count += 1
            if while_count >= 5:
                while_count = 1
                for name in self.faculties_name:
                    if self.max_lec[name] == self.counter[name]:
                        continue
                    for i in range(1,6):
                        if self.max_lec[name] == self.counter[name]:
                            break
                        for j in range(1,6):
                            if self.max_lec[name] == self.counter[name]:
                                break
                            preference = (i-1)*5 + j
                            preference = str(preference)
                            if preference in self.blocked_slot:
                                continue
                            binary = 0
                            for slot_batch in faculty_lecture_final_map[name]:
                                if slot_batch==preference:
                                    binary = 1
                                    break
                            for k in range(1,6):
                                temp_preference = (i-1)*5 + k
                                temp_preference = str(temp_preference)
                                if temp_preference in self.blocked_slot and temp_preference in self.final_time_table:
                                    if self.final_time_table[temp_preference] == name:
                                        binary = 1
                                        break
                            if binary == 0:
                                if preference not in self.blocked_slot:
                                    self.faculty_lectures[name].append(preference)
                                    self.final_time_table[preference] = name
                                    if name not in faculty_lecture_final_map:
                                        faculty_lecture_final_map[name] = []
                                        faculty_lecture_final_map[name].append((preference,self.batch))
                                    else:
                                        faculty_lecture_final_map[name].append((preference,self.batch))
                                    self.counter[name] += 1
                                    temp = name
                                    self.blocked_slot.append(preference)
                                    #print(temp,self.counter[temp],preference)
                                    for k in range(1,6):
                                        temp_preference = (i-1)*5 + k
                                        temp_preference = str(temp_preference)
                                        if temp_preference not in self.time_table_map:
                                            continue
                                        if temp in self.time_table_map[temp_preference]:
                                            self.time_table_map[temp_preference].remove(temp)
                                    delete.append(preference)
                                    
            cnt = 0
            for name in self.faculties_name:
                if self.max_lec[name] == self.counter[name]:
                    cnt += 1 
                    for arr in self.time_table_map:
                        if name in self.time_table_map[arr]:
                            self.time_table_map[arr].remove(name)        
            if cnt == len(self.faculties_name):
                break
            for arr in self.time_table_map:
                if len(self.time_table_map[arr]) == 1:
                    if self.counter[self.time_table_map[arr][0]] == self.max_lec[self.time_table_map[arr][0]]:
                        continue
                    binary = 0
                    if self.time_table_map[arr][0] in faculty_lecture_final_map:
                        for slot_batch in faculty_lecture_final_map[self.time_table_map[arr][0]]:
                            if slot_batch==arr:
                                binary = 1
                                break
                        if binary==1:
                            continue
                    self.faculty_lectures[self.time_table_map[arr][0]].append(arr)
                    self.final_time_table[arr] = self.time_table_map[arr][0]
                    self.counter[self.time_table_map[arr][0]] += 1
                    temp = self.time_table_map[arr][0]
                    if temp not in faculty_lecture_final_map:
                        faculty_lecture_final_map[temp] = []
                        faculty_lecture_final_map[temp].append((arr,self.batch))
                    else:
                        faculty_lecture_final_map[temp].append((arr,self.batch))
                    self.blocked_slot.append(arr)
                    #print(temp,self.counter[temp],arr)
                    while_count = 0
                    for i in range(1,6):
                        temp_preference = (int(arr)-1)/5
                        temp_preference = temp_preference*5
                        temp_preference = temp_preference + i
                        temp_preference = str(temp_preference)
                        if temp_preference not in self.time_table_map:
                            continue
                        if temp in self.time_table_map[temp_preference]:
                            self.time_table_map[temp_preference].remove(temp)
                    delete.append(arr)
                else:
                    flag = 0
                    minimum = 20
                    for prof in self.time_table_map[arr]:
                        if self.counter[prof] == self.max_lec[prof]:
                            continue
                        binary = 0
                        if prof in faculty_lecture_final_map:
                            for slot_batch in faculty_lecture_final_map[prof]:
                                if slot_batch==arr:
                                    binary = 1
                                    break
                            if binary==1:
                                continue
                        if self.counter[prof] <= minimum:
                            minimum = self.counter[prof]
                            flag = 1
                            temp = prof
                    if flag == 1:
                        while_count = 0
                        self.faculty_lectures[temp].append(arr)
                        self.final_time_table[arr] = temp
                        self.counter[temp] += 1
                        if temp not in faculty_lecture_final_map:
                            faculty_lecture_final_map[temp] = []
                        faculty_lecture_final_map[temp].append((arr,self.batch))
                        #print(temp,self.counter[temp],arr)
                        for i in range(1,6):
                            temp_preference = (int(arr)-1)/5
                            temp_preference = temp_preference*5
                            temp_preference = temp_preference + i
                            temp_preference = str(temp_preference)
                            if temp_preference not in self.time_table_map:
                                continue
                            if temp in self.time_table_map[temp_preference]:
                                self.time_table_map[temp_preference].remove(temp)
                        delete.append(arr)
                        self.blocked_slot.append(arr)
            for x in delete:
                if x in self.time_table_map:
                    del self.time_table_map[x]
    def print_time_table(self):
        for i in range(1,6):
            for j in range(1,6):
                preference = (i-1)*5 + j
                preference = str(preference)
                if preference in self.final_time_table:
                    print(self.final_time_table[preference],preference,end=' ')
                else:
                    print("     ",preference,"     ", end=' ')
                print("")
            print("")
    def printxyz(self):
        print(self.time_table_map)
    def set_batch(self,batch):
        self.batch = batch

def get_input_1():
    print("Give the name of the preferences csv file for B-Tech First Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    faculty_id = str(column)
                    print("Maximum lectures of",faculty_id,":-")
                    max_lec = int(input())
                    faculty_map_1.set_max_lectures(faculty_id,max_lec)
                    time_table_1.set_max_lectures(faculty_id,max_lec)
                    time_table_1.fill_counter(faculty_id)
                    time_table_1.add_faculty(faculty_id)
                    time_table_1.set_batch("btech1")
                else:
                    if len(column) < 3 and len(column) > 0:
                        time_table_1.fill_the_map(faculty_id,column)
                        faculty_map_1.fill_the_map(faculty_id,column)
                c = c+1
                #print(column)

faculty_map_1 = Faculty()
time_table_1 = Time_table()
get_input_1()
#faculty_map.printxyz()
time_table_1.make_time_table()
print()
print()
print()
time_table_1.print_time_table()



# TIME-TABLE FOR B-TECH SECOND YEAR

def get_input_2():
    print("Give the name of the preferences csv file for B-Tech Second Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    faculty_id = str(column)
                    print("Maximum lectures of",faculty_id,":-")
                    max_lec = int(input())
                    faculty_map_2.set_max_lectures(faculty_id,max_lec)
                    time_table_2.set_max_lectures(faculty_id,max_lec)
                    time_table_2.fill_counter(faculty_id)
                    time_table_2.add_faculty(faculty_id)
                    time_table_2.set_batch("btech2")
                else:
                    if len(column) < 3 and len(column) > 0:
                        time_table_2.fill_the_map(faculty_id,column)
                        faculty_map_2.fill_the_map(faculty_id,column)
                c = c+1
                #print(column)

faculty_map_2 = Faculty()
time_table_2 = Time_table()
get_input_2()
#faculty_map.printxyz()
time_table_2.make_time_table()
print()
print()
print()
time_table_2.print_time_table()


# TIME-TABLE FOR B-TECH THIRD YEAR


class Time_table_with_slots:
    def __init__(self):
        self.time_table_map = {}    
        self.slot_faculty_map = {}
        self.slots_name = []
        self.final_time_table = {}
        self.counter = {}
        self.max_lec = {}
        self.blocked_slot = []
        self.faculty_lectures = {}
        self.batch = ""
        self.preferences = {}
        self.weighted_preferences = {}
        for i in range(1,6):
            for j in range(1,6):
                preference = (i-1)*5 + j
                preference = str(preference)
                self.final_time_table[preference] = []
    def set_max_lectures(self,name,max_lecs):
        self.max_lec[name] = max_lecs
    def fill_the_map(self):
        for slot in self.weighted_preferences:
            for preference,weight in self.weighted_preferences[slot]:
                if preference not in self.time_table_map:
                    self.time_table_map[preference] = []
                    self.time_table_map[preference].append((slot,weight))
                else:
                    self.time_table_map[preference].append((slot,weight))
    def fill_counter(self,name):
        self.counter[name] = 0
    def add_slots(self,name):
        self.slots_name.append(name)
        if name in self.slot_faculty_map:
            for faculty in self.slot_faculty_map[name]:
                self.faculty_lectures[faculty] = []
    def make_time_table(self):
        while_count = 0
        while 1:
            delete = []
            while_count += 1
            if while_count >= 5:
                while_count = 0
                for slot in self.slots_name:
                    if self.max_lec[slot] == self.counter[slot]:
                        continue
                    for i in range(1,6):
                        if self.max_lec[slot] == self.counter[slot]:
                            break
                        for j in range(1,6):
                            if self.max_lec[slot] == self.counter[slot]:
                                break
                            preference = (i-1)*5 + j
                            preference = str(preference)    
                            if preference in self.blocked_slot:
                                continue
                            binary = 0
                            for faculty in self.slot_faculty_map[slot]:
                                if faculty in faculty_lecture_final_map:
                                    for slot_batch in faculty_lecture_final_map[faculty]:
                                        if slot_batch==arr:
                                            binary = 1
                                            break
                            for k in range(1,6):
                                temp_preference = (i-1)*5 + k
                                temp_preference = str(temp_preference)                
                                if temp_preference in self.blocked_slot and temp_preference in self.final_time_table:
                                    if self.slot_faculty_map[slot][0] in self.final_time_table[temp_preference]:
                                        binary = 1
                                        break
                            if binary == 0:
                                if preference not in self.blocked_slot:
                                    for faculty in self.slot_faculty_map[slot]:
                                        self.faculty_lectures[faculty].append(preference)
                                        self.final_time_table[preference].append(faculty)
                                    self.counter[slot] += 1
                                    for faculty in self.slot_faculty_map[slot]:
                                        if faculty not in faculty_lecture_final_map:
                                            faculty_lecture_final_map[faculty] = []
                                        faculty_lecture_final_map[faculty].append((preference,self.batch))
                                    for l in range(1,6):
                                        temp_preference = (i-1)*5 + l
                                        temp_preference = str(temp_preference)
                                        if temp_preference not in self.time_table_map:
                                            continue
                                        for slots,weight in self.time_table_map[temp_preference]:
                                            if slots == slot:
                                                self.time_table_map[temp_preference].remove((slots,weight))
                                    self.blocked_slot.append(preference)
                                    while_count = 0
                                    delete.append(preference)
            cnt = 0
            for name in self.slots_name:
                if self.max_lec[name] == self.counter[name]:
                    cnt += 1 
                    for arr in self.time_table_map:
                        for slot,weight in self.time_table_map[arr]:
                            if name == slot:
                                self.time_table_map[arr].remove((slot,weight))        
            if cnt == len(self.slots_name):
                break
            for arr in self.time_table_map:
                if len(self.time_table_map[arr]) == 1:
                    if self.counter[self.time_table_map[arr][0][0]] == self.max_lec[self.time_table_map[arr][0][0]]:
                        continue
                    binary = 0
                    for faculty in self.slot_faculty_map[self.time_table_map[arr][0][0]]:
                        if faculty in faculty_lecture_final_map:
                            for slot_batch in faculty_lecture_final_map[faculty]:
                                if slot_batch==arr:
                                    binary = 1
                                    break
                    if binary==1:
                        continue
                    for faculty in self.slot_faculty_map[self.time_table_map[arr][0][0]]:
                        #print(self.faculty_lectures)
                        self.faculty_lectures[faculty].append(arr)
                        self.final_time_table[arr].append(faculty)
                    self.counter[self.time_table_map[arr][0][0]] += 1
                    for faculty in self.slot_faculty_map[self.time_table_map[arr][0][0]]:
                        temp = faculty
                        if temp not in faculty_lecture_final_map:
                            faculty_lecture_final_map[temp] = []
                        faculty_lecture_final_map[temp].append((arr,self.batch))
                    temp = self.time_table_map[arr][0][0]
                    for i in range(1,6):
                        temp_preference = (int(arr)-1)/5
                        temp_preference = temp_preference*5
                        temp_preference = temp_preference + i
                        temp_preference = str(temp_preference)
                        if temp_preference not in self.time_table_map:
                            continue
                        for slot,weight in self.time_table_map[temp_preference]:
                            if temp == slot:
                                self.time_table_map[temp_preference].remove((slot,weight))
                    self.blocked_slot.append(arr)
                    while_count = 0
                    delete.append(arr)
                else:
                    flag = 0
                    maximum = 0
                    for slot,weight in self.time_table_map[arr]:
                        if self.counter[slot] == self.max_lec[slot]:
                            continue
                        binary = 0
                        for faculty in self.slot_faculty_map[slot]:
                            if faculty in faculty_lecture_final_map:
                                for slot_batch in faculty_lecture_final_map[faculty]:
                                    if slot_batch==arr:
                                        binary = 1
                                        break
                        if binary==1:
                            continue
                        if weight >= maximum:
                            maximum = weight
                            flag = 1
                            temp = slot
                    if flag == 1:
                        for faculty in self.slot_faculty_map[temp]:
                            self.faculty_lectures[faculty].append(arr)
                            self.final_time_table[arr].append(faculty)
                        self.counter[temp] += 1
                        for faculty in self.slot_faculty_map[temp]:
                            if faculty not in faculty_lecture_final_map:
                                faculty_lecture_final_map[faculty] = []
                            faculty_lecture_final_map[faculty].append((arr,self.batch))
                        for i in range(1,6):
                            temp_preference = (int(arr)-1)/5
                            temp_preference = temp_preference*5
                            temp_preference = temp_preference + i
                            temp_preference = str(temp_preference)
                            if temp_preference not in self.time_table_map:
                                continue
                            for slot,weight in self.time_table_map[temp_preference]:
                                if slot == temp:
                                    self.time_table_map[temp_preference].remove((slot,weight))
                        self.blocked_slot.append(arr)
                        while_count = 0
                        delete.append(arr)
            for x in delete:
                if x in self.time_table_map:
                    del self.time_table_map[x]
    def print_time_table(self):
        for i in range(1,6):
            for j in range(1,6):
                preference = (i-1)*5 + j
                preference = str(preference)
                if preference in self.final_time_table:
                    print(self.final_time_table[preference],preference,end=' ')
                else:
                    print("     ",preference,"     ", end=' ')
                print("")
            print("")
    def printxyz(self):
        print(self.time_table_map)
    def set_batch(self,batch):
        self.batch = batch
    def add_preference(self,slot_id,preference):
        if slot_id not in self.preferences:
            self.preferences[slot_id] = []
        self.preferences[slot_id].append(preference)
    def make_weighted_preferences(self):
        for slot in self.preferences:
            self.weighted_preferences[slot] = []
        for slot in self.preferences:
            weights_of_preferences = {}
            for preference in self.preferences[slot]:
                if preference not in weights_of_preferences:
                    weights_of_preferences[preference] = 1
                else:
                    weights_of_preferences[preference] += 1
            for preference in weights_of_preferences:
                self.weighted_preferences[slot].append((preference,weights_of_preferences[preference]))
    def fill_slot_to_faculty_map(self,slot,faculty):
        if slot not in self.slot_faculty_map:
            self.slot_faculty_map[slot] = []
            self.slot_faculty_map[slot].append(faculty)
        else:
            self.slot_faculty_map[slot].append(faculty)    

def get_input_3():
    print("Give the name of the csv file which contains eight slots and its faculties for B-Tech Third Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    slot_id = column
                    print("Maximum lectures for",slot_id,":-")
                    max_lec = int(input())
                    time_table_3.set_max_lectures(slot_id,max_lec)
                    time_table_3.fill_counter(slot_id)
                    time_table_3.set_batch("btech3")
                else:
                    time_table_3.fill_slot_to_faculty_map(slot_id,column)
                    faculty_map_3.add_faculty_and_slot(column,slot_id)
                c = c+1
                #print(column)
            time_table_3.add_slots(slot_id)

    print("Give the name of the csv file which conatins preferences for B-Tech Third Year:")
    file = input()
    slot_preferences = {}
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    faculty_id = str(column)
                    slot_id = faculty_map_3.faculty_slot_map[faculty_id]
                else:
                    if len(column) < 3 and len(column) > 0:
                        time_table_3.add_preference(slot_id,column)
                c = c+1
    time_table_3.make_weighted_preferences()
    time_table_3.fill_the_map()

faculty_map_3 = Faculty()
time_table_3 = Time_table_with_slots()
get_input_3()
#faculty_map.printxyz()
time_table_3.make_time_table()
time_table_3.print_time_table()


# TIME-TABLE FOR B-TECH FOURTH YEAR


def get_input_4():
    print("Give the name of the csv file which contains eight slots and its faculties for B-Tech Fourth Year:")
    file = input()
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    slot_id = column
                    print("Maximum lectures for",slot_id,":-")
                    max_lec = int(input())
                    time_table_4.set_max_lectures(slot_id,max_lec)
                    time_table_4.fill_counter(slot_id)
                    time_table_4.set_batch("btech3")
                else:
                    time_table_4.fill_slot_to_faculty_map(slot_id,column)
                    faculty_map_4.add_faculty_and_slot(column,slot_id)
                c = c+1
                #print(column)
            time_table_4.add_slots(slot_id)

    print("Give the name of the csv file which conatins preferences for B-Tech Fourth Year:")
    file = input()
    slot_preferences = {}
    with open(file, newline='') as csvfile:
        input_data = csv.reader(csvfile, quotechar='|')
        for row in input_data:
            c = 0
            for column in row:
                if c == 0:
                    faculty_id = str(column)
                    slot = faculty_map_4.faculty_slot_map[faculty_id]
                else:
                    if len(column) < 3 and len(column) > 0:
                        time_table_4.add_preference(slot_id,column)
                c = c+1
    time_table_4.make_weighted_preferences()
    time_table_4.fill_the_map()

faculty_map_4 = Faculty()
time_table_4 = Time_table_with_slots()
get_input_4()
#faculty_map.printxyz()
time_table_4.make_time_table()
time_table_4.print_time_table()
