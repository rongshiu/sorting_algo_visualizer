
# coding: utf-8

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


def bubble_sort(array):
    issorted=False
    counter=0
    while issorted==False:
        issorted=True
        for i in range(len(array)-1-counter):
            if array[i]>array[i+1]:
                swap(i,i+1,array)
                issorted=False
            yield array
        counter +=1
    

def insertion_sort(array):
    for i in range(1,len(array)):
        for j in reversed(range(1,i+1)):
            if array[j] < array[j-1]:
                swap(j,j-1,array)
            yield array

def selection_sort(array):
    i=0
    while i<len(array)-1:
        curr_smallest=i
        for j in range(i+1,len(array)):
            if array[curr_smallest]>array[j]:
                curr_smallest=j
        swap(i,curr_smallest,array)
        i+=1
        yield array
        
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = array[end]
    pivotIdx = start
    for i in range(start, end):
        if array[i] < pivot:
            swap(i, pivotIdx, array)
            pivotIdx += 1
        yield array
    swap(end, pivotIdx, array)
    yield array

    yield from quick_sort(array, start, pivotIdx - 1)
    yield from quick_sort(array, pivotIdx + 1, end)

def swap(i,j,array):
    array[i],array[j]=array[j],array[i]


if __name__=='__main__':
    N=int(input('Enter number of integers to be sorted: '))
    M=str(input('\nPlease choose method of sorting:\n(b)Bubble Sort\n(i)Insertion Sort\n(q)Quick Sort\n(s)Selection sort\n'))
    
    array=[]
    for n in range(1,N+1):
        array.append(n) 
    random.shuffle(array)
    
    if M=='b':
        title='Bubble Sort'
        generator=bubble_sort(array)
    elif M=='i':
        title='Insertion Sort'
        generator=insertion_sort(array)
    elif M=='s':
        title='Selection Sort'
        generator=selection_sort(array)
    elif M=='q':
        title='Quick Sort'
        generator=quick_sort(array,0,len(array)-1)
    else:
        print('Invalid Method Selected')

    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(array)), array, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update_fig(array, rects, iteration):
        for rect, val in zip(rects, array):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()    

