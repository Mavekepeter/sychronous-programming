import time

def fetch_data():
    print("start fetching")
    time.sleep(2) # simulating  a blocking i/o operation
    print("Down fetching")
    return{'data':1}

def print_numbers():
    for i in range (30):
        print(i)
        time.sleep(1)
     
def main():
    value=fetch_data()
    print(value)
    print_numbers()
    
    
main()