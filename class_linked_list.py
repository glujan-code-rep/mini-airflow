import os
import time
from multiprocessing import Process

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data.__name__)
            temp = temp.next

    def executeList(self):
        temp = self.head
        if os.fork() != 0:  # <--
            return
        while (temp):
            temp.data()
            temp = temp.next
            #time.sleep(3)

if __name__=='__main__':

    def run21():
        with open('test.txt','a') as f:
            f.write('test\n')
        #print('soy guillermo')
        #time.sleep(3)
        #exit()
        with open('test.txt','a') as f:
            f.write('test 2')

    def run1():
        pid = os.getpid()        
        with open('/home/guillorocker/Escritorio/dags/test.txt','a') as f:
            f.write('2: {}\n'.format(pid))
        #time.sleep(3)
    
    def run2():
        pid = os.getpid()  
        with open('/home/guillorocker/Escritorio/dags/test.txt','a') as f:
            f.write('3: {}\n'.format(pid))
        #print('Soy guillermo')
        #time.sleep(3)

    

    def run3():
        with open('/home/guillorocker/Escritorio/dags/test.txt','a') as f:
            f.write('Chau\n')
        #print('Chau')
        #time.sleep(3)

    llist = LinkedList()

    llist.head = Node(run1)
    second = Node(run2)
    third = Node(run3)

    llist.head.next = second

    second.next = third

    pid = os.getpid()
    with open('/home/guillorocker/Escritorio/dags/test.txt','a') as f:
        f.write('1: {}\n'.format(pid))
    p = Process(target=llist.executeList)
    p.start()
    p.join()

    print('done')

    #llist.printList()

    #llist.executeList()


    
    #print(third.next)


        