#!/usr/bin/env python


def extract_users(list_name: str, content: str):
    header = f"{list_name}\nSearch\n"
    footer = f"\nSuggested for you\n"
    list = content.split(header)[1].split(footer)[0]
    lines = list.splitlines()
    filtered_lines = [line for line in lines if line.strip() != "·"]
    users = [line for line in filtered_lines if valid_user(line)]
    return set(users)


def multi_line_input(prompt):
    print(prompt)
    lines = []
    empty_count = 0

    while True:
        line = input()
        if line.strip() == "":
            empty_count += 1
            if empty_count == 2:
                break
        else:
            empty_count = 0

        lines.append(line)

    return "\n".join(lines)


def valid_user(name: str):
    return name == name.lower().replace(" ", "")


if __name__ == "__main__":
    followers_content = multi_line_input("Copy and paste your followers content here:")
    followers = extract_users("Followers", followers_content)
    following_content = multi_line_input("Copy and paste your following content here:")
    following = extract_users("Following", following_content)
    unfollowers = sorted(following - followers)
    print(f"You have {len(unfollowers)} unfollowers:")

    for username in unfollowers:
        print(username)
