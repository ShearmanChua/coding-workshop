import re
from itertools import count


def reset_defaults():
    return '', -1


def check_function_call(quotes):
    for quote in quotes:
        function_calls = re.findall(r'(?:\)->)?\w+\(', quote)
        if any(')->' not in call for call in function_calls):
            return True
    return False


def check_string_concatenation(quotes):
    return any('+' in quote for quote in quotes)


def check_not_variable(quotes):
    return any(re.findall(r'\W', var) and ')->' not in var for var in quotes)


line_to_check, start_idx = reset_defaults()
for idx in count(start=1):
    try:
        input_line = input()

        # ignore lines starting with comments
        if input_line.startswith('//'):
            continue
        
        line_to_check += input_line

        # remove characters after comments (https://www.rosettacode.org/wiki/Strip_comments_from_a_string#Regular_expressions)
        # m = re.match(r'([^//]*)//(.*)$', line_to_check)
        # if m:
        #     line_to_check = m.group(1)

        # remove characters after comments
        line_to_check = line_to_check.split('//')[0]

        # remove leading and trailing spaces
        line_to_check = re.sub(r'^ +| +$', '', line_to_check)
        
        # ignore if line doesnt start with 'logger.debug'
        if not line_to_check.startswith('logger.debug'):
            continue

        if start_idx == -1:
            start_idx = idx

        # dont continue if line doesnt end with ';'
        if not line_to_check.endswith(';'):
            continue
            
        # only keep string inside logger.debug statements
        line_to_check = re.sub(r'\);$', '', line_to_check)
        line_to_check = re.sub(r'^logger.debug\(', '', line_to_check)
        
        # remove all whitespace
        line_to_check = re.sub(' ', '', line_to_check)
        # print(f'line_to_check {start_idx}: {line_to_check}')
        
        # get all strings outside "", separated by ','
        outside_quotes = re.sub(r'"[^"]+"|(["]+)', ' ', line_to_check).split()
        outside_quotes = [item for quote in outside_quotes for item in (quote.split(',')[1:] if quote.startswith(',') else [quote])]
        # print(f'outside_quotes: {outside_quotes}')
        
        # check outside_quotes for function calls (lambda is ok)
        if check_function_call(outside_quotes):
            # print('function call not lambda detected')
            print(start_idx)
            line_to_check, start_idx = reset_defaults()
            continue
            
        # check outside_quotes for string concatenation
        if check_string_concatenation(outside_quotes):
            # print('string concatenation detected')
            print(start_idx)
            line_to_check, start_idx = reset_defaults()
            continue
            
        # check outside_quotes for anything that is not a variable
        if check_not_variable(outside_quotes):
            # print('not a variable detected')
            print(start_idx)
            line_to_check, start_idx = reset_defaults()
            continue
        
        line_to_check, start_idx = reset_defaults()

    except EOFError:
        break


# Check for:
# 1. Function calls (function() outside "")
# 2. Str concat (check for + sign outside "")
# 3. lambda function OK (() -> check outside "")
# 4. Arithmetic Operators (check for not variables outside "")
# 5. Multi-line print first line only (check if closing ) on the same line and get whole line by checking for EOL;)
# 6. Ignore comments (check for //)
# 7. Each line check before comments (//)
# 8. Check for logger.debug()



# logger.debug(hello());  //prob
# logger.debug(hello + ()->hello());  //prob
# logger.debug(hello + (a)->hello(b));  //prob
# logger.debug(()->hello() + hello);  //prob
# logger.debug("We have " + getUserCount() + ()->getUserCount() + hi);  //prob
# logger.debug("We have " + getUserCount + ()->getUserCount() + hi);  //prob
# logger.debug("We have " + getUserCount + getUserCount() + hi);  //prob
# logger.debug("We have " + getUserCount() + " users" + ()->getUserCount());  //prob
# logger.debug("We have " + getUserCount(a,b) + " users" + (3,4)->getUserCount(1,2));  //prob
# logger.debug(ok + "We have " + getUserCount() + " users" + ()->getUserCount());  //prob
# logger.debug(ok + "We have " + getUserCount(f) + " users" + ()->getUserCount());  //prob
# logger.debug(ok + "We have " + ()->getUserCount() + " users" + ()->getUserCount());  //prob
# logger.debug(ok + "We have " + (la)->getUserCount(la) + " users" + (bb)->getUserCount(bb));  //prob
# logger.debug("We have {} users.", getUserCount(), test1);  //prob
# logger.debug("We have {} users.", getUserCount(la), test1);  //prob
# logger.debug("a + b = {}", a+b);  //prob
# logger.debug("a + b = {}", a, b==c);  //prob
# logger.debug("a + b = {}", ab, b-c);  //prob
# logger.debug("a + b = {}", a!=b);  //prob
# logger.debug("a + b = {}", a>b);  //prob
# logger.debug("a + b = {}", ab, c*d);  //prob
# logger.debug(hello);
# logger.debug(()->hello());
# logger.debug("We have {} users.", ()->getUserCount(), test1);
# logger.debug("We have {} users.", (ab)->getUserCount(ab), test1);
# logger.debug("We have {} users.", getUserCount, ()->test1());
# logger.debug("a + b = {}", ab, cd, e_f);
