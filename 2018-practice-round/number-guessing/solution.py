import sys

t = int(input())

for i in range(1, t + 1):
    a, b = [int(i) for i in input().split(" ")]
    l, u = [a+1, b]
    guesses = []
    n = int(input())
    for j in range(1, n + 1):
        guess = int((l+u)/2)
        guesses.append(guess)
        print("{}".format(guess),flush=True)
        result = input()
        if result == "TOO_BIG":
            u = guess
        elif result == "TOO_SMALL":
            l = guess + 1
        elif result == "CORRECT":
            break
        else:
            print("a:{},b:{},l:{},u:{},guess:{}".format(a,b,l,u,guesses))
            sys.exit("{}".format(result))
sys.exit()