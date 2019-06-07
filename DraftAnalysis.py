from Helpers import *
import operator

class DraftAnalysis:
    def __init__(self, drafts):
        self.total = len(drafts)
        self.sources = get_counts(drafts, "source")
        self.players = []

        for draft in drafts:
            self.players.extend(draft.players)

    def print_total(self):
        print("Total Mocks: {}".format(self.total))

    def print_sources(self):
        print("Sources:")
        for key, value in self.sources.items():
            print("\t{}: {}".format(key, value))

    def print_most_frequent(self):
        player_counts = get_counts(self.players, "name")
        
        print("Most Frequently Drated Players:")
        for key, value in sorted(player_counts.items(), key=operator.itemgetter(1), reverse=True):
            print("\t{}: {}%".format(key, int(value / self.total * 100)))


    def print_most_frequent_by(self, attr: str):
        position_counts = get_counts(self.players, attr)

        print("Most Frequently Drafted Players (By {}):".format(attr))
        for position, position_total in position_counts.items():
            print("\t{}:".format(position))
            players = get_counts([player for player in self.players if getattr(player, attr) == position], "name")

            for player, count in sorted(players.items(), key=operator.itemgetter(1), reverse=True):
                print("\t\t{}: {}%".format(player, int(count / position_total * 100)))

    def print_average_round_drafted_by(self, attr: str):
        counts = get_counts(self.players, attr)

        print("Average Round Drafted (By {})".format(attr))
        for key, value in counts.items():
            i = [player.drafted for player in self.players if getattr(player, attr) == key]
            print("\t{}: {}".format(key, sum(i) / len(i)))


