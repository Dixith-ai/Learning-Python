# Python Learning Repository

A comprehensive collection of Python programming examples organized by difficulty level, with automated daily push functionality.

## Repository Structure

This repository contains Python code examples organized into the following categories:

- **`beginner/`** - Basic Python concepts and simple algorithms (18 files)
- **`intermediate/`** - Intermediate programming problems and data manipulation (40 files)
- **`algorithms/`** - Core algorithms and sorting techniques (10 files)
- **`data_structures/`** - Data structure implementations and operations (24 files)
- **`advanced/`** - Complex algorithms and advanced programming concepts (44 files)
- **`systems/`** - System design and implementation examples (4 files)

**Total: 140 Python files**

## Daily Push Automation

This repository features an automated daily push system that gradually reveals the codebase over 70 days, pushing 2 files per day in a structured learning progression.

### How It Works

1. **Schedule**: The `PUSH_SCHEDULE.md` file contains a detailed 70-day schedule
2. **Staging**: Files are organized in the `_staging/` directory (git-ignored)
3. **Automation**: GitHub Actions workflow runs daily at 9:00 AM UTC
4. **Progress**: Each day, exactly 2 files are pushed according to the schedule

### Key Files

- **`PUSH_SCHEDULE.md`** - Complete 70-day schedule with file assignments
- **`.github/workflows/daily-push.yml`** - GitHub Actions automation
- **`scripts/setup_staging.py`** - Setup script for organizing files
- **`scripts/check_progress.py`** - Progress monitoring and reporting
- **`_staging/`** - Staging directory (git-ignored)

## Getting Started

### Initial Setup

1. **Run the setup script** to organize files for daily pushing:
   ```bash
   python scripts/setup_staging.py
   ```

2. **Check progress** at any time:
   ```bash
   python scripts/check_progress.py
   ```

3. **View schedule summary**:
   ```bash
   python scripts/check_progress.py --summary
   ```

### Manual Operations

#### Trigger Daily Push Manually
You can manually trigger the daily push workflow:
1. Go to the "Actions" tab in GitHub
2. Select "Daily File Push" workflow
3. Click "Run workflow"
4. Optionally specify a day override (1-70)

#### Override Specific Day
To push files for a specific day:
1. Use the manual trigger with day override
2. Or modify the start date in `_staging/schedule.json`

## Learning Progression

The daily push follows a carefully designed learning progression:

### Days 1-9: Beginner Level
- Basic Python syntax and concepts
- Simple algorithms and problem-solving
- Fundamental programming patterns

### Days 10-29: Intermediate Level
- String manipulation and data processing
- Array and list operations
- Intermediate algorithmic thinking

### Days 30-34: Algorithms
- Core sorting algorithms
- Graph traversal techniques
- Search algorithms

### Days 35-46: Data Structures
- Binary trees and BST operations
- Linked list manipulations
- Stack and queue implementations

### Days 47-69: Advanced Level
- Dynamic programming problems
- Complex graph algorithms
- Advanced data structure problems

### Day 70: Systems
- System design patterns
- Advanced implementation techniques

## Monitoring Progress

### Progress Tracking
The system provides several ways to monitor progress:

1. **GitHub Actions Logs**: Check the Actions tab for daily execution logs
2. **Progress Artifacts**: Download progress.json from workflow artifacts
3. **Local Script**: Run `python scripts/check_progress.py` for detailed analysis

### Progress Metrics
- Files pushed vs. total files
- Current day in the 70-day schedule
- Category-wise file distribution
- Recent commit history
- Next files to be pushed

## Customization

### Modifying the Schedule
1. Edit `PUSH_SCHEDULE.md` to change file assignments
2. Run `python scripts/setup_staging.py` to regenerate the JSON schedule
3. The GitHub Action will automatically use the updated schedule

### Changing Push Frequency
To modify the push frequency:
1. Edit the cron schedule in `.github/workflows/daily-push.yml`
2. Adjust the schedule in `PUSH_SCHEDULE.md` accordingly
3. Update the setup script if needed

### Adding New Files
1. Add files to the appropriate category directory
2. Update `PUSH_SCHEDULE.md` to include the new files
3. Run the setup script to regenerate the schedule

## Technical Details

### GitHub Actions Workflow
- **Trigger**: Daily at 9:00 AM UTC + manual trigger
- **Environment**: Ubuntu latest with Python 3.9
- **Permissions**: Read/write access to repository
- **Artifacts**: Progress tracking and logs

### File Organization
- **Staging Directory**: `_staging/` (git-ignored)
- **Schedule Data**: `_staging/schedule.json`
- **Progress Tracking**: Generated during workflow execution

### Error Handling
- Validates file existence before copying
- Handles missing schedule gracefully
- Provides detailed error messages in logs
- Continues execution even if some files are missing

## Contributing

This repository is designed for learning and demonstration purposes. The daily push system ensures a structured learning experience while maintaining the complete codebase for reference.

## License

This project is open source and available under the MIT License.
