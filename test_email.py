def test_email_addr(email_addr):
    """
    Test if email_addr is valid and has a valid domain.

    Uses the dns module included with dnspython.

    A cache of domain results is kept. Can exhaust memory if checking a
    multitude of different domains.
    """
    if 'domain_cache' not in vars(test_email_addr):
        test_email_addr.domain_cache = {}

    import dns.resolver
    import re

    # Email regex's are a real pain, so we use a (fairly) strict regex to
    # validate the email first and then a looser one to strip out
    # the components.  See
    # http://ex-parrot.com/~pdw/Mail-RFC822-Address.html
    EmailRegexStrict = (
        r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)"
        r"*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*"
        r"[a-z0-9])?"
    )
    EmailRegexLoose = r"(.+)@(.+)"

    if not re.match(EmailRegexStrict, email_addr):
        return(False)
    domain = re.match(EmailRegexLoose, email_addr).group(2)

    if domain in test_email_addr.domain_cache:
        return(test_email_addr.domain_cache[domain])

    try:
        dns.resolver.query(domain + '.', 'SOA')
        result = True
    except dns.resolver.NXDOMAIN:
        result = False
    except dns.resolver.NoAnswer:
        result = False

    test_email_addr.domain_cache[domain] = result
    return(result)


addrs = [
    'user@gmail.com',
    'invalid@address here',
    'user2112@bad-tdl.yyz',
]
print('Validating addresses...')
for addr in addrs:
    is_valid = test_email_addr(addr)
    print('%s: %s' % (addr, is_valid))
