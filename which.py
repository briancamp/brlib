def which(executable):
    """Equivalent of witch(1). Returns the path (if any) of executable."""
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(executable)
    if fpath:
        if is_exe(executable):
            return executable
    else:
        for path in os.environ['PATH'].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, executable)
            if is_exe(exe_file):
                return exe_file
    return(None)


executables = [
    'ls',
    'fdisk',
    'somescript',
    'python',
]
print('Checking paths...')
for executable in executables:
    exec_path = which(executable)
    print('%s: %s' % (executable, exec_path))
