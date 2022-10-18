'''Calculate scores'''

from sys import stdin, stdout
import math
import bisect

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

class Challenge:
    def __init__(self):
        self.unique_lang = []
        self.highest_score = 0.0
        self.accepted = False
    def calculate_score(self, score, language, status_of_submission):
        bonus_score = 0.0
        first_submission = False

        if score > self.highest_score:
            self.highest_score = score

        if status_of_submission == 'Accepted':
            if not self.accepted:
                self.accepted = True
                first_submission = True
                bonus_score += score
            if language not in self.unique_lang:
                self.unique_lang.append(language)
                bonus_score += 1.0

        else:
            bonus_score += -1.0

        return bonus_score, first_submission

class Team:
    def __init__(self, team_name, first_submission):
        self.team_name = team_name
        self.first_submission = first_submission
        self.first_accepted_submission = None
        self.total_score = 0.0
        self.challenges = dict()
    def make_submission(self, submission_position, score, challenge_name, language, status_of_submission):
        if challenge_name not in self.challenges.keys():
            self.challenges[challenge_name] = Challenge()
        bonus_points, first_submission = self.challenges[challenge_name].calculate_score(score, language, status_of_submission)
        self.total_score += bonus_points
        if self.first_accepted_submission == None and first_submission:
            self.first_accepted_submission = submission_position
            return first_submission
        return False
    def calculate_total_score(self):
        for challenge in self.challenges.keys():
            self.total_score += self.challenges[challenge].highest_score
            self.total_score = round_half_up(self.total_score, 2)
        return self.total_score


teams = {}
submission_position = 0
first_submission_teams = []
first_accepted_submission_teams = []

for submission in stdin.readlines():
    submission_list = submission.strip().split(",")
    team =  submission_list[0]
    if team not in teams.keys():
        teams[team] = Team(team,submission_position)
        first_submission_teams.append(team)
    first_accepted_submission = teams[team].make_submission(submission_position, float(submission_list[1]), submission_list[2], submission_list[3], submission_list[4])
    if first_accepted_submission:
        first_accepted_submission_teams.append(team)
        first_submission_teams.remove(team)
    submission_position += 1

team_points = []
team_ranking = []

rank_by_submission = first_accepted_submission_teams + first_submission_teams
no_of_teams = len(rank_by_submission)

for team in teams.keys():
    points = teams[team].calculate_total_score()
    pos_to_insert = bisect.bisect(team_points, (points,no_of_teams-rank_by_submission.index(team)))

    team_points.insert(pos_to_insert,(points,no_of_teams-rank_by_submission.index(team)))
    team_ranking.insert(pos_to_insert,teams[team].team_name)

for idx, team in enumerate(reversed(team_ranking)):
    print("{},{},{:0.2f}".format(idx+1,team,teams[team].total_score))

