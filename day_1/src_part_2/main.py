from list_of_movements import list_of_movements

def get_password(dial_move_list: list[str], full_dial: list[int], dial_start: int) -> int:
    zero_hits: int = 0
    current_position = dial_start
    size = len(full_dial)

    for move in dial_move_list:
        direction = move[0]
        steps = int(move[1:])

        if direction == "R":
            new_pos = current_position + steps
            zero_hits += (new_pos // size) - (current_position // size)
            current_position = new_pos % size

        elif direction == "L":
            new_pos = current_position - steps
            # normalize negative positions
            zero_hits += ((current_position + size - 1) // size) - ((new_pos + size - 1) // size)
            current_position = new_pos % size

    return zero_hits

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