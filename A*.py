values = {'A':[('B', 6), ('F', 3)], 'B':[('A', 6), ('D', 2), ('C', 3)], 'C':[('B', 3), ('E', 5), ('D', 1)],
        'D':[('B', 2), ('C', 1), ('E', 8)], 'E':[('C', 5), ('D', 8), ('I', 5), ('J', 5)],
        'F':[('A', 3), ('G', 1), ('H', 7)], 'G':[('F', 1), ('I', 3)], 'H':[('F', 7), ('I', 2)],
        'I':[('G', 3), ('H', 2), ('E', 5), ('J', 3)],
        }
heuristic_Values = {'A':10, 'B':8, 'C':5, 'D':7, 'E':3, 'F':6, 'G':5, 'H':3, 'I':1, 'J':0}
start_node = 'A'
stop_node = 'I'
current_destination = float('inf')
Current_node = ''
total = 0
nodes = []
while Current_node != stop_node:
  for node, distination in values[start_node]:
    if current_destination > total + distination + heuristic_Values[node]:
      current_destination = total + distination + heuristic_Values[node]
      Current_node = node
  nodes.append(start_node)
  start_node = Current_node
  total = current_destination - heuristic_Values[Current_node]

  if Current_node == 'J':
    break
  Current_node = ''
  current_destination = float('inf')
nodes.append(Current_node)
print("Optimal path is ",nodes)
print("The optimal distance is ", total)