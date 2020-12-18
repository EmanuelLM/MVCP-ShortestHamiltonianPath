import random
import math
import copy
 
total_Waiting_Time3 = 0
 
 
def algorithm(array):
  
    for j in range(2, len(array)):
        for i in range(len(array[0])):
            array[j][i] = 0
 
    initial_floor = random.randint(0, 101)
    # Indicates where the elevator will stop
    stops = list()
    # Indicates what person is being served
    serving_i = list()
    # Indicates the waiting time for each person
    waiting_time = list()
    # Helps compute the subpaths
    tmp_path = list()
 
    # Add the original floor (random) to the list of stops
    stops.append(initial_floor)
    total_waiting_time = 0
    average_waiting_time = 0
    cumulative_waiting_time = 0
 
    #  Compute the big path THEN see if the elevator can stop to fetch anyone else
    for i in range(len(array[0])):
        if array[0][i] < array[1][i]:
            direction = 1
        else:
            direction = -1
 
        status = array[2][i]
 
        # if person has not been served, continue
        if status == 0:
            # clear the temp path
            tmp_path.clear()
            # MAIN path (WF)
            tmp_path.append(array[0][i])
            #  MAIN path (DF)
            tmp_path.append(array[1][i])
            # Person being served ID
            serving_i.append(i)
            # Set served status to 1
            array[2][i] = 1
            w_t = abs(stops[-1] - array[0][i])
            waiting_time.append(cumulative_waiting_time + w_t)
            # Compute subpaths
            for j in range(1, len(array[0])):
                w_t = abs(tmp_path[0] - array[0][j])
                # UP --> people are going in the same direction
                if direction > 0 and array[0][j] > array[0][i] and array[1][i] > array[1][j] \
                        and array[0][j] < array[1][j] and array[2][j] != 1 and len(tmp_path) < 5:
                    # Add the waiting floor
                    tmp_path.append(array[0][j])
                    # Add the destination floor
                    tmp_path.append(array[1][j])
                    # Compute the waiting time
                    waiting_time.append(waiting_time[-1] + w_t)
                    # Store index of person
                    serving_i.append(j)
                    # Update served status
                    array[2][j] = 1
                # DOWN --> can we pick up x person
                elif direction < 0 and array[0][j] < array[0][i] and array[1][i] < array[1][j] \
                        and array[0][j] > array[1][j] and array[2][j] != 1 and len(tmp_path) < 5:
                    # add WF
                    tmp_path.append(array[0][j])
                    # add DF
                    tmp_path.append(array[1][j])
                    # store index of person
                    serving_i.append(j)
                    waiting_time.append(waiting_time[-1] + w_t)
                    array[2][j] = 1
 
            if direction > 0:
                # Sort in ascending order
                tmp_path.sort()
            else:
                # Sort in descending order
                tmp_path.sort(reverse=True)
            # add the subpaths to the main one
            for p in tmp_path:
                stops.append(p)
        cumulative_waiting_time = waiting_time[-1]
 
    for i in range(len(waiting_time)):
        array[3][i] = waiting_time[serving_i[i]]
 
    # Call the second elevator for the 15 longest waiting people
    #             We must find them first
 
    # INDEX of the people who have the longest waiting times
    highest_fifteen_index = list()
    len_arr = len(array[0])
 
    if len_arr == 30:
        # Get the 15 last people
        for i in range(len(serving_i) - 15, len(serving_i)):
            highest_fifteen_index.append(serving_i[i])
    elif len_arr == 15:  # Get the 5 last people
        for i in range(len(serving_i) - 5, len(serving_i)):
            highest_fifteen_index.append(serving_i[i])
 
    # We want at index 0 to be the person who has waited the longest
    highest_fifteen_index.reverse()
    print('Sending ', highest_fifteen_index, " to lift 2")
 
    # initialize the subset that will go to the elevator 2
    top15_wt = list()
    for i in range(4):
        top15_wt.append(list())
        for j in range(len(highest_fifteen_index)):
            top15_wt[i].append(0)
    # Copies the info the the main array to the subset one of 15 people
    for i in range(len(top15_wt)):
        for j in range(len(top15_wt[0])):
            if i == 2:  # WT and SS to 0
                top15_wt[i][j] = 0
            else:
                # Rest is copied
                top15_wt[i][j] = array[i][highest_fifteen_index[j]]
 
    # Create a copy of the index, we need this because throughout the process, we are going to modify the list.
    # We wish to keep the original indexes though
    temp_highest_15_index = copy.deepcopy(highest_fifteen_index)
    done = False
 
    # We now need to create batches of 5 people to send the second lift as that is the limit in capacity.
    while not done:
        # Treat 5 people at a time
        if len(temp_highest_15_index) > 5:
            tmp_5 = []
            for i in range(4):
                tmp_5.append(list())
                for j in range(5):
                    tmp_5[i].append(0)
 
            for i in range(len(tmp_5)):
                for j in range(len(tmp_5[0])):
                    if i == 2:
                        tmp_5[i][j] = 0
                    else:
                        tmp_5[i][j] = array[i][temp_highest_15_index[j]]
                # Reduce the size of the list by 4 because we will iterate 4 times
                temp_highest_15_index = temp_highest_15_index[1: -1]
            temp_highest_15_index = temp_highest_15_index[1: -1]
            print('Matrix of the 5 people going to lift 2 : ', tmp_5)
            tmp_5 = lift2(tmp_5)
 
            print('Remaining people to be served : ', temp_highest_15_index)
 
            for i in range(len(array)):
                for j in range(len(highest_fifteen_index)):
                    if i == highest_fifteen_index[j]:
                        array[i][highest_fifteen_index[j]] = tmp_5[i][highest_fifteen_index[j]]
        else:
            done = True
            tmp_5 = []
            for i in range(4):
                tmp_5.append(list())
                for j in range(len(temp_highest_15_index)):
                    tmp_5[i].append(0)
 
            for i in range(4):
                tmp_5.append(len(tmp_5))
                for j in range(len(tmp_5[0])):
                    if i == j:
                        tmp_5[i][j] = 0
                    else:
                        tmp_5[i][j] = array[i][temp_highest_15_index[j]]
 
            print("Final matrix of the Lift number 2 : ", tmp_5)
            tmp_5 = lift2(tmp_5)
 
            for i in range(len(array)):
                for j in range(len(highest_fifteen_index)):
                    if i == highest_fifteen_index[j]:
                        array[i][highest_fifteen_index[j]] = tmp_5[i][highest_fifteen_index[j]]
 
    for i in range(len(array)):
        for j in range(len(highest_fifteen_index)):
            if i == highest_fifteen_index[j]:
                array[i][highest_fifteen_index[j]] = top15_wt[i][highest_fifteen_index[j]]
 
    # We now need to update the final output with the updated waiting times for the people who were served by lift 2
    print('## Lift 1 ##')
    for i in range(len(highest_fifteen_index)):
        serving_i.remove(highest_fifteen_index[i])
 
    print('The serving order of lift 1 was : ', serving_i)
 
    for i in range(len(array[3])):
        total_waiting_time += array[3][i]
 
    total_Waiting_Time3 = total_waiting_time
    average_waiting_time = total_waiting_time // len(array[3])
 
    print(
        "\t\t\t\t_______________________________________\n\t\t\t\tTABLEAU RECAPITULATIF DE L'ALGORITHME 3\n\t\t\t\t_______________________________________")
    for item in array:
        print(item)
 
    print('\nOverall statistics of the algorithm :')
    print('Total amount of time waited by users : ', total_waiting_time)
    print('Average waiting time for users : ', average_waiting_time)
    print(
        '------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
 
 
def lift2(array):
    infinity = 99999
    print('## Lift 2 finding shortest path ##')
    print('...')
    # Store the WF and DF of everyone who is going up or down
    up_wf = list()
    up_df = list()
    down_wf = list()
    down_df = list()
 
    for i in range(len(array[0])):
        array[2][i] = 0
        # person is going up
        if array[0][i] < array[1][i]:
            up_wf.append(array[0][i])
            up_df.append(array[1][i])
        else:
            # person is going down
            down_wf.append(array[0][i])
            down_df.append(array[1][i])
 
    # Compute the min and max for each WF and DF.  This ensures our lift is picking up everyone in one direction, then does the reverse.
    # This is an efficient way to serve everyone
 
    # We initialize the variable to infinity just in case no one is going up or down.
    # This will allow our adjency matrix of the graph to stay intact
 
    min_up_wf = infinity + 1
    max_up_df = infinity + 2
    max_down_wf = infinity + 3
    min_down_df = infinity + 4
 
    try:
        min_up_wf = min(*up_wf)
        max_up_df = max(*up_df)
    except Exception:
        print('No one is going up in this batch')
 
    try:
        max_down_wf = max(*down_wf)
        min_down_df = min(*down_df)
    except Exception:
        print('No one is going down in this batch')
 
    if min_up_wf == min_down_df:
        min_down_df += 1
 
    if max_up_df == max_down_wf:
        max_down_wf += 1
 
    floors = list()
    initial_floor_e2 = random.randint(0, 101)
    floors.append(initial_floor_e2)
    floors.append(min_up_wf)
    floors.append(max_up_df)
    floors.append(max_down_wf)
    floors.append(min_down_df)
    change = False
 
    for i in range(1, len(floors)):
        if floors[0] == floors[i]:
            floors[0] += 1
            initial_floor_e2 += 1
            change = True
 
    inf = 99999
    graph = Graph(len(floors), inf)
    graph.initialize_adj()
    graph.add_edge(floors.index(initial_floor_e2), floors.index(min_up_wf), abs(initial_floor_e2 - min_up_wf))
    graph.add_edge(floors.index(initial_floor_e2), floors.index(max_down_wf), abs(initial_floor_e2 - max_down_wf))
    graph.add_edge(floors.index(min_up_wf), floors.index(max_up_df), abs(min_up_wf - max_up_df))
    graph.add_edge(floors.index(max_up_df), floors.index(max_down_wf), abs(max_up_df - max_down_wf))
    graph.add_edge(floors.index(max_down_wf), floors.index(min_down_df), abs(max_down_wf - min_down_df))
    graph.add_edge(floors.index(min_down_df), floors.index(min_up_wf), abs(min_down_df - min_up_wf))
    sorted_floors = copy.deepcopy(floors)
    matrix = graph.get_matrix()
 
    min_hamiltonian_path = MinHamPath(floors, matrix, initial_floor_e2)
    MinHamPath.SMALLEST_COST = 9999
    min_hamiltonian_path.permutations(floors, 0)
    print('The Shortest Hamiltonian Path for this set is : ', MinHamPath.BEST_PATH, ' for a total cost of ',
          MinHamPath.SMALLEST_COST)
 
    total_path = list()
    tmp_path = list()
    serving_order = list()
    cumulative_waiting_time = 0
 
    if change:
        total_path.append(MinHamPath.BEST_PATH[0] - 1)
    else:
        total_path.append(MinHamPath.BEST_PATH[0])
 
    for i in range(len(MinHamPath.BEST_PATH) - 1):
        tmp_path.clear()
        if MinHamPath.BEST_PATH[i + 1] > MinHamPath.BEST_PATH[i]:
            for j in range(len(array[0])):
                if array[0][j] < array[1][j] and array[2][j] != 1 and array[0][j] >= MinHamPath.BEST_PATH[i]:
                    tmp_path.append(array[0][j])
                    tmp_path.append(array[1][j])
                    array[2][j] = 1
 
                    w_tt = abs(MinHamPath.BEST_PATH[i] - array[0][j]) + cumulative_waiting_time
                    serving_order.append(j)
                    array[3][j] = 100 + w_tt
 
            tmp_path.sort()
            cumulative_waiting_time += abs(MinHamPath.BEST_PATH[i] - MinHamPath.BEST_PATH[i + 1])
        else:
            for j in range(len(array[0])):
                if array[0][j] > array[1][j] and array[2][j] != 1 and array[0][j] <= MinHamPath.BEST_PATH[i]:
                    tmp_path.append(array[0][j])
                    tmp_path.append(array[1][j])
                    array[2][j] = 1
                    w_tt = abs(MinHamPath.BEST_PATH[i] - array[0][j]) + cumulative_waiting_time
                    serving_order.append(j)
                    array[3][j] = 100 + w_tt
 
            tmp_path.sort(reverse=True)
            cumulative_waiting_time += abs(MinHamPath.BEST_PATH[i] - MinHamPath.BEST_PATH[i + 1])
 
        for k in range(len(tmp_path)):
            total_path.append(tmp_path[k])
    print('Complete path of Lift2 is  ', total_path, ',the serving order was : ', serving_order)
    return array
 
 
class Graph:
    ADJ_MATRIX = []
 
    def __init__(self, num_vertices, infinity):
        self.num_vertices = num_vertices
        self.infinity = infinity
        Graph.ADJ_MATRIX = list()
        for i in range(num_vertices):
            Graph.ADJ_MATRIX.append(list())
            for j in range(num_vertices):
                Graph.ADJ_MATRIX[i].append(0)
 
    def initialize_adj(self):
        for i in range(len(Graph.ADJ_MATRIX[0])):
            for j in range(len(Graph.ADJ_MATRIX)):
                Graph.ADJ_MATRIX[i][j] = self.infinity
 
    def add_edge(self, source, destination, distance):
        Graph.ADJ_MATRIX[source][destination] = distance
 
    def print_matrix(self):
        print('Distance Matrix:', Graph.ADJ_MATRIX)
 
    def get_matrix(self):
        return Graph.ADJ_MATRIX
 
 
class MinHamPath:
    SMALLEST_COST = 9999
    INITIAL_FLOOR = 0
    BEST_PATH = list()
    ORIGINAL_FLOORS = list()
    ADJ_MATRIX = list()
 
    def __init__(self, original_floorsi, adj_matrixi, initial_floori):
        MinHamPath.ORIGINAL_FLOORS = copy.deepcopy(original_floorsi)
        MinHamPath.ADJ_MATRIX = adj_matrixi
        MinHamPath.INITIAL_FLOOR = initial_floori
 
    def permutations(self, array, element):
        for i in range(element, len(array)):
            tmp = array[i]
            array[i] = array[element]
            array[element] = tmp
            self.permutations(array, element + 1)
            tmp = array[element]
            array[element] = array[i]
            array[i] = tmp
 
        if element == len(array) - 1 and array[0] == MinHamPath.INITIAL_FLOOR:
            self.helper_function(array)
 
    def helper_function(self, array):
        current_cost = 0
        for i in range(len(array) - 1):
            current_cost += MinHamPath.ADJ_MATRIX[MinHamPath.ORIGINAL_FLOORS.index(array[i])][
                MinHamPath.ORIGINAL_FLOORS.index(array[i + 1])]
 
        if current_cost < MinHamPath.SMALLEST_COST:
            MinHamPath.BEST_PATH = copy.deepcopy(array)
 
        MinHamPath.SMALLEST_COST = min(current_cost, MinHamPath.SMALLEST_COST)
 
 
array = list()
array.append([98, 19, 72, 63, 23, 94, 91, 43, 15, 99, 25, 22, 96, 0, 22, 0, 49, 79, 51, 74, 61, 6, 83, 11, 44, 47, 92, 2, 17, 76])
array.append([67, 63, 28, 3, 63, 5, 72, 16, 34, 77, 95, 71, 44, 83, 98, 55, 63, 28, 13, 10, 59, 97, 40, 93, 38, 15, 44, 99, 21, 68])
array.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
array.append([0, 1784, 21, 77, 681, 1151, 128, 217, 478, 1209, 133, 150, 201, 402, 543, 844, 1274, 220, 216, 258, 329, 325, 337, 338, 340, 346, 748, 984, 1446, 1613])
algorithm(array)