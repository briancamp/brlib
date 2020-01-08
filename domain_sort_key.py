def domain_sort_key(domain):
    """Key to sort domains alphabetically, by top level."""
    import re
    domain_expr = r'(.*\.)?(.*\.)(.*)'
    domain_search = re.search(domain_expr, domain)
    if (not domain_search) or (not domain_search.group(1)):
        key = domain
    else:
        key = '%s%s%s' % (domain_search.group(
            2), domain_search.group(3), domain_search.group(1))
    return(key)


domains = ['www.google.com', 'cnn.com', 'mail.google.com', 'www.bing.com']
print('before: %s' % domains.__repr__())
domains.sort(key=domain_sort_key)
print('after: %s' % domains.__repr__())
