import class_name
import play_game

Table = class_name.Table()

initial_state = {
    'BLOCKS':['A','B','C','D'],
    'ON':[('A','B'),('C','D')],
    'ONT':['B','D'],
    'CLR':['C','A']
}

final_state = {
    'BLOCKS':['A','B','C','D'],
    'ON':[('C','D')],
    'ONT':['A','B'],
    'CLR':['A','B','C']
}


Table1 = play_game.initiate_game(initial_state, Table)


# initial condition met
print("INITIAL STATE:-")
for key,value in initial_state.items():
    print(key,value)

Table.print_table()

Table.US('A','B')

print("Unstacked A:-")
Table.print_table()

Table.PD()

print("Putdown A")
Table.print_table()

print("FINAL STATE:-")
for key,value in final_state.items():
    print(key,value)

print("\n-----------------------------------------------")
print("System generated final state")
Table1 = play_game.initiate_game(final_state, class_name.Table())
Table1.print_table()