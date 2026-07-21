#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
"""
import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template
    and a list of attendees.
    """
    # 1. Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # 2. Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # 3. Handle empty list of objects
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 4. Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name")
        if name is None:
            name = "N/A"

        event_title = attendee.get("event_title")
        if event_title is None:
            event_title = "N/A"

        event_date = attendee.get("event_date")
        if event_date is None:
            event_date = "N/A"

        event_location = attendee.get("event_location")
        if event_location is None:
            event_location = "N/A"

        # Replace placeholders using string replace method
        invitation = template
        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))

        # Write to output file
        filename = f"output_{index}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(invitation)
