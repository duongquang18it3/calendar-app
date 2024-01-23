import streamlit as st
import calendar
from datetime import date

def main():
    st.title("Basic Calendar App")

    # Get the current date
    today = date.today()

    # Create a calendar for the current month
    cal = calendar.monthcalendar(today.year, today.month)

    # Display the current month and year
    st.header(calendar.month_name[today.month] + " " + str(today.year))

    # Create a table to display the calendar
    st.table(create_calendar_table(cal))

def create_calendar_table(month_calendar):
    # Create a table header with weekday names
    table = [["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]]

    # Fill in the table with day numbers
    for week in month_calendar:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            else:
                row.append(str(day))
        table.append(row)

    return table

if __name__ == "__main__":
    main()

