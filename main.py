import numpy as np
import datetime
def main(x):
    date = datetime.date.strptime(x, "%m/%d/%y")
    month = date.hour
    

if __name__ == '__main__':
    main('3/11/2023')


