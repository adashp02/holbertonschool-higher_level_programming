"""program that generates an invite form addressed to a given atendee

Args:
    template (str)
    attendees (list(dict))

Returns:
    file based on template with placeholders replaced with data/attendees
"""
import os

def generate_invitations(template, attendees):
    """templating function that verifies
    template is a str and attendees - list of dicts
    """
if not isinstance(template, str):
    print("Error: Template is not a string.")
    return
if not isinstance(attendees, list):
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees should be a list of dictionaries.")
            return
        
"""Error handling"""
if not template:
    print("Error: Template is empty, no files generated.")
    return
if not attendees:
    print("Error: no data provided, no file generated.")
    return

"""Iterates through the list of attendees and replaces placeholders
with values from each attendee's dictionary"""

for index, attendee in enumerate(attendees, start=1):
    invitation = template
    for key in ["name", "event_title", "event_date", "event_location"]:
        value = attendee.get(key) or "N/A"
        placeholder = "{" + key + "}"
        invitation = invitation.replace(placeholder, value)

"""Write the processed template to output files named output_{index}.txt,
where {index} is the index of the attendee starting from 1"""

output_filename = f"output_{index}.txt"

"""chekcs if output file already exists before writing"""

if os.path.exists(output_filename):
    print(f"Error: The file {output_filename} already exixsts.")
    continue

try:
    with open(output_filename, 'w') as file:
        file.write(invitation)
except Exception as e:
    print(f"Error: Impossible to write file {output_filename}. Exception: {e}")
