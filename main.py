#!/usr/bin/python
 # -*- coding: utf-8 -*-
from queue import Queue

class process:
    '''
    a process cointains:
        PID
        priority
        offset
        num_of_blocks
        printer
        scanner
        modems
        drivers
    '''
    def __init__(self, n_PID, n_priority, n_offset, n_num_of_blocks, n_printer, n_scanner, n_modems, n_drivers):
        self.PID = n_PID
        self.priority = n_priority
        self.offset = n_offset
        self.num_of_blocks = n_num_of_blocks
        self.printer = n_printer
        self.scanner = n_scanner
        self.modems = n_modems
        self.drivers = n_drivers

    def printProcess(self):
        print('  PID: {}\n  priority: {}\n  offset: {}\n  num_of_blocks: {}\n  printer: {}\n  scanner: {}\n  modems: {}\n  drivers: {}\n\n\n'.format(self.PID, self.priority, self.offset, self.num_of_blocks, self.printer, self.modems,self.scanner, self.drivers))



real_time = Queue()
priority_1 = Queue()
priority_2 = Queue()
priority_3 = Queue()

def sizeOfAllQueues():
    return real_time.qsize() + priority_1.qsize() + priority_2.qsize() + priority_3.qsize()

def putInQueue(process):
    if sizeOfAllQueues()<1000:
        if process.priority == 0:
            real_time.put()
        elif process.priority == 1:
            priority_1.put()
        elif process.priority == 2:
            priority_2.put()
        else:
            priority_3.put()
    
def getFromQueue():
    if real_time.qsize() != 0:
        return real_time.get()
    elif priority_1.qsize() != 0:
        return priority_1.get()
    elif priority_2.qsize() != 0:
        return priority_2.get()
    else:
        return priority_3.get()


def createAllProcesses():
    file_of_processes = open('files/processes.txt','r')
    #print(file_of_processes.read())

    all_processes = file_of_processes.read()

    all_processes = all_processes.split('\n')

    #print(all_processes)

    for i_process in all_processes:
        if i_process == '':
            continue
        i_process = i_process.split(', ')
        print(i_process)
        #print(len(i_process))
        if len(i_process) == 8:
            new_process = process(i_process[0], i_process[1], i_process[2], i_process[3], i_process[4], i_process[5], i_process[6], i_process[7])

            new_process.printProcess()


def main():
    print('olá\n')
    print(sizeOfAllQueues())


    createAllProcesses()
if __name__ == '__main__':
    main()
