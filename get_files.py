import json
import sys

try:
    with open('schedule.json', 'r') as f:
        schedule_data = json.load(f)
    
    day = sys.argv[1]
    print(f'Looking for day {day} in schedule', file=sys.stderr)
    
    files = schedule_data['schedule'].get(str(day), [])
    print(f'Found files: {files}', file=sys.stderr)
    
    if not files:
        print(f'No files scheduled for day {day}', file=sys.stderr)
        sys.exit(1)
    
    # Output ONLY the JSON to stdout
    print(json.dumps(files))
    
except Exception as e:
    print(f'Error reading schedule: {e}', file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit(1)
