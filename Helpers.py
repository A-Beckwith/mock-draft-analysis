import xlrd

class Player:
    def __init__(self, name, team, position, drafted, depth):
        self.name = name
        self.team = team
        self.position = position
        self.drafted = drafted
        self.depth = position + str(depth)

class Draft:
    def __init__(self, source, date):
        self.source = source
        self.date = date
        self.players = []
        self.counts = {
            "QB": 0,
            "RB": 0,
            "WR": 0,
            "TE": 0,
            "DST": 0,
            "K": 0
        }

    def add_player(self, name, team, position, drafted):
        self.counts[position] += 1
        self.players.append(Player(name, team, position, drafted, self.counts[position]))

def get_drafts(wb):
    i = 0
    drafts = []
    while i < wb.ncols:
        draft = Draft(wb.cell_value(0,i), wb.cell_value(0,i+1))

        for n, t, p, r in [wb.row_values(n, i, i+4) for n in range(1,16)]:
            draft.add_player(n, t, p, r)

        drafts.append(draft)
        i += 5
    
    return drafts


def get_counts(players, attr):
    temp = dict()

    for player in players:
        i = getattr(player, attr)
        try:
            temp[i] += 1
        except:
            temp[i] = 1

    return temp