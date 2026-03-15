# main.py
import time

def main():
    print("Starting background task...")
    count = 0
    while True:
        print(f"Tick {count}")
        count += 1
        time.sleep(5)

if __name__ == "__main__":
    main()