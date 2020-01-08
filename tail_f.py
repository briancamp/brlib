def tail_f(filename, timeout=None):
    """Run the system's "tail -n0 -F" on filename and yield each line."""
    import os
    import select
    import subprocess
    sp = subprocess.Popen(['tail', '-n0', '-F', filename], bufsize=0,
                          stdout=subprocess.PIPE, stderr=open(os.devnull, "w"))
    while True:
        sp_select = select.select([sp.stdout], [], [], timeout)
        if not sp_select[0]:
            raise Exception(
                'tail on "%s" recieved no input for %s seconds.' %
                (filename, timeout))
        line_bytes = sp.stdout.readline()
        line = line_bytes.decode('utf-8').rstrip('\n')
        if not line:
            break   # will only happen if tail is killed
        yield line


file_name = '/var/log/messages'
print('Running tail_f on %s. Hit Ctrl-C to stop.' % file_name)
try:
    for line in tail_f(file_name):
        print(line)
except KeyboardInterrupt:
    pass
