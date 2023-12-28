import os
from datetime import datetime
import time
import csv
from pynput import mouse, keyboard

# Declare activity_detected as global
global activity_detected
activity_detected = False

# Callback for mouse activity
def on_move(x, y):
    global activity_detected
    activity_detected = True

# Callback for keyboard activity
def on_press(key):
    global activity_detected
    activity_detected = True

def commit_github():
    global activity_detected  # Declare activity_detected as global

    github_username = "<your-username>"
    repo_name = "<repo-name>" # where the script is in
    token = "<token>"

    # Initialize the repository if not already done
    if not os.path.exists('.git'):
        os.system('git init')
        os.system(f'git remote add origin https://github.com/{github_username}/{repo_name}.git')
        os.system('git pull origin master --allow-unrelated-histories')

    csv_file_path = 'commit_log.csv'
    
    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['Commit_Time']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        last_commit_time = None

        # Set up mouse and keyboard listeners
        mouse_listener = mouse.Listener(on_move=on_move)
        keyboard_listener = keyboard.Listener(on_press=on_press)

        mouse_listener.start()
        keyboard_listener.start()

        while True:
            # Wait for activity or timeout (10 seconds)
            start_time = time.time()
            while not activity_detected and time.time() - start_time < 10:
                time.sleep(1)

            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # If activity detected, perform commit
            if activity_detected:
                os.system(f'echo "{current_datetime}" > status_ammar.txt')

                with open('status_ammar.txt', 'r') as status_file:
                    new_commit_time = status_file.read().strip()

                    if new_commit_time != last_commit_time:
                        last_commit_time = new_commit_time

                        os.system('git add .')
                        os.system(f'git commit -m "{current_datetime}"')
                        
                        merge_conflict_detected = os.system('git push -u origin master') != 0

                        if not merge_conflict_detected:
                            print(f"Commit with {current_datetime} successful. Contents of status_ammar.txt committed to GitHub.")
                            
                            # Write commit time and date to CSV file
                            writer.writerow({'Commit_Time': current_datetime})
                            csv_file.flush()  # Ensure the changes are written immediately
                        else:
                            print(f"Merge conflict detected at {current_datetime}. Resolving conflicts...")

                            merge_conflict_message = f"Merge conflict resolved automatically - {current_datetime}"
                            os.system(f'echo "{merge_conflict_message}" | git commit -a --amend --no-edit')
                            os.system('git push -u origin master')

                            print(f"Merge conflict resolved at {current_datetime}, and contents of status_ammar.txt committed to GitHub.")
                    else:
                        print(f"No new changes in status_ammar.txt at {current_datetime}.")
                
                # Reset activity flag
                activity_detected = False

            # Wait for another 10 seconds before checking again
            time.sleep(300)

        mouse_listener.stop()
        keyboard_listener.stop()

commit_github()
