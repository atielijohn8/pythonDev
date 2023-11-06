picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def show_tree():
    for i in range(len((picture))):  # Iterate over each row
        for row in picture[i]:  # Iterate over each element in the row
            if row == 0:
                print(' ', end='')
            else:
                print('*', end='')
        print()  # Move to the next line after each row

show_tree()
show_tree()