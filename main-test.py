from main import Add

def TestAdd():
    assert Add(1,2) == 3
    print("Add function works properly!")

if __name__ == '__main__':
    TestAdd()