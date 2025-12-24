from list_of_movements import list_of_movements

def get_password(dial_move_list: list[str], full_dial: list[int], dial_start: int) -> int:
    list_restarts: int = 0
    current_dial_position: int = dial_start
    dial_size: int = len(full_dial)
    
    for move in dial_move_list:
        direction: str = move[0]    #get direction from move string ex. 'R68' becomes 'R'
        steps: int = int(move[1:])  #get steps from move string ex. 'R68' becomes 68
        
        if direction == "R":
            current_dial_position = (current_dial_position + steps) % dial_size
        elif direction == "L":
            current_dial_position = (current_dial_position - steps) % dial_size
        
        if current_dial_position == 0:
            list_restarts += 1
            
    return list_restarts

def main():
    full_dial: list[int] = [n for n in range(0, 100)]
    dial_start: int = 50
    
    #expected result 3
    test_move_list: list[str] = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    
    move_list: list[str] = list_of_movements

    final_dial_position = get_password(move_list, full_dial, dial_start)
    
    print(final_dial_position)
    
if __name__ == "__main__":
    main()
