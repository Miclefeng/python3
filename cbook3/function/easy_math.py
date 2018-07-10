from operator import add, sub
from random import randint, choice

ops = {'+': add, '-': sub}
MAXTRIES = 2


def doprob():
    op = choice('+-')
    #     print(op)
    nums = [randint(1, 10) for i in range(MAXTRIES)]
    nums.sort(reverse=True)
    #     print(nums)
    ans = ops[op](*nums)
    #     print(ans)
    pr = '{:d} {:s} {:d} = '.format(nums[0], op, nums[1])
    #     print(pr)
    oops = 0

    while True:
        try:
            if int(input(pr)) == ans:
                print('correct')
                break
            if oops == MAXTRIES:
                print('answer\n{:s}{:d}'.format(pr, ans))
            else:
                print('incorrect... try again')
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print('invalid input... try again')


def main():
    while True:
        doprob()
        try:
            opt = input('Again? [y/n] : ').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == '__main__':
    main()