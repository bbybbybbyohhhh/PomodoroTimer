import time

def countdown_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r')  # The \r helps overwrite the line, creating a countdown effect
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

def pomodoro_session(work_time=25, short_break=5, long_break=15, cycles=4):
    for cycle in range(1, cycles + 1):
        print(f"\nCycle {cycle} of {cycles}: Time to work!")
        countdown_timer(work_time)
        if cycle < cycles:
            print(f"\nShort break time! Enjoy {short_break} minutes of rest.")
            countdown_timer(short_break)
        else:
            print(f"\nCycle {cycle} complete. Time for a long break! Enjoy {long_break} minutes of rest.")
            countdown_timer(long_break)

def main():
    print("Welcome to the Pomodoro Timer!")
    
    # Default values for work time and breaks
    work_time = int(input("Enter work session length in minutes (default is 25): ") or 25)
    short_break = int(input("Enter short break length in minutes (default is 5): ") or 5)
    long_break = int(input("Enter long break length in minutes (default is 15): ") or 15)
    cycles = int(input("Enter the number of work cycles before a long break (default is 4): ") or 4)
    
    # Start the Pomodoro session
    pomodoro_session(work_time, short_break, long_break, cycles)

if __name__ == "__main__":
    main()
