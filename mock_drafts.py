import xlrd
import operator
from DraftAnalysis import *
from Helpers import *
from DraftAnalysis import *

# TODO: adjust for drafts as a list
# TODO: add in round drafted

def main():
    wb = xlrd.open_workbook("./Mock_Drafts.xlsx").sheet_by_index(0)

    mock_drafts = get_drafts(wb)
    analysis = DraftAnalysis(mock_drafts)

    # analysis.print_total()
    # analysis.print_sources()
    # analysis.print_most_frequent
    analysis.print_most_frequent_by("depth")
    # analysis.print_most_frequent_by("position")
    # analysis.print_average_round_drafted_by("depth")
    # analysis.print_average_round_drafted_by("name")


main()