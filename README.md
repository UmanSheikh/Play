# Zoom Meeting Auto-Joiner

This Python script automates the process of joining Zoom meetings for multiple users using the Playwright library. It leverages the Playwright Chromium browser, Faker for generating random names, and asyncio for concurrent execution.

## Features

- Automatically joins Zoom meetings with random user names.
- Allows the script to be used by authorized users by checking an external URL.
- Simulates multiple users joining a Zoom meeting at the same time.
- Handles permissions for microphone usage and auto-joins with audio.
- Ability to control the length of time each user stays in the meeting.

## Requirements

- Python 3.7+
- Chromium installed (Playwright will handle this automatically)
- Internet connection

## Installation

1. Clone the repository:

```bash
git clone https://github.com/UmanSheikh/Play.git
```

2. Navigate to the project directory:

```bash
cd your-repo-name
```

3. Install the required Python packages by creating a virtual environment and installing the dependencies:

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install asyncio nest_asyncio playwright Faker requests
```


4. Install Playwright dependencies:

```bash
python -m playwright install
```

## Usage

Ensure that you are allowed to use the script by configuring the `allow2.txt` file hosted on a remote server.

Run the script with the following command:

```bash
python script.py <number_of_users> <meetingcode> <passcode> <time_in_minutes>
```

- `<number_of_users>`: Number of users to join the Zoom meeting.
- `<meetingcode>`: The Zoom meeting code.
- `<passcode>`: The Zoom meeting passcode.
- `<time_in_minutes>`: The time for each user to stay in the meeting.

## Dependencies

Here are the Python packages used in the project:

```txt
asyncio
nest_asyncio
playwright
Faker
requests
```

