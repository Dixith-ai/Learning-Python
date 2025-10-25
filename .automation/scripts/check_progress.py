#!/usr/bin/env python3
"""
Progress tracker for daily push automation.
This script shows which files have been pushed and displays progress.
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

def load_schedule():
    """Load the schedule from JSON file."""
    schedule_file = Path("_staging/schedule.json")
    if not schedule_file.exists():
        print("Error: _staging/schedule.json not found!")
        print("Run scripts/setup_staging.py first.")
        return None
    
    with open(schedule_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def check_files_exist():
    """Check which files from the schedule actually exist in the repository."""
    schedule = load_schedule()
    if not schedule:
        return None, None
    
    existing_files = []
    missing_files = []
    
    for day, files in schedule['schedule'].items():
        for file_path in files:
            if os.path.exists(file_path):
                existing_files.append(file_path)
            else:
                missing_files.append(file_path)
    
    return existing_files, missing_files

def get_git_commit_history():
    """Get commit history to determine which files were pushed when."""
    import subprocess
    
    try:
        # Get commit log with file changes
        result = subprocess.run(
            ['git', 'log', '--name-only', '--pretty=format:%H|%ad|%s', '--date=short'],
            capture_output=True, text=True, check=True
        )
        
        commits = []
        current_commit = None
        
        for line in result.stdout.split('\n'):
            if '|' in line and not line.startswith(' '):
                # This is a commit line
                if current_commit:
                    commits.append(current_commit)
                
                parts = line.split('|')
                current_commit = {
                    'hash': parts[0],
                    'date': parts[1],
                    'message': parts[2],
                    'files': []
                }
            elif line.strip() and current_commit:
                # This is a file line
                current_commit['files'].append(line.strip())
        
        if current_commit:
            commits.append(current_commit)
        
        return commits
    
    except subprocess.CalledProcessError:
        print("Warning: Could not get git commit history")
        return []

def analyze_progress():
    """Analyze the current progress of the daily push schedule."""
    schedule = load_schedule()
    if not schedule:
        return
    
    existing_files, missing_files = check_files_exist()
    commits = get_git_commit_history()
    
    # Count files by category
    category_counts = defaultdict(int)
    for file_path in existing_files:
        category = file_path.split('/')[0]
        category_counts[category] += 1
    
    # Calculate progress
    total_files = len(existing_files) + len(missing_files)
    pushed_files = len(existing_files)
    progress_percentage = (pushed_files / total_files * 100) if total_files > 0 else 0
    
    # Find current day based on files pushed
    current_day = 0
    for day, files in schedule['schedule'].items():
        day_num = int(day)
        all_files_exist = all(os.path.exists(f) for f in files)
        if all_files_exist:
            current_day = max(current_day, day_num)
    
    print("=" * 60)
    print("DAILY PUSH PROGRESS REPORT")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    print(f"Overall Progress: {pushed_files}/{total_files} files ({progress_percentage:.1f}%)")
    print(f"Current Day: {current_day}/70")
    print()
    
    print("Files by Category:")
    for category in ['beginner', 'intermediate', 'algorithms', 'data_structures', 'advanced', 'systems']:
        count = category_counts.get(category, 0)
        print(f"  {category.capitalize()}: {count} files")
    print()
    
    if missing_files:
        print(f"Missing Files ({len(missing_files)}):")
        for file_path in missing_files[:10]:  # Show first 10
            print(f"  - {file_path}")
        if len(missing_files) > 10:
            print(f"  ... and {len(missing_files) - 10} more")
        print()
    
    # Show recent commits
    if commits:
        print("Recent Commits:")
        for commit in commits[:5]:  # Show last 5 commits
            date = commit['date']
            message = commit['message']
            file_count = len(commit['files'])
            print(f"  {date}: {message} ({file_count} files)")
        print()
    
    # Show next files to be pushed
    next_day = current_day + 1
    if next_day <= 70 and str(next_day) in schedule['schedule']:
        next_files = schedule['schedule'][str(next_day)]
        print(f"Next Files (Day {next_day}):")
        for file_path in next_files:
            print(f"  - {file_path}")
    elif current_day >= 70:
        print("🎉 All files have been pushed! Schedule complete!")
    else:
        print("No more files scheduled.")

def show_schedule_summary():
    """Show a summary of the entire schedule."""
    schedule = load_schedule()
    if not schedule:
        return
    
    print("\n" + "=" * 60)
    print("SCHEDULE SUMMARY")
    print("=" * 60)
    
    total_files = 0
    for day, files in schedule['schedule'].items():
        total_files += len(files)
    
    print(f"Total Days: {len(schedule['schedule'])}")
    print(f"Total Files: {total_files}")
    print(f"Files per Day: 2 (except last day)")
    print(f"Start Date: {schedule.get('start_date', 'Not specified')}")
    print(f"Created: {schedule.get('created_at', 'Unknown')}")
    
    # Show category breakdown
    category_breakdown = defaultdict(int)
    for day, files in schedule['schedule'].items():
        for file_path in files:
            category = file_path.split('/')[0]
            category_breakdown[category] += 1
    
    print("\nCategory Breakdown:")
    for category, count in sorted(category_breakdown.items()):
        print(f"  {category.capitalize()}: {count} files")

def main():
    """Main function."""
    if len(sys.argv) > 1 and sys.argv[1] == '--summary':
        show_schedule_summary()
    else:
        analyze_progress()
        show_schedule_summary()

if __name__ == "__main__":
    main()
