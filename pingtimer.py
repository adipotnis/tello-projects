# import the necessary packages
from threading import Thread


class pingtimer:
    def __init__(self, src=0, name="timer"):

        # initialize the thread name
        self.name = name
        self.duration = 0
        # initialize the variable used to indicate if the thread should
        # be stopped
        self.stopped = False

    def start(self, duration = 0):
        # start the thread to read frames from the video stream
        self.duration = duration
        t = Thread(target=self.update, name=self.name, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        # keep looping infinitely until the thread is stopped
        while True:
            # if the thread indicator variable is set, stop the thread
            pingtimer.sleep(self.duration)
            print(1)
            if self.stopped:
                print('thread exit successfully')
                return

    def stop(self):
        # indicate that the thread should be stopped
        self.stopped = True

t = pingtimer()
t.start(duration=2)
pingtimer.sleep(10)
t.stop()
