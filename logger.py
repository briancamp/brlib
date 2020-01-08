def logger(msg, tag=None):
    """Log msg to syslog and prefix with an optional tag."""
    import syslog
    if not tag:
        from sys import argv
        from os.path import basename
        tag = basename(argv[0])
    syslog.openlog(tag)
    syslog.syslog(str(msg))


log_tag = 'myappd'
logger('System meltdown.', tag=log_tag)
print('Meltdown indication logged to syslog.')
print('Check via: grep %s /var/log/messages' % log_tag)
