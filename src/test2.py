from curtsies import Input
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow

print(yellow('this prints normally, not to the alternate screen'))
with Input() as input_generator:
    for c in input_generator:
        if c == '<ESC>':
            break
        elif c == '<SPACE>':
            print(red('SPACE'))
        else:
            print(c)
