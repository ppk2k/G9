# G9
# Tor Connection Automation

This project automates the process of connecting to the Tor network and accessing `.onion` sites.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Ensure that Tor is installed and running locally.

## How to Run

You can run the workflow either manually through GitHub Actions or automatically on a schedule (set to run daily at midnight).

## Workflow Trigger

The workflow is triggered on:

- A manual dispatch from GitHub.
- A scheduled cron job (every day at midnight).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
