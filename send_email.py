

def send_email(to_addrs, subject, from_addr, body='',
               attachment_names=None, mono_spaced=True, mono_big=True):
    """Send an email using the local MTA."""
    import os
    import smtplib
    import email
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    if isinstance(to_addrs, str):
        to_addrs = [to_addrs]
    if isinstance(attachment_names, str):
        attachment_names = [attachment_names]

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addrs)
    msg.preamble = body

    if mono_spaced and mono_big:
        body = '<html><body><big><pre>%s</pre></big></body></html>' % body
    elif mono_spaced:
        body = '<html><body><pre>%s</pre></body></html>' % body
    msg.attach(MIMEText(body, 'html'))

    if attachment_names:
        for attachment_name in attachment_names:
            part = email.mime.Base.MIMEBase('application', 'octet-stream')
            with open(attachment_name) as f:
                part.set_payload(f.read())
            email.Encoders.encode_base64(part)
            attachment = ('attachment; filename=%s' %
                          os.path.basename(attachment_name))
            part.add_header('Content-Disposition', attachment)
            msg.attach(part)

    smtp = smtplib.SMTP('localhost')
    smtp.sendmail(from_addr, to_addrs, msg.as_string())
    smtp.quit()


from_addr = '"Example Mailer" <noreply@example.com>'
try:
    send_email('enduser@example.com', 'A message from brlib', from_addr,
               body='Just a test message, disregard')
except ConnectionRefusedError:
    print('Example only works when a local MTA is configured.')
