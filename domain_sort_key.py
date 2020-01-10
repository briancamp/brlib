def domain_sort_key(domain):
    """Key to sort hosts / domains alphabetically, by domain name."""
    import re
    domain_expr = r'(.*\.)?(.*\.)(.*)'  # Eg: (www.)(google.)(com)
    domain_search = re.search(domain_expr, domain)

    if domain_search and domain_search.group(1):
        # sort by domain name  and then everything left of
        # Eg: google, com, www
        domain_values = (
            domain_search.group(2),
            domain_search.group(3),
            domain_search.group(1)
        )
        key = '%s%s%s' % domain_values
    else:
        # no host portion, just return the domain name
        key = domain
    return(key)


domains = ['www.google.com', 'cnn.com', 'mail.google.com', 'www.bing.com']
print('before: %s' % domains.__repr__())
domains.sort(key=domain_sort_key)
print('after: %s' % domains.__repr__())
