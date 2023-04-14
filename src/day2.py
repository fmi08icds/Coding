import sys


def hello(name) :
    print ("Hello {} and welcome to the Int. Comp. for DS".format(name))


def main():
    if len(sys.argv) > 1 :
        name = str(sys.argv[1])
    else :
        name = "<NO NAME>"
        print("Program called without arguments. Please, specify your name as the first argument.")

    # Call my first function here
    hello(name)



if __name__ == '__main__':
    main()
