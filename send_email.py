

def send_email(to_addrs, subject, from_addr, body='', attachment_names=None,
               mono_spaced=True, mono_big=True, html_nolink=True):
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

    # Build a list of html components and then join them
    body_html_lines = [body]
    if mono_spaced:
        # Add <pre> tags
        body_html_lines.insert(0, '<pre>')
        body_html_lines.append('</pre>')
        if mono_big:
            # Add <big> tags
            body_html_lines.insert(0, '<big>')
            body_html_lines.append('</big>')
    if html_nolink:
        # Add <a rel=nofollow> tags, to keep mail clients from automatically
        # creating hyperlinks.
        body_html_lines.insert(
            0, '<a rel="nofollow" style="text-decoration:none; color:#333">')
        body_html_lines.append('</a>')
    body_html = '\n'.join(body_html_lines)
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
