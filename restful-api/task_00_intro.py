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
        # Placeholders to replace
        keys = ["name", "event_title", "event_date", "event_location"]
        try:
            for key in keys:
                val = attendee.get(key)
                val_str = str(val) if val is not None else "N/A"
                content = content.replace("{" + key + "}", val_str)
            
            output_filename = f"output_{idx}.txt"
            if os.path.exists(output_filename):
                pass # Logic to handle existing file if needed, currently overwrites
            
            with open(output_filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error processing attendee {idx}: {e}")
