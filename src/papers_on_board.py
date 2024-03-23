def put_on_board(number_notes, note_width, note_height):
    note_area = note_width * note_height
    board_width = note_width
    board_hight = note_height

    while (board_width * board_hight) / note_area < number_notes:
        if board_width + note_width > board_hight + note_height:
            board_hight += note_height
        else:
            board_width += note_width
    if board_width > board_hight:
        result = board_width
    else:
        result = board_hight
    return result    
