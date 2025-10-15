import  time

CSI = '\x1b['
RESET = f'{CSI}0m'
ZERO = f'{CSI}0G'
ERASE = f'{CSI}2K'


def draw_line(offset, length, color):
    offset_part = f'{" " * offset}'
    filed_part = f'{" " * length}'
    line = f'{offset_part}{CSI}48;5;{color}m{filed_part}{RESET}'
    print(line)


#first task flag
for i in [220, 2, 9]:
    draw_line(0, 23, i)
    draw_line(0, 23, i)
print()



#Fird task graph
m = []
for i in range(1, 10):
    print(f'{CSI}48;5m{str(10 - i) + " "}{RESET}', end = "")
    for j in range(0, 10):
        if i == (9 - j):
            print(f'{CSI}31;47m  {RESET}', end = "")
        else:
            print(f'{CSI}48;5m  {RESET}', end = "")
    print()
for i in range(10):
    print(str(i) + " ", end="")
print('\n')
time.sleep(1)

#Fourth information processing test
with open("sequence.txt") as f:
    data = f.read()
values = [abs(float(num)) for num in data.split('\n')]
oddvalue = 0
notoddvalue = 0
for i in range(0, len(values)):
    if (i % 2 == 0):
        notoddvalue += values[i]
    else:
        oddvalue += values[i]

allvalues = oddvalue + notoddvalue
first_percent = (oddvalue / allvalues) * 100 
second_percent = (notoddvalue / allvalues) * 100
print('Нечётные позиции', f'{CSI}48;5;{1}m{" " * round(first_percent) }{ str(round(first_percent, 2))}{RESET}')
print('Чётные позиции  ', f'{CSI}48;5;{2}m{" " * round(second_percent) + str(round(second_percent, 2))}{RESET}')
print()
time.sleep(1)

#Fifth (additional) task
l = [[0, 1, 3], 
     [15, 4, 1], 
     [0, 3, 15]]
ll = ["Германия               ", 
      "Россия                 ", 
      "Российская Империя     "]
while True:
    for color in range(len(l)):
        draw_line(0, 23, l[color][0])
        draw_line(0, 23, l[color][0])

        draw_line(0, 23, l[color][1])
        draw_line(0, 23, l[color][1])
            
        draw_line(0, 23, l[color][2])
        draw_line(0, 23, l[color][2])
        print(ll[color])
        time.sleep(1)
        print(f"{CSI}1G{CSI}{7}A", end="")
