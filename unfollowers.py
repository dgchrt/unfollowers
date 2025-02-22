#!/usr/bin/env python


def extract_users(list_name: str, content: str):
    header = f"{list_name}\nSearch\n"
    list = content.split(header)[1]
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
    print(
        "This program will ask for your list of followers and following from a prominent picture-focused Internet forum, then display who's not following you back. Please open your profile on your browser, open each list when asked, scroll down to load the whole list, select all (Ctrl+A), copy (Ctrl+C) and paste (Shift+Ctrl+V), then hit Enter twice after pasting the content to proceed."
    )
    followers_content = multi_line_input("Copy and paste your followers content here:")
    followers = extract_users("Followers", followers_content)
    print("Followers:")
    print(followers)
    following_content = multi_line_input("Copy and paste your following content here:")
    following = extract_users("Following", following_content)
    print("Following:")
    print(following)

    unfollowers = sorted(following - followers)

    print("Your unfollowers are:")

    for username in unfollowers:
        print(username)
