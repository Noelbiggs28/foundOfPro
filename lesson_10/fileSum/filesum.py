def file_sum(name_of_text_file):
    try: 
        total = 0
        with open(name_of_text_file, 'r') as numbers:
            for line in numbers:
                total += float(line.strip())
        with open('sum.txt', 'w') as sum:
            sum.write(str(total))
    except FileNotFoundError:
        print('cant find file')

file_sum('numbers.txt')