# Educational Keylogger Demonstration

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-blue.svg" alt="Platform: Windows">
  <img src="https://img.shields.io/badge/Python-3.6%2B-green.svg" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/Purpose-Educational%20Only-red.svg" alt="Purpose: Educational Only">
</p>

## ⚠️ DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY**

This project demonstrates the basic concepts of keyboard monitoring for educational and research purposes. It is designed to help understand how keyloggers work and the potential privacy implications of such technology.

**IMPORTANT: Using keyloggers without explicit consent is illegal in most jurisdictions and is a violation of privacy. This code should NEVER be used to monitor anyone's activity without their knowledge and consent.**

The author of this code assumes NO LIABILITY for any misuse of this software. By using this code, you accept full responsibility for your actions and agree to use it only in a legal and ethical manner.

## 🎓 Educational Purpose

This demonstration helps to understand:
- How keyboard events can be captured at a system level
- The potential privacy implications of keystroke logging
- How to implement basic input monitoring in Python
- Security awareness and the importance of protecting personal data
- Techniques used to deploy monitoring software via USB devices

## 🔧 Features

- Keystroke logging with detailed reports
- System information collection (OS, username, etc.)
- Special key mapping (Enter, Tab, Function keys, etc.)
- Automated USB deployment package creation
- Log analysis tools with visualization capabilities
- Both visible and hidden execution demonstrations

## 📋 Requirements

- Python 3.6+
- Windows operating system
- pynput library
- matplotlib (optional, for log analysis)

## 🚀 Installation & Basic Usage

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/educational-keylogger.git
   cd educational-keylogger
   ```

2. Install the required libraries:
   ```
   pip install pynput matplotlib
   ```

3. Run the script with:
   ```
   python keylogger.py
   ```

4. Choose from the available options:
   - Run the keylogger demonstration
   - Create a USB deployment package
   - Exit

## 📊 Features Overview

### 1. Standard Keylogger Demonstration

The basic demonstration shows:
- Keyboard event capturing
- Logging to timestamped files
- Special key handling
- Session statistics

### 2. USB Deployment Package

Create a complete educational package for USB deployment that includes:
- Main keylogger script
- Batch launchers and automation scripts
- Log analyzers and extraction tools
- Comprehensive documentation

### 3. Log Analysis

Analyze captured keystroke data to understand:
- Keystroke frequency patterns
- System information collected
- Data visualization tools
- Most common key combinations

## 🖥️ Usage Instructions

### Running the Keylogger Demonstration

1. Open a command prompt and navigate to the directory containing the keylogger.py file.
2. Run the script:
   ```
   python keylogger.py
   ```
3. Choose option 1 from the menu
4. Confirm you understand this is for educational purposes only
5. The keylogger will start capturing keystrokes
6. Press Ctrl+C to stop the demonstration

### Creating a USB Deployment Package

1. Run the keylogger script
2. Choose option 2 from the menu
3. Confirm you understand this is for educational purposes only
4. Enter a directory name for the package (or use the default)
5. Copy the generated files to a USB drive for demonstration

### Log Analysis and Visualization

After running the demonstration:
1. Navigate to the logs directory
2. Run the analysis tool:
   ```
   python log_analyzer.py
   ```
3. Select the log file to analyze
4. View statistics and visualizations of captured keystrokes

## 💾 USB Drive Deployment Instructions

For educational demonstration of how such tools could potentially be deployed via removable media:

1. Create the deployment package using option 2 in the main script
2. Copy all files from the generated directory to a USB drive
3. When plugged into a Windows system with Python installed:
   - Run `launch_keylogger_demo.bat` for the visible demonstration
   - The educational demonstration will install dependencies and run
4. Logs will be saved in a `logs` folder on the USB drive

## 🔍 Understanding the Logs

1. Logs are stored in a `logs` folder in the same directory as the script
2. Each log file is named with a timestamp (e.g., `keylog_20230615_123045.txt`)
3. Log files contain:
   - A header with timestamp and system information
   - The captured keystrokes with special key notation
   - A footer with session end time

## 🛡️ Protecting Yourself from Real Keyloggers

This educational demonstration highlights why you should:

1. Keep your antivirus software updated
2. Be cautious about what software you install
3. Use two-factor authentication for sensitive accounts
4. Consider using password managers instead of typing sensitive passwords
5. Be wary of unknown USB devices
6. Never run unknown executables from removable media

## ⚖️ Legal and Ethical Considerations

Using keyloggers without consent may violate:
- Computer Fraud and Abuse Act (US)
- Electronic Communications Privacy Act (US)
- Data Protection laws (EU/UK)
- Similar laws in other jurisdictions

Potential legal consequences include:
- Criminal charges
- Civil liability
- Fines and imprisonment

## 🔧 Technical Implementation

This demonstration uses the `pynput` library to monitor keyboard events at a system level. It captures both regular keystrokes and special keys, writing them to a log file with timestamps.

The implementation is deliberately simplified for educational purposes and does not include any features that would make it suitable for malicious use, such as:
- Hiding itself from detection
- Starting automatically with the system
- Transmitting data over networks
- Capturing screenshots or other sensitive information

## 📜 License

This educational code is provided under the MIT License, with the explicit restriction that it must only be used for educational and ethical purposes. See the [LICENSE](LICENSE) file for details.
