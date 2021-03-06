"""
    TrackingTime CSV export parser for Jira

    Assumes input file is comma delimited

    Work log grouped in order of:
        Project -> Task -> Day -> Aggregated time for that day (in minutes)

"""

from utils import *
from pprint import pprint

"""
TODO
    FIX:
        Some dates may be outputting in random order
    ADD:
        Total hours worked
"""


def main():
    config = open_config("config.json")

    move_timesheet_to_working_folder(config)

    timesheet = read_input_timesheet(config)

    projects_time = read_data_to_dict(timesheet)

    pprint(projects_time, indent=4, width=1)

    write_processed_data_to_csv(config, projects_time)


if __name__ == "__main__":
    main()
