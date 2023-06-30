import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from random import randint, random

fig = plt.figure(figsize=(8,6))
axes = fig.add_subplot(1,1,1)
plt.style.use("seaborn")

animationCounter = 0

palette = list(reversed(sns.color_palette("seismic", 2).as_hex()))
input1 = input()

randomlimiter = 10
randomlimiterbottom = 0

def animate(i):
    fun = 0
    i = fun

    global randomlimiter
    global randomlimiterbottom
    
    UpVotes    = randint(randomlimiterbottom, randomlimiter)
    DownVotes  = randint(randomlimiterbottom, randomlimiter)
    LeftVotes  = randint(randomlimiterbottom, randomlimiter)
    RightVotes = randint(randomlimiterbottom, randomlimiter)
    AVotes     = randint(randomlimiterbottom, randomlimiter)
    BVotes     = randint(randomlimiterbottom, randomlimiter)
    StartVotes = randint(randomlimiterbottom, randomlimiter)

    randomlimiter = randomlimiter + 10
    randomlimiterbottom = randomlimiterbottom + 10

    DataUpVotes    = randint(UpVotes, randomlimiter)
    DataDownVotes  = randint(DownVotes, randomlimiter)
    DataLeftVotes  = randint(LeftVotes, randomlimiter)
    DataRightVotes = randint(RightVotes, randomlimiter)
    DataAVotes     = randint(AVotes, randomlimiter)
    DataBVotes     = randint(BVotes, randomlimiter)
    DataStartVotes = randint(StartVotes, randomlimiter)
    global animationCounter
    animationCounter += 1

    if animationCounter == 16:
        ani.event_source.stop()
        animationCounter = 0

        inputresult = {'Up': DataUpVotes, 'Down': DataDownVotes, 'Left' : DataLeftVotes, 'Right' : DataRightVotes, 'A' : DataAVotes, 'B' : DataBVotes, 'Start' : DataStartVotes}
        winner = max(inputresult, key=inputresult.get)
        print(winner, 'got the most votes')

        plt.close(fig)

    plt.barh(['Up', 'Down', 'Left', 'Right', 'A', 'B', 'Start'], [DataUpVotes,DataDownVotes,DataLeftVotes,DataRightVotes,DataAVotes,DataBVotes,DataStartVotes], color=palette)

if input1 == "start":
    ani = FuncAnimation(fig, animate, interval=1000, repeat=True)
    input1 == "empty"

plt.show()