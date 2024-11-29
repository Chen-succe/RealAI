import sys

# sys.exit('异常')
def a():
    
    # sys.exit()
    quit()
    # exit()
    print(1)
    

if __name__ == '__main__':
    for i in range(10):
        while True:
            try:
                a()
            except SystemExit as systemExit:
                print('a')
                # SystemExit(1)
                # print(e)
                
                print('b')
                # sys.exit(systemExit.code)
                break