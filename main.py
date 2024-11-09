import os
import platform
import sys

# Define the shutdown function
def shutdown():
    # Get the current operating system
    current_platform = platform.system().lower()
    
    # Check the OS and perform shutdown
    if current_platform == 'windows':
        print("Shutting down Windows system...")
        os.system("shutdown /s /f /t 0")  # /s = shutdown, /f = force close apps, /t 0 = no delay
    elif current_platform == 'linux' or current_platform == 'darwin':  # Linux or macOS
        print("Shutting down Unix-based system (Linux/macOS)...")
        os.system("sudo shutdown now")  # Requires sudo privileges
    else:
        print(f"Unsupported OS: {current_platform}. Cannot shutdown.")

# Main function to test the shutdown function
def main():
    user_input = input("Do you want to shutdown the system? (yes/no): ").lower()
    
    if user_input == "yes":
        shutdown()
    else:
        print("Shutdown aborted.")

if __name__ == "__main__":
    main()
