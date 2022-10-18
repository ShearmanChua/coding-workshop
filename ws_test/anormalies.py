'''Anomalies In Logs'''

from sys import stdin, stdout

from pyparsing import line

# Only one login is allowed er user at a time.
# It is an anomaly if there is a logout when the user is not logged in or there is a login when the user is already logged in.

# one line per event, chronologically sorted
# each event is of the form ‘login userid time’ or ‘logout userid time’, where userid is a string of U alphanumeric characters, and time is a string of exactly T characters.

class LoginTracker:
    def __init__(self):
        self.login_dict = dict()
    def check_if_logged_in(self,user):
        return user in self.login_dict.keys()
    def login(self,user,time):
        self.login_dict[user] = time
    def logout(self,user):
        del self.login_dict[user]

login_tracker = LoginTracker()
line_tracker = 1

for log in stdin.readlines():
    if log[:5] == 'login':
        if login_tracker.check_if_logged_in(log.split(' ')[1]):
            print("{} ".format(line_tracker) + log.strip())
        else:
            login_tracker.login(log.split(' ')[1],log.split(' ')[2])
    elif log[:5] == 'logou':
        if login_tracker.check_if_logged_in(log.split(' ')[1]):
            login_tracker.logout(log.split(' ')[1])
        else:
            print("{} ".format(line_tracker) + log.strip())
    
    line_tracker += 1
