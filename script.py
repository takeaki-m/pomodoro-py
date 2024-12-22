import sys
import os
import datetime
import time
import subprocess

target_file_path = os.path.expanduser('~/pomodoro-history.csv')
def check_log_files():
    if os.path.isfile(target_file_path):
        print("pomodoro file exists")
    else:
        with open(target_file_path, 'w') as f:
            pass
        print("pomodoro file created")
def count_down(minutes):
    """
    count down the number of minutes

    :param minutes: total time
    :return:nothing
    """
    base_seconds = minutes * 60
    seconds = minutes * 60
    try:
        while seconds > 0:
            time.sleep(1)
            position = seconds / base_seconds
            print(position)
            if (seconds / 60) % 5 == 0:
                multiple = 10 * position
                print(("#" * int(multiple)) + ": " + str(100 * position) + "%")
            seconds -= 1
    except KeyboardInterrupt:
        print("interrupted")
def write_pomodoro(message, tasks):
    delta = datetime.timedelta(hours=9)
    jst = datetime.timezone(delta, 'JST')
    now = datetime.datetime.now(jst)
    print(now)
    f = open(target_file_path, '+a')
    new_lines = message + "," + tasks + "," + str(now) + "\n"
    print(new_lines)
    f.write(new_lines)
    f.close()

def read_latest_task_name():
    with open(target_file_path, 'r') as f:
        lines = f.readlines()
        last_lines = lines[-1]
        split_list = last_lines.split(',')
        print(split_list[1])
        return split_list[1]

def beep():
    command = ["afplay", "/System/Library/Sounds/Ping.aiff"]
    subprocess.call(command)

def interactive_choice(options_list):
    """
    post the options and choose one

    :param options_list:
    :return: selected option
    """
    try:
        if not options_list:
                print("specify options")
                return None
        while True:
                print("select one")
                for i, option in enumerate(options_list):
                    print(f"{i}, {option}")
                choice = input(">> ")
                if choice.isdigit():
                    choice_number = int(choice)
                    if choice_number < len(options_list) - 1:
                        return options_list[choice_number]
                print("invalid option, please try again")
    except KeyboardInterrupt:
        print("cancelled")

if __name__ == "__main__":
    options = ["START", "REST"]
    selected = interactive_choice(options)
    print(f"your choice: {selected}")
    if selected == 'START':
        print("input task name")
        task_name = input(">> ")
        check_log_files()
        write_pomodoro("START", task_name)
        beep()
        count_down(25)
        write_pomodoro("FINISH", read_latest_task_name())
        beep()
    elif selected == 'REST':
        check_log_files()
        write_pomodoro("START", "REST")
        beep()
        count_down(5)
        write_pomodoro("FINISH", "REST")
        beep()
