
def run1():
    print('run1')

def run2():
    print('run2')

def run3():
    print('run3')


_dict = {'run1':run2,'run3':None}

print(_dict)

name = 'run1'

_dict[name]()