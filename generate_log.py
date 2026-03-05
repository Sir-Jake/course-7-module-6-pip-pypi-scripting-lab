import requests
from datetime import datetime

def fetch_data():
    """Fetches a sample post from JSONPlaceholder API."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}

def run_automation():
    """Main logic for the automation tool."""
    # 1. Fetch data
    post = fetch_data()
    title = post.get("title", "No title found")
    print(f"Fetched Post Title: {title}")

    # 2. Write to log file
    log_data = [
        "User logged in",
        f"Fetched data: {title}",
        "Report exported"
    ]
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

if __name__ == "__main__":
    run_automation()
