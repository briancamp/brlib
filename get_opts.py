DefaultConfigFile = '/dev/null'


def load_yaml(yml_txt, file_name=None, valid=None):
    pass


def get_opts():
    """Argument parser."""
    import argparse
    global Debug
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_file', '-c', type=str,
                        default=DefaultConfigFile)
    parser.add_argument('--debug', '-d', action='store_true')
    args = parser.parse_args()

    def valid_cfg(cfg):
        cfg['opt1']
        cfg['opt2']

    config = load_yaml(None, file_name=args.config_file, valid=valid_cfg)
    args.config = config
    Debug = args.debug
    return(args)


options = get_opts()
print('Config File: %s' % options.config_file)
print('Debugging enabled? %s' % options.debug)
print('Try with --help.')
