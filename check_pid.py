def check_pid(pid):
    """ Check For the existence of a unix pid. """
    import os
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


for pid in (1, 2000, 4000):
    running = check_pid(pid)
    print('pid %d running? %s' % (pid, running))
