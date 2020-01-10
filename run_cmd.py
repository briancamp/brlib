def run_cmd(cmd, shell=False, input=None):
    """Run the supplied command and return a dict of its outputs."""
    from subprocess import Popen, PIPE, STDOUT
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=STDOUT, shell=shell,
              universal_newlines=True)
    stdout, stderr = p.communicate(input=input)
    exit_code = p.returncode
    return({'stdout': stdout, 'stderr': stderr, 'exit_code': exit_code})


cmd = ['ls', '-l']
cmd_out = run_cmd(cmd)

print('Command: %s' % ' '.join(cmd))
print('Exit code: %d' % cmd_out['exit_code'])
print('Standard out:\n%s' % cmd_out['stdout'])
print('Standard error:\n%s' % cmd_out['stderr'])
