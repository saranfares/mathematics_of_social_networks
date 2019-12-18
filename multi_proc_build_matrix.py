import multiprocessing

def worker():
    # do process here
    print("in worker")
    return

if __name__ == '__main__':
    jobs = []
    for i in range(10):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
