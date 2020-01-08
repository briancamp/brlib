class ExternalError(Exception):
    pass


def load_yaml(yml_txt, file_name=None, valid=None):
    """Load a YAML file and optionally apply a validator."""
    import yaml
    try:
        if file_name:
            with open(file_name) as f:
                yml_txt = f.read()
        yml = yaml.safe_load(yml_txt)
        if valid:
            valid(yml)
    except Exception as e:
        raise ExternalError(e)
    return(yml)


yaml_txt = """
debug: False
log_file: /var/log/blah
retries: 5
"""
yaml_var = load_yaml(yaml_txt)
print(yaml_var.__repr__())
