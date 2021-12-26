import class_name

def initiate_game(initial_state, Table):
    
    if(initial_state['BLOCKS']):
        blocks = initial_state['BLOCKS']
        for block in blocks:
            Table.add_block(block)
            
    if(initial_state['ON']):
        on_blocks = initial_state['ON']
        for tuple_value in on_blocks:
            Table.PU(tuple_value[0])
            Table.S(tuple_value[0],tuple_value[1])


    return Table