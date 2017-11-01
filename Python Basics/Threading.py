import threading

#to make a class run in parallel, need to  inherit methods from threading
class parallel_Method_Running(threading.Thread):
    #need to define a method named run
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            print(threading.get_ident)


insta1 = parallel_Method_Running(name='Method1')
insta2 = parallel_Method_Running(name='Method2')
insta1.start()
insta2.start()



