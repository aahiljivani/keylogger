# Key Logger

This is a simple key logger script developed as part of my exploration into basic methods of intrusion within CyberSecurity. It logs keystrokes to a `log.txt` file and handles special keys such as space, enter, and tab.

## Features

- **Keystroke Logging**: Captures all keystrokes and writes them to a `log.txt` file.
- **Escape to Exit**: Press the `Esc` key to stop the program.
- **Special Key Handling**:
  - `Enter`, `Tab`, and `Space` create new lines in the `log.txt` file.
- **Batch Writing**: The logger writes every 10 characters to the `log.txt` file, resetting the buffer after each write.

## How It Works

1. **Keystroke Capture**: The program listens for keystrokes using the `pynput` library.
2. **Buffered Writing**: Every 10 keystrokes are saved to the `log.txt` file.
3. **Exit Mechanism**: Press the `Esc` key to safely stop the logger.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/keylogger.git
   cd keylogger
