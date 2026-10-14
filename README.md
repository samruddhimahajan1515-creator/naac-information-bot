# NAAC Information Bot

An offline prototype for general NAAC accreditation preparation questions. It includes a browser-based chat demo and a Python desktop version.

## Browser demo

Open `index.html` in a modern browser. It needs no installation, server, or API key.

## Python desktop app

Run with Python 3:

```bash
python naac_bot.py
```

The Python app uses Tkinter, which is included with most standard Windows Python installations.

## Features

- Suggested questions and free-text input in the browser demo
- Local topic matching for process, criteria, evidence, and visit preparation
- A simple desktop chat interface in Python
- New-conversation controls and reminders to verify current official guidance

## Limitations

These are demonstrations with a small local response set. They are not connected to an LLM or a live NAAC document collection, and they are not official NAAC services. Verify cycle-specific guidance through the official NAAC portal.

## Project report

See [`docs/NAAC_Information_Bot_Report.pdf`](docs/NAAC_Information_Bot_Report.pdf) for the assignment report and sample interactions.

