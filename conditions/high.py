def highest_even():
    highest_even = [10, 1, 2, 3, 4, 8, 11]
    highest_even.sort(reverse=True)  # Sort in descending order to find the highest even number first
    print(highest_even)

    highest_even_number = None

    for value in highest_even:
        if value % 2 == 0:
            highest_even_number = value
            break

    if highest_even_number is not None:
        print(f'The highest even number is: {highest_even_number}')
    else:
        print('No even numbers found in the list.')

    return highest_even
highest_even()
