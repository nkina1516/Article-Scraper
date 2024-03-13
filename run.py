#You can run this code by entering: python3 run.py

import os
from Module1 import mod1
from Module2 import mod2

def main():

    # Process data from Module1
    mod1.main()

    # Process data from Module2
    mod2.main()

if __name__ == "__main__":
    main()
