import os
import psutil
import subprocess
import platform


# ASCII Text: BeerBooster
def print_ascii_art():
    print("""
 ____                                    ____              _             
|  _ \ _ __ ___  ___  ___  ___  ___     | __ )  ___   ___ | | __ _ _ __   
| |_) | '__/ _ \/ _ \/ __|/ _ \/ __|____|  _ \ / _ \ / _ \| |/ _` | '_ \  
|  __/| | |  __/  __/\__ \  __/ (_|_____| |_) | (_) | (_) | | (_| | | | | 
|_|   |_|  \___|\___||___/\___|\___|    |____/ \___/ \___/|_|\__,_|_| |_|                                                                         
    """)


# Common Functions
def kill_resource_hogging_processes(threshold=80):
    """
    Kill processes that are consuming more than a specified CPU threshold.
    :param threshold: CPU usage percentage threshold for killing processes.
    """
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['pid'] == os.getpid():
                continue
            if proc.info['cpu_percent'] > threshold:
                psutil.Process(proc.info['pid']).kill()
                print(
                    f"Killed process {proc.info['name']} with PID {proc.info['pid']} using {proc.info['cpu_percent']}% CPU")
        except psutil.NoSuchProcess:
            pass


def clean_temp_files(path):
    """
    Delete temporary files to free up space.
    :param path: Temporary files directory path.
    """
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                try:
                    os.remove(os.path.join(root, name))
                except Exception as e:
                    print(f"Error deleting file {name}: {e}")
            for name in dirs:
                try:
                    os.rmdir(os.path.join(root, name))
                except Exception as e:
                    print(f"Error deleting directory {name}: {e}")
        print("Temporary files have been cleaned.")
    else:
        print("Temporary folder does not exist.")


# Linux-Specific Functions
def clean_memory_linux():
    """
    Free up the system's memory cache on Linux systems.
    """
    os.system('sync; echo 3 > /proc/sys/vm/drop_caches')
    print("Memory cache has been cleared on Linux.")


def optimize_power_settings_linux():
    """
    Optimize Linux power settings to high performance.
    """
    os.system('cpupower frequency-set -g performance')
    print("CPU governor has been set to performance mode on Linux.")


def update_drivers_linux():
    """
    Update system packages including drivers on Linux.
    """
    os.system('sudo apt update && sudo apt upgrade -y')
    print("System packages including drivers have been updated on Linux.")


def optimize_disk_usage_linux():
    """
    Optimize disk usage by removing unused packages and cleaning up on Linux.
    """
    os.system('sudo apt autoremove -y && sudo apt clean')
    print("Unused packages have been removed and apt cache cleaned on Linux.")


def defragment_ext4_filesystem():
    """
    Defragment ext4 filesystem on Linux.
    """
    os.system('e4defrag /')
    print("Defragmented ext4 filesystem on Linux.")


# Windows-Specific Functions
def optimize_power_settings_windows():
    """
    Optimize Windows power settings to high performance.
    """
    os.system('powercfg -setactive SCHEME_MIN')
    print("Power settings have been optimized to High Performance on Windows.")


def update_drivers_windows():
    """
    Check and update drivers on Windows.
    """
    os.system('pnputil.exe /scan-devices')
    print("Drivers have been checked for updates on Windows.")


def defragment_hard_drive_windows():
    """
    Defragment hard drive on Windows.
    """
    os.system('defrag C: /U /V')
    print("Hard drive has been defragmented on Windows.")


def disable_startup_programs_windows():
    """
    Disable unused startup programs on Windows.
    """
    os.system('wmic startup where "User=\'\'" call Disable')
    print("Unused startup programs have been disabled on Windows.")


# Main Function
if __name__ == "__main__":
    print_ascii_art()
    system_type = platform.system()

    # Common Functions (Medium)
    clean_temp_files(os.getenv('TEMP', '/tmp'))  # Pass the appropriate temp folder path

    kill_resource_hogging_processes()

    # OS-Specific Functions
    if system_type == 'Linux':
        clean_memory_linux()  # Medium
        optimize_power_settings_linux()  # Medium
        update_drivers_linux()  # Easy
        optimize_disk_usage_linux()  # Easy
        defragment_ext4_filesystem()  # Hard
    elif system_type == 'Windows':
        optimize_power_settings_windows()  # Medium
        update_drivers_windows()  # Easy
        defragment_hard_drive_windows()  # Hard
        disable_startup_programs_windows()  # Medium
    else:
        print(f"OS-specific optimizations not supported for {system_type}")
