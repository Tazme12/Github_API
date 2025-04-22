import requests
import os

def main():
    while True:
        username = input("Please enter GitHub username: ")

        url = f"https://api.github.com/users/{username}/events"
        data = requests.get(url)

        if data.status_code == 200:
            data = data.json()

        for events in data:

            if events ['type'] == 'IssueCommentEvent':
                    print(f"- {username} commented on issue {events['payload']['issue']['number']}")
            elif events['type'] == 'PushEvent':
                print(f"- {username} pushed to {events['repo']['name']}")
            elif events['type'] == 'IssuesEvent':
                print(f"- {username} created issue {events['payload']['issue']['number']}")
            elif events['type'] == 'WatchEvent':
                print(f"- {username} starred {events['repo']['name']}")
            elif events['type'] == 'PullRequestEvent':
                print(f"- {username} created pull request {events['payload']['pull_request']['number']}")
            elif events['type'] == 'PullRequestReviewEvent':
                print(f"- {username} reviewed pull request {events['payload']['pull_request']['number']}")
            elif events['type'] == 'PullRequestReviewCommentEvent':
                print(f"- {username} commented on pull request {events['payload']['pull_request']['number']}")
            elif events['type'] == 'CreateEvent':
                print(f"- {username} created {events['payload']['ref_type']} {events['payload']['ref']}")
            else:
                print(f"- {username} {events['type']}")
        else:
            print("Error, request invalid or timed out")

if __name__ == "__main__":
    main()