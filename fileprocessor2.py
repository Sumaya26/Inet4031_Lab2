#!/usr/bin/python3
import sys

def main():
    user_data = []
    for line in sys.stdin:
        if line.startswith('#'):
            continue
        user_info = line.strip().split(':')
        user_data.append(user_info)

    print("Printing out User Data:")
    for user_info in user_data:
        username, password, userid, groupid = user_info
        print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

    print("End of User Data")

if __name__ == "__main__":
    main()
