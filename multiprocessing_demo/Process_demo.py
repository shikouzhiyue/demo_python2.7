#!usr/bin/python
# -*- coding:utf-8 -*-
import multiprocessing
import time

##实例 第一种方式
# def process(num):
#     time.sleep(num)
#     print 'Process:', num
#
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#
#     print 'CPU number:' + str(multiprocessing.cpu_count())
#     for p in multiprocessing.active_children():
#         print 'Child process name: ' + p.name + ' id: ' + str(p.pid)
#
#     print 'Process End!'

##实例 自定义类 第二种方式
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print 'Pid: ' + str(self.pid) + ' LoopCount: ' + str(count)


# if __name__ == '__main__':
#     for i in range(2, 5):
#         p = MyProcess(i)
#         p.start()

##deamon属性 如果设置为True，当父进程结束后，子进程会自动被终止。
# if __name__ == '__main__':
#     for i in range(2, 5):
#         p = MyProcess(i)
#         p.daemon =True
#         p.start()
#
#     print 'Main process end!'
## 输出结果为 Main process end!

if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon =True
        p.start()
        p.join()

    print 'Main process end!'
##每个子进程都调用了join()方法，这样父进程（主进程）就会等待子进程执行完毕。