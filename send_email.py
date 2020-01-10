

def send_email(to_addrs, subject, from_addr, body='',
               attachment_names=None, mono_spaced=True, mono_big=True):
    """
    Send an email using the local MTA.

    The body is sent as text and a multi-part <pre>'ed block.
    """
    import smtplib
    from email.message import EmailMessage

    if isinstance(to_addrs, str):
        to_addrs = [to_addrs]
    if isinstance(attachment_names, str):
        attachment_names = [attachment_names]

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)
    msg.preamble = body

    if mono_spaced and mono_big:
        body_html = '<html><body><big><pre>%s</pre></big></body></html>' % body
    elif mono_spaced:
        body_html = '<html><body><pre>%s</pre></body></html>' % body
    msg.add_alternative(body_html, subtype='html')

    if attachment_names:
        for attachment_name in attachment_names:
            with open(attachment_name, 'rb') as f:
                attachment_data = f.read()
            msg.add_attachment(
                attachment_data,
                maintype='application', subtype='octet-stream',
                filename=attachment_name
            )

    smtp = smtplib.SMTP('localhost')
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    smtp.quit()


from_addr = '"Example Mailer" <noreply@example.com>'
try:
    send_email('enduser@example.com', 'A message from brlib', from_addr,
               body='Just a test message, disregard')
except ConnectionRefusedError:
    print('Example only works when a local MTA is configured.')
