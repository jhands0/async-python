import queue

def task(name, work_queue):
    if work_queue.empty():
        print(f"Task {name} nothing to do")
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            print(f"Task {name} running")
            for x in range(count):
                total += 1
            print(f"Task {name} total: {total}")

def main():
    """
    This is the main entry point for the program
    """
    
    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    tasks = [(task, "One", work_queue), (task, "Two", work_queue)]

    for t, n, q in tasks:
        t(n, q)

if __name__ == '__main__':
    main()