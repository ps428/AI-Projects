import block

Table = block.Table()

initial_state = {
    'ON':[['A','B'],['C','D']],
    'CLR':['C','A']
}

final_state = {
    'ON':['C','D'],
    'ONT':['A','B'],
    'CLR':['A','B','C']    
}


Table.add_block('A')
Table.add_block('B')
Table.add_block('C')
Table.add_block('D')

Table.PU('A')
Table.S('A','B')

Table.PU('C')
Table.S('C','D')
# initial condition met
print("INITIAL STATE:-")
print(initial_state)

Table.print_table()

Table.US('A','B')

print("Unstacked A:-")
Table.print_table()

Table.PD()

print("Putdown A")
Table.print_table()

print("FINAL STATE:-")
print(final_state)
