def mkdir_p(path):
    """Make directories for the full path, like mkdir -p."""
    import os
    import errno
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


mkdir_p('my_dir/hi/test')
print('Run, check via: find my_dir')
