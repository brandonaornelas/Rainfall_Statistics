months = {'January': None, 'February': None, 'March': None, 'April': None, 'May': None, 'June': None, 'July': None, 'August': None, 'September': None, 'October': None, 'November': None, 'December': None}


def user_input():
    for key in months.keys():
        try:
            number = float(input(f'Enter rainfall for {key}: '))
            months[key] = number
        except (ValueError, TypeError):
            print('Rainfall has to be a number.')
            number = float(input(f'Enter rainfall for {key}: '))
            months[key] = number
    return months       


def main():
    user_input()
    maximum = max(months, key=months.get)
    minimum = min(months, key=months.get)
    total = sum(months.values())
    average = (sum(months.values()) / len(months))
    print()
    print(f'Total rainfall for the year: {total}')
    print(f'Average rainfall for the year: {average}')
    print(f'Hightest rainfall month: {maximum}')
    print(f'Lowest rainfall month: {minimum}')


main()

        