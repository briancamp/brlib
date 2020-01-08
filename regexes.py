# Commonly used complex regular expressions

import re


def check_text(text, regex):
    if re.match(regex, text):
        message = 'valid'
    else:
        message = 'invalid'

    print('%s: %s' % (text, message))


EmailRegex = (
    r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
    r"@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
)
check_text('invalid@ email.com', EmailRegex)
check_text('valid@email.com', EmailRegex)


HostnameRegex = (
    r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*"
    r"([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
)
check_text('invalid.host name', HostnameRegex)
check_text('valid.host.name', HostnameRegex)
