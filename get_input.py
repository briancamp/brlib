

def get_input(prompt, expr=None, get_bool=False, validator=None,
              menu=None, error_text='Invalid.  Try again.',
              series=False):
    """Get input from the user with prompt and apply optional validation."""
    import re
    while 'final_answer' not in locals():
        if menu:
            digits = len(str(len(menu)))
            print('%s\n' % prompt)
            for i in range(0, len(menu)):
                line_text = menu[i] if isinstance(menu[i], str) else menu[i][1]
                print('(%s) %s' % (repr(i + 1).rjust(digits), line_text))
            print('')
            answer = input('Enter selection number: ')
        else:
            answer = input(prompt)

        if not expr and not get_bool and not validator and not menu:
            final_answer = answer
        elif expr and re.search(expr, answer):
            final_answer = answer
        elif get_bool and re.search('^(ye?s?|no?)$', answer):
            final_answer = (True if re.search('^ye?s?$', answer) else False)
        elif validator and validator(answer):
            final_answer = answer
        elif (menu and
              re.search(r'^\d+$', answer) and
              int(answer) < len(menu) + 1):
            if isinstance(menu[int(answer) - 1], str):
                final_answer = menu[int(answer) - 1]
            else:
                final_answer = menu[int(answer) - 1][0]
        else:
            print(error_text)

    if series:
        if get_input('Another? ', get_bool=True):
            return(
                [final_answer] + get_input(
                    prompt, expr=expr, get_bool=get_bool,
                    error_text=error_text, series=True
                )
            )
        else:
            return([final_answer])
    else:
        return(final_answer)


first_name = get_input('First name? ', expr=r'^[\w]+$',
                       error_text='Letters only, try again.')
pony = get_input('Do you want a pony? ', get_bool=True)

if pony:
    want_str = "want"
else:
    want_str = "don't want"

print('Your name is %s and you %s a pony.' % (first_name, want_str))
