import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random
from time import sleep
from threading import Thread

## Hadriel Benjo

fileName = 'example.txt'

def threadPlt():
    print('execute : threadPlt\n')
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    style.use('seaborn-dark-palette')
    def animate(i):
        graph_data = open(fileName, 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        if len(lines) > 0:
            for line in lines:
                if len(line) > 1:
                    x, y = line.split(',')
                    xs.append(int(x))
                    ys.append(int(y))
                    
        ax.clear()
        ax.plot(xs,ys)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

    print('finished : threadPlt\n')


def threadRandomNumber():
    print('execute : threadRandomNumber\n')

    x = 0
    #maxVal = 0
    randTill = 5
    while x < 100:
        y = random.randint(0,randTill)
        line = '' + str(x) + ',' + str(y) + '\n'

        file = open(fileName, "a")
        file.write(line)
        file.close()

        #if maxVal < y: maxVal = y+5
        #ax.set_yticks(list(range(0,maxVal+1,5)))
        print('Write new line: ', line)

        randTill += 5
        x += 1
        sleep(2)
        
    
    
    print('finished : threadRandomNumber\n')


if __name__ == "__main__":
    print('Started..')
    
    
    thread1 = Thread(target = threadPlt, args = [])
    thread2 = Thread(target = threadRandomNumber, args = [])
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    print('Finished!')
