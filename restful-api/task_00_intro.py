import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(x, dict) for x in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for idx, attendee in enumerate(attendees, start=1):
        content = template
        try:
            content = content.replace("{name}", str(attendee.get("name") or "N/A"))
            content = content.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
            content = content.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
            content = content.replace("{event_location}", str(attendee.get("event_location") or "N/A"))
            
            output_filename = f"output_{idx}.txt"
            with open(output_filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error processing attendee {idx}: {e}")
