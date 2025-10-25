#!/usr/bin/env python3
"""
Setup staging directory for daily push automation.
This script organizes all Python files into the _staging directory
according to the PUSH_SCHEDULE.md schedule.
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime, timedelta

def create_staging_structure():
    """Create the staging directory structure."""
    staging_dir = Path("_staging")
    staging_dir.mkdir(exist_ok=True)
    
    # Create subdirectories
    subdirs = ["beginner", "intermediate", "algorithms", "data_structures", "advanced", "systems"]
    for subdir in subdirs:
        (staging_dir / subdir).mkdir(exist_ok=True)
    
    return staging_dir

def copy_files_to_staging():
    """Copy all Python files to staging directory."""
    staging_dir = create_staging_structure()
    
    # Source directories
    source_dirs = ["beginner", "intermediate", "algorithms", "data_structures", "advanced", "systems"]
    
    copied_files = []
    
    for source_dir in source_dirs:
        if os.path.exists(source_dir):
            for file_path in Path(source_dir).glob("*.py"):
                dest_path = staging_dir / source_dir / file_path.name
                shutil.copy2(file_path, dest_path)
                copied_files.append(str(dest_path))
                print(f"Copied: {file_path} -> {dest_path}")
    
    return copied_files

def parse_schedule():
    """Parse the PUSH_SCHEDULE.md file to extract the daily schedule."""
    schedule_file = Path("PUSH_SCHEDULE.md")
    if not schedule_file.exists():
        print("Error: PUSH_SCHEDULE.md not found!")
        return None
    
    schedule = {}
    current_day = None
    
    with open(schedule_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if line.startswith("**Day "):
            # Extract day number
            day_part = line.split(":")[0]
            day_num = int(day_part.replace("**Day ", "").replace("**", ""))
            current_day = day_num
            schedule[day_num] = []
        elif line.startswith("- ") and current_day is not None:
            # Extract file path
            file_path = line.replace("- ", "").strip()
            schedule[current_day].append(file_path)
    
    return schedule

def create_schedule_json(schedule):
    """Create a JSON file with the schedule for easy parsing by GitHub Actions."""
    schedule_data = {
        "total_days": 70,
        "start_date": "2024-01-01",  # This can be configured
        "schedule": schedule,
        "created_at": datetime.now().isoformat()
    }
    
    with open("_staging/schedule.json", 'w', encoding='utf-8') as f:
        json.dump(schedule_data, f, indent=2)
    
    print("Created _staging/schedule.json")

def validate_file_count():
    """Validate that we have the expected number of files."""
    expected_counts = {
        "beginner": 18,
        "intermediate": 40,
        "algorithms": 10,
        "data_structures": 24,
        "advanced": 44,
        "systems": 4
    }
    
    total_expected = sum(expected_counts.values())
    
    actual_counts = {}
    total_actual = 0
    
    for category in expected_counts.keys():
        if os.path.exists(category):
            count = len(list(Path(category).glob("*.py")))
            actual_counts[category] = count
            total_actual += count
        else:
            actual_counts[category] = 0
    
    print("\nFile count validation:")
    print(f"Expected total: {total_expected}")
    print(f"Actual total: {total_actual}")
    
    for category, expected in expected_counts.items():
        actual = actual_counts.get(category, 0)
        status = "OK" if actual == expected else "MISSING"
        print(f"{status} {category}: {actual}/{expected}")
    
    return total_actual == total_expected

def main():
    """Main function to set up staging directory."""
    print("Setting up staging directory for daily push automation...")
    
    # Validate file counts
    if not validate_file_count():
        print("Warning: File count validation failed!")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            return
    
    # Copy files to staging
    print("\nCopying files to staging directory...")
    copied_files = copy_files_to_staging()
    print(f"Copied {len(copied_files)} files to staging directory")
    
    # Parse and create schedule
    print("\nParsing schedule...")
    schedule = parse_schedule()
    if schedule:
        create_schedule_json(schedule)
        print(f"Parsed schedule for {len(schedule)} days")
    else:
        print("Failed to parse schedule!")
        return
    
    # Create a summary file
    summary = {
        "setup_date": datetime.now().isoformat(),
        "total_files": len(copied_files),
        "schedule_days": len(schedule) if schedule else 0,
        "files_per_day": 2,
        "staging_directory": "_staging"
    }
    
    with open("_staging/setup_summary.json", 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
    
    print("\n[SUCCESS] Staging setup complete!")
    print("[SUCCESS] Files copied to _staging/")
    print("[SUCCESS] Schedule parsed and saved")
    print("[SUCCESS] Ready for daily push automation")

if __name__ == "__main__":
    main()
