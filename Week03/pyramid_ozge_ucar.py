def calculate_pyramid_height(number_of_blocks):
    height = 0
    blocks_used = 0
    while True:
        next_layer_blocks = height + 1
        if blocks_used + next_layer_blocks <= number_of_blocks:
            blocks_used += next_layer_blocks
            height += 1
        else:
            break
    return height
